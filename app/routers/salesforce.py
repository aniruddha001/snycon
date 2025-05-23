import os
import requests
from dotenv import load_dotenv

load_dotenv()  # 👈 Load the .env file

# 👇 Now fetch from environment instead of hardcoding
SF_CLIENT_ID = os.getenv('SF_CLIENT_ID')
SF_CLIENT_SECRET = os.getenv('SF_CLIENT_SECRET')
SF_USERNAME = os.getenv('SF_USERNAME')
SF_PASSWORD = os.getenv('SF_PASSWORD')
SF_SECURITY_TOKEN = os.getenv('SF_SECURITY_TOKEN')

def salesforce_login():
    url = "https://connect-speed-6644.my.salesforce.com/services/oauth2/token"
    data = {
        'grant_type': 'password',
        'client_id': SF_CLIENT_ID,
        'client_secret': SF_CLIENT_SECRET,
        'username': SF_USERNAME,
        'password': SF_PASSWORD + SF_SECURITY_TOKEN
    }

    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()

def fetch_salesforce_contacts(access_token, instance_url):
    query = "SELECT Id, FirstName, LastName, Email FROM Contact LIMIT 5"
    url = f"{instance_url}/services/data/v57.0/query?q={query}"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['records']
