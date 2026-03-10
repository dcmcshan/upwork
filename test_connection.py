#!/usr/bin/env python3
"""
Simple script to test Upwork API connection.
"""
from upwork_api_client import UpworkAPIClient
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    print("=" * 60)
    print("Upwork API Connection Test")
    print("=" * 60)
    print()
    
    try:
        client = UpworkAPIClient()
        
        if not client.access_token:
            print("⚠ No access token found in .env file")
            print("\nTo get an access token, you need to:")
            print("1. Register your application at https://www.upwork.com/services/api/apply")
            print("2. Get your Client ID and Client Secret")
            print("3. Set up OAuth2 flow to get access token")
            print("\nYou can run: python upwork_api_client.py")
            print("to interactively get an access token.")
        else:
            print("Testing connection with existing access token...")
            print()
            
            if client.test_connection():
                print("\n" + "=" * 60)
                print("✓ Connection successful!")
                print("=" * 60)
            else:
                print("\n" + "=" * 60)
                print("✗ Connection failed")
                print("=" * 60)
                print("\nPossible issues:")
                print("- Access token may be expired (try refreshing)")
                print("- Invalid credentials in .env file")
                print("- Network connectivity issues")
                
    except ValueError as e:
        print(f"\n✗ Configuration error: {str(e)}")
        print("\nPlease ensure your .env file contains:")
        print("- UPWORK_CLIENT_ID")
        print("- UPWORK_CLIENT_SECRET")
        print("- UPWORK_ACCESS_TOKEN (optional, for testing)")
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
