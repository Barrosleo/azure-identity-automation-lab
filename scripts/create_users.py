"""
Purpose:
Creates Azure Entra ID users using Microsoft Graph.
Demonstrates basic identity provisioning automation.
"""

import requests
from auth import get_access_token

TOKEN = get_access_token()
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

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

for user in USERS:
    payload = {
        "accountEnabled": True,
        "displayName": user["displayName"],
        "mailNickname": user["mailNickname"],
        "userPrincipalName": user["userPrincipalName"],
        "passwordProfile": {
            "forceChangePasswordNextSignIn": True,
            "password": "TempP@ssw0rd!"
        }
    }

    response = requests.post(
        "https://graph.microsoft.com/v1.0/users",
        headers=HEADERS,
        json=payload
    )

    print(response.status_code, response.text)

