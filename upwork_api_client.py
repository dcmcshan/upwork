"""
Upwork API Client with OAuth2 Authentication
"""
import os
import json
import logging
from typing import Dict, Optional, Any
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class UpworkAPIClient:
    """
    Client for connecting to Upwork API using OAuth2 authentication.
    
    Upwork API Documentation: https://developers.upwork.com/
    """
    
    # Upwork API endpoints
    BASE_URL = "https://www.upwork.com/api"
    AUTH_URL = "https://www.upwork.com/ab/account-security/oauth2/authorize"
    TOKEN_URL = "https://www.upwork.com/api/v3/oauth2/token"
    
    # Upwork GraphQL endpoint (primary API)
    GRAPHQL_URL = "https://api.upwork.com/graphql"
    
    def __init__(self, client_id: Optional[str] = None, 
                 client_secret: Optional[str] = None,
                 access_token: Optional[str] = None,
                 refresh_token: Optional[str] = None):
        """
        Initialize Upwork API client.
        
        Args:
            client_id: Upwork OAuth2 client ID
            client_secret: Upwork OAuth2 client secret
            access_token: OAuth2 access token (if already obtained)
            refresh_token: OAuth2 refresh token (if available)
        """
        load_dotenv()
        
        self.client_id = client_id or os.getenv('UPWORK_CLIENT_ID')
        self.client_secret = client_secret or os.getenv('UPWORK_CLIENT_SECRET')
        self.access_token = access_token or os.getenv('UPWORK_ACCESS_TOKEN')
        self.refresh_token = refresh_token or os.getenv('UPWORK_REFRESH_TOKEN')
        
        if not self.client_id or not self.client_secret:
            raise ValueError(
                "UPWORK_CLIENT_ID and UPWORK_CLIENT_SECRET must be provided "
                "either as parameters or in .env file"
            )
        
        # Initialize OAuth2 session
        self.session = None
        if self.access_token:
            self._initialize_session()
    
    def _initialize_session(self):
        """Initialize OAuth2 session with access token."""
        if not self.access_token:
            raise ValueError("Access token is required to initialize session")
        
        self.session = OAuth2Session(
            client_id=self.client_id,
            token={
                'access_token': self.access_token,
                'refresh_token': self.refresh_token,
                'token_type': 'Bearer'
            }
        )
    
    def get_authorization_url(self, redirect_uri: str, 
                             scopes: Optional[list] = None) -> str:
        """
        Get the authorization URL for OAuth2 flow.
        
        Args:
            redirect_uri: Redirect URI registered with Upwork
            scopes: List of OAuth2 scopes (default: basic profile and jobs)
            
        Returns:
            Authorization URL
        """
        if scopes is None:
            scopes = ['r_myprofile', 'r_jobs', 'w_jobs']
        
        oauth = OAuth2Session(
            client_id=self.client_id,
            redirect_uri=redirect_uri,
            scope=scopes
        )
        
        authorization_url, state = oauth.authorization_url(self.AUTH_URL)
        return authorization_url
    
    def get_access_token_from_code(self, authorization_code: str, 
                                   redirect_uri: str) -> Dict[str, Any]:
        """
        Exchange authorization code for access token.
        
        Args:
            authorization_code: Authorization code from OAuth2 callback
            redirect_uri: Redirect URI used in authorization
            
        Returns:
            Token response containing access_token, refresh_token, etc.
        """
        oauth = OAuth2Session(
            client_id=self.client_id,
            redirect_uri=redirect_uri
        )
        
        token = oauth.fetch_token(
            self.TOKEN_URL,
            code=authorization_code,
            client_secret=self.client_secret
        )
        
        self.access_token = token['access_token']
        self.refresh_token = token.get('refresh_token')
        self._initialize_session()
        
        return token
    
    def refresh_access_token(self) -> Dict[str, Any]:
        """
        Refresh the access token using refresh token.
        
        Returns:
            New token response
        """
        if not self.refresh_token:
            raise ValueError("Refresh token is required to refresh access token")
        
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        
        token = oauth.refresh_token(
            self.TOKEN_URL,
            refresh_token=self.refresh_token,
            client_id=self.client_id,
            client_secret=self.client_secret
        )
        
        self.access_token = token['access_token']
        self.refresh_token = token.get('refresh_token', self.refresh_token)
        self._initialize_session()
        
        return token
    
    def _make_graphql_request(self, query: str, variables: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Make a GraphQL API request.
        
        Args:
            query: GraphQL query string
            variables: GraphQL variables
            
        Returns:
            API response as dictionary
        """
        if not self.session:
            if not self.access_token:
                raise ValueError(
                    "No access token available. Please authenticate first."
                )
            self._initialize_session()
        
        payload = {'query': query}
        if variables:
            payload['variables'] = variables
        
        try:
            response = self.session.post(
                self.GRAPHQL_URL,
                json=payload,
                headers={
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                }
            )
            response.raise_for_status()
            result = response.json()
            if 'errors' in result:
                raise Exception(f"GraphQL errors: {result['errors']}")
            return result.get('data', result)
        except Exception as e:
            logger.error(f"GraphQL request failed: {str(e)}")
            if hasattr(e, 'response') and e.response is not None:
                try:
                    logger.error(f"Response: {e.response.text[:500]}")
                except:
                    pass
            raise
    
    def _make_request(self, method: str, endpoint: str, 
                     params: Optional[Dict] = None,
                     data: Optional[Dict] = None,
                     json_data: Optional[Dict] = None,
                     use_api_key: bool = False) -> Dict[str, Any]:
        """
        Make an authenticated API request.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint (relative to BASE_URL)
            params: URL parameters
            data: Form data
            json_data: JSON data
            use_api_key: If True, use API key authentication instead of OAuth2
            
        Returns:
            API response as dictionary
        """
        url = f"{self.BASE_URL}/{endpoint.lstrip('/')}"
        
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        
        # Try API key authentication if requested
        if use_api_key and self.access_token:
            headers['X-Upwork-API-Key'] = self.access_token
            # Use requests directly instead of OAuth2 session
            import requests
            try:
                response = requests.request(
                    method=method,
                    url=url,
                    params=params,
                    data=data,
                    json=json_data,
                    headers=headers
                )
                response.raise_for_status()
                return response.json()
            except Exception as e:
                logger.error(f"API key request failed: {str(e)}")
                raise
        
        # Use OAuth2 authentication
        if not self.session:
            if not self.access_token:
                raise ValueError(
                    "No access token available. Please authenticate first."
                )
            self._initialize_session()
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                data=data,
                json=json_data,
                headers=headers
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"API request failed: {str(e)}")
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_text = e.response.text[:500] if hasattr(e.response, 'text') else str(e.response)
                    logger.error(f"Response: {error_text}")
                except:
                    pass
            raise
    
    def get_profile(self) -> Dict[str, Any]:
        """
        Get current user's profile.
        
        Returns:
            User profile data
        """
        # Try GraphQL first (primary API)
        try:
            query = """
            query {
                freelancer {
                    profile {
                        title
                        publicName
                        city
                        country
                    }
                }
            }
            """
            return self._make_graphql_request(query)
        except Exception as e:
            logger.warning(f"GraphQL profile request failed: {str(e)}, trying REST API")
            # Fallback to REST API endpoints
            endpoints = [
                '/profiles/v2/providers/me.json',
                '/profiles/v1/providers/me.json',
                '/api/profiles/v1/providers/me.json'
            ]
            # Try with API key authentication first
            for endpoint in endpoints:
                try:
                    return self._make_request('GET', endpoint, use_api_key=True)
                except Exception as e2:
                    logger.warning(f"API key auth failed with {endpoint}: {str(e2)}")
                    try:
                        return self._make_request('GET', endpoint, use_api_key=False)
                    except Exception as e3:
                        logger.warning(f"OAuth2 auth failed with {endpoint}: {str(e3)}")
                        continue
            raise Exception("Failed to get profile with all known endpoints and auth methods")
    
    def search_jobs(self, query: str, page: int = 0, 
                   page_size: int = 10, **kwargs) -> Dict[str, Any]:
        """
        Search for jobs.
        
        Args:
            query: Search query string
            page: Page number (0-indexed)
            page_size: Number of results per page
            **kwargs: Additional search parameters
            
        Returns:
            Job search results
        """
        params = {
            'q': query,
            'paging': page,
            'paging_limit': page_size,
            **kwargs
        }
        
        # Try different API endpoints based on Upwork API version
        endpoints = [
            '/profiles/v2/search/jobs.json',
            '/jobs/v2/search/jobs.json',
            '/jobs/v1/search.json'
        ]
        
        for endpoint in endpoints:
            try:
                return self._make_request('GET', endpoint, params=params)
            except Exception as e:
                logger.warning(f"Failed with endpoint {endpoint}: {str(e)}")
                continue
        
        raise Exception("Failed to search jobs with all known endpoints")
    
    def get_job_details(self, job_id: str) -> Dict[str, Any]:
        """
        Get details of a specific job.
        
        Args:
            job_id: Job ID
            
        Returns:
            Job details
        """
        endpoints = [
            f'/jobs/v2/jobs/{job_id}.json',
            f'/jobs/v1/jobs/{job_id}.json'
        ]
        
        for endpoint in endpoints:
            try:
                return self._make_request('GET', endpoint)
            except Exception as e:
                logger.warning(f"Failed with endpoint {endpoint}: {str(e)}")
                continue
        
        raise Exception("Failed to get job details with all known endpoints")
    
    def test_connection(self) -> bool:
        """
        Test the API connection by getting user profile.
        
        Returns:
            True if connection is successful, False otherwise
        """
        if not self.access_token:
            logger.error("✗ No access token found. Please set UPWORK_ACCESS_TOKEN in .env file or get one using the OAuth2 flow.")
            return False
        
        try:
            profile = self.get_profile()
            logger.info("✓ Successfully connected to Upwork API")
            
            # Try to extract profile info from different response formats
            profile_data = profile
            if 'freelancer' in profile:
                profile_data = profile['freelancer'].get('profile', {})
            elif 'profile' in profile:
                profile_data = profile['profile']
            
            title = profile_data.get('title', 'N/A')
            name = profile_data.get('publicName', profile_data.get('name', 'N/A'))
            logger.info(f"Profile: {name} - {title}")
            return True
        except ValueError as e:
            logger.error(f"✗ Configuration error: {str(e)}")
            return False
        except Exception as e:
            logger.error(f"✗ Connection test failed: {str(e)}")
            logger.info("This might be because:")
            logger.info("1. Access token is invalid or expired")
            logger.info("2. API endpoints have changed")
            logger.info("3. Network connectivity issues")
            logger.info("4. Upwork API credentials are incorrect")
            return False


def main():
    """Test the Upwork API connection."""
    try:
        client = UpworkAPIClient()
        
        if not client.access_token:
            print("\n⚠ No access token found in environment variables.")
            print("\nTo get an access token:")
            print("1. Get authorization URL:")
            redirect_uri = input("Enter your redirect URI: ").strip()
            auth_url = client.get_authorization_url(redirect_uri)
            print(f"\nVisit this URL to authorize:\n{auth_url}\n")
            
            auth_code = input("Enter the authorization code from the callback: ").strip()
            token = client.get_access_token_from_code(auth_code, redirect_uri)
            print(f"\n✓ Access token obtained!")
            print(f"Access Token: {token['access_token'][:20]}...")
            if 'refresh_token' in token:
                print(f"Refresh Token: {token['refresh_token'][:20]}...")
        else:
            print("Testing connection with existing access token...")
            if client.test_connection():
                print("\n✓ Connection successful!")
            else:
                print("\n✗ Connection failed. Please check your credentials.")
                
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        print(f"\n✗ Error: {str(e)}")


if __name__ == "__main__":
    main()
