"""
Purpose:
Creates security groups in Azure Entra ID.
"""

import requests
from auth import get_access_token

TOKEN = get_access_token()
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

GROUPS = [
    "GG-Engineering",
    "GG-ITAdmins",
    "GG-AllStaff"
]

for group in GROUPS:
    payload = {
        "displayName": group,
        "mailEnabled": False,
        "mailNickname": group.lower(),
        "securityEnabled": True
    }

    response = requests.post(
        "https://graph.microsoft.com/v1.0/groups",
        headers=HEADERS,
        json=payload
    )

    print(response.status_code, response.text)
