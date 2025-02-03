from dotenv import load_dotenv
import os
import requests

load_dotenv()




# Use the actual API endpoint URL, not the Swagger documentation URL
loginURL = "https://wagerapi.amwager.com/api/user/login"  # This is an example, use the actual endpoint

params = {
    "Username": os.getenv("AMWAGER_USERNAME"),
    "Password": os.getenv("AMWAGER_PASSWORD"),
    "Tmsid": "string",
    "TalonPayload": "string"
}

# If you need to include headers
headers = {
    "Content-Type": "application/json"
}

response = requests.post(loginURL, json=params, headers=headers)
print(response.status_code)
token = response.json()['Token']
print(token)
# print(response.json())
# print(response.headers)

# Use the actual API endpoint URL, not the Swagger documentation URL    