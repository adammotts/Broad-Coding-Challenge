import requests

ENDPOINT = 'https://api-v3.mbta.com'
API_KEY = "63dc0dc1290b4c7ab113262929a05bcc"

def get_data(
    endpoint: str,
    route: str,
    api_key: str
) -> dict:
    
    url = f'{endpoint}/{route}&api_key={api_key}'
    
    response = requests.get(
        url = url
    )
    
    if response.status_code == 200:
        return response.json()["data"]
    
    else:
        raise Exception(f'Error Retrieving Data From {route}: {response.status_code}')