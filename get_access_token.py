#!/usr/bin/env python3
"""
Interactive script to help you get an Upwork OAuth2 access token.
"""
import os
import sys
from upwork_api_client import UpworkAPIClient
from dotenv import load_dotenv, set_key

load_dotenv()

def main():
    print("=" * 70)
    print("Upwork OAuth2 Access Token Generator")
    print("=" * 70)
    print()
    
    # Check for existing credentials
    client_id = os.getenv('UPWORK_CLIENT_ID')
    client_secret = os.getenv('UPWORK_CLIENT_SECRET')
    
    if not client_id or client_id == 'your_client_id':
        print("⚠ No valid UPWORK_CLIENT_ID found in .env file")
        print()
        print("To get your Client ID and Secret:")
        print("1. Go to: https://www.upwork.com/services/api/apply")
        print("2. Create a new application")
        print("3. Get your Client ID and Client Secret")
        print("4. Add them to your .env file:")
        print("   UPWORK_CLIENT_ID=your_actual_client_id")
        print("   UPWORK_CLIENT_SECRET=your_actual_client_secret")
        print()
        return
    
    if not client_secret or client_secret == 'your_client_secret':
        print("⚠ No valid UPWORK_CLIENT_SECRET found in .env file")
        print()
        print("Please add UPWORK_CLIENT_SECRET to your .env file")
        print()
        return
    
    print(f"✓ Found Client ID: {client_id[:10]}...")
    print()
    
    # Initialize client
    try:
        client = UpworkAPIClient()
    except Exception as e:
        print(f"✗ Error initializing client: {str(e)}")
        return
    
    # Get redirect URI
    print("Enter your OAuth2 redirect URI (must match what you set in Upwork Developer Portal):")
    print("Common examples:")
    print("  - http://localhost:8080/callback")
    print("  - https://yourdomain.com/callback")
    print("  - urn:ietf:wg:oauth:2.0:oob (for desktop apps)")
    print()
    redirect_uri = input("Redirect URI: ").strip()
    
    if not redirect_uri:
        print("✗ Redirect URI is required")
        return
    
    # Get authorization URL
    print()
    print("Getting authorization URL...")
    try:
        auth_url = client.get_authorization_url(
            redirect_uri=redirect_uri,
            scopes=['r_myprofile', 'r_jobs', 'w_jobs']
        )
        
        print()
        print("=" * 70)
        print("STEP 1: Authorize the application")
        print("=" * 70)
        print()
        print("Visit this URL in your browser:")
        print()
        print(auth_url)
        print()
        print("After authorizing, you'll be redirected to your redirect URI")
        print("with an authorization code in the URL.")
        print()
        print("=" * 70)
        print("STEP 2: Get the authorization code")
        print("=" * 70)
        print()
        print("The authorization code will be in the URL as 'code=...'")
        print("Example: http://localhost:8080/callback?code=abc123...")
        print()
        
        auth_code = input("Enter the authorization code: ").strip()
        
        if not auth_code:
            print("✗ Authorization code is required")
            return
        
        print()
        print("Exchanging authorization code for access token...")
        
        # Exchange code for token
        token = client.get_access_token_from_code(auth_code, redirect_uri)
        
        print()
        print("=" * 70)
        print("✓ Success! Access token obtained")
        print("=" * 70)
        print()
        print("Your access token:")
        print(f"  {token['access_token'][:50]}...")
        print()
        
        if 'refresh_token' in token:
            print("Your refresh token:")
            print(f"  {token['refresh_token'][:50]}...")
            print()
        
        # Ask to save to .env
        save = input("Save to .env file? (y/n): ").strip().lower()
        if save == 'y':
            env_path = '.env'
            set_key(env_path, 'UPWORK_ACCESS_TOKEN', token['access_token'])
            if 'refresh_token' in token:
                set_key(env_path, 'UPWORK_REFRESH_TOKEN', token['refresh_token'])
            print()
            print("✓ Tokens saved to .env file")
            print()
            print("You can now test the connection:")
            print("  python test_connection.py")
        else:
            print()
            print("Add these to your .env file:")
            print(f"UPWORK_ACCESS_TOKEN={token['access_token']}")
            if 'refresh_token' in token:
                print(f"UPWORK_REFRESH_TOKEN={token['refresh_token']}")
        
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        print()
        print("Common issues:")
        print("- Invalid redirect URI (must match Upwork Developer Portal)")
        print("- Authorization code expired (they expire quickly)")
        print("- Invalid authorization code")
        return

if __name__ == "__main__":
    main()
