"""
Purpose:
Assigns users to groups using Microsoft Graph.
Demonstrates group-based access control automation.
"""

import requests
from auth import get_access_token

TOKEN = get_access_token()
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# Replace with real IDs after creation
GROUP_ID = "group-object-id"
USER_ID = "user-object-id"

payload = {
    "@odata.id": f"https://graph.microsoft.com/v1.0/directoryObjects/{USER_ID}"
}

response = requests.post(
    f"https://graph.microsoft.com/v1.0/groups/{GROUP_ID}/members/$ref",
    headers=HEADERS,
    json=payload
)

print(response.status_code, response.text)
