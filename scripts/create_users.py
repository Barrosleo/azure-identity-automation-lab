"""
Purpose:
Creates Azure Entra ID users using Microsoft Graph.
Demonstrates basic identity provisioning automation.

The temporary password is read from the TEMP_USER_PASSWORD
environment variable (set it in .env), never hard-coded.
"""

import os
import sys

import requests
from auth import get_access_token  # auth.py also loads the .env file

GRAPH_USERS_URL = "https://graph.microsoft.com/v1.0/users"

TEMP_PASSWORD = os.getenv("TEMP_USER_PASSWORD")
if not TEMP_PASSWORD:
    sys.exit("TEMP_USER_PASSWORD is not set. Add it to your .env file.")

USERS = [
    {
        "displayName": "John Doe",
        "userPrincipalName": "john.doe@lab.onmicrosoft.com",
        "mailNickname": "johndoe"
    },
    {
        "displayName": "Sarah Smith",
        "userPrincipalName": "sarah.smith@lab.onmicrosoft.com",
        "mailNickname": "sarahsmith"
    }
]


def create_user(user, headers):
    payload = {
        "accountEnabled": True,
        "displayName": user["displayName"],
        "mailNickname": user["mailNickname"],
        "userPrincipalName": user["userPrincipalName"],
        "passwordProfile": {
            "forceChangePasswordNextSignIn": True,
            "password": TEMP_PASSWORD
        }
    }

    response = requests.post(GRAPH_USERS_URL, headers=headers, json=payload, timeout=30)

    if response.status_code == 201:
        print(f"Created: {user['userPrincipalName']}")
    else:
        error = response.json().get("error", {}).get("message", response.text)
        print(f"Failed:  {user['userPrincipalName']} ({response.status_code}) {error}")


def main():
    token = get_access_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    for user in USERS:
        create_user(user, headers)


if __name__ == "__main__":
    main()
