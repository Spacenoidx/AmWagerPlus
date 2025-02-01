url = "https://wagerapi.amwager.com/api/ToteProgram/GetAllEvents"
import requests
headers = {
    'Content-Type': 'application/json',
    'token': '93d73d6d-8fe3-4bb0-ba63-23cf6ef464f3',}

response = requests.get(url, headers=headers)
# print(response.json())

for i in response.json()['ToteResponse']['Events']:
    print(i)
    
### https://wagerapi.amwager.com/swagger/ui/index#!/DataProducts/DataProducts_DownloadDataProduct