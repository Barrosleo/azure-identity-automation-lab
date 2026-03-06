"""
Purpose:
Audits current users and groups in Azure Entra ID.
Useful for validation and reporting.
"""

import requests
from auth import get_access_token

TOKEN = get_access_token()
HEADERS = {
    "Authorization": f"Bearer {TOKEN}"
}

users = requests.get(
    "https://graph.microsoft.com/v1.0/users",
    headers=HEADERS
).json()

groups = requests.get(
    "https://graph.microsoft.com/v1.0/groups",
    headers=HEADERS
).json()

print(f"Users found: {len(users.get('value', []))}")
print(f"Groups found: {len(groups.get('value', []))}")
