import requests
import json
import copy
import simplejson as json
from decimal import Decimal

def create_collection(api_key, collection_name):
    url = "https://api.getpostman.com/collections"

    headers = {
        "X-Api-Key": api_key,
        "Content-Type": "application/json"
    }

    data = {
        "collection": {
            "info": {
                "name": collection_name,
                "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
            },
            "item": []
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        collection_data = response.json()
        collection_id = collection_data.get('collection', {}).get('uid')
        if collection_id:
            print(f"\nCollection '{collection_name}' created successfully with collection_id: {collection_id}")
            return collection_id
        else:
            print(f"\nCollection '{collection_name}' created, but collection_id not found in the response.")
    else:
        print(f"\nFailed to create collection '{collection_name}'. Status code: {response.status_code}")

    return None


def create_folder(collection_id, folder_name, api_key):

    url = f'https://api.getpostman.com/collections/{collection_id}/folders'
    
    headers = {
        'Content-Type': 'application/json',
        'X-API-Key': api_key
    }

    data = {
        'name': folder_name
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        folder_data = response.json()
        folder_id = folder_data.get('data', {}).get('id')
        if folder_id:
            print(f"\nFolder '{folder_name}' created successfully with folder_id: {folder_id}")
            return folder_id
        else:
            print(f"\nFolder '{folder_name}' created, but folder_id not found in the response.")
    else:
        print(f"\nFailed to create collection '{folder_name}'. Status code: {response.status_code}")
    return None

def create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script):
    
    url = f'https://api.getpostman.com/collections/{collection_id}/requests?folder={folder_id}'

    headers = {
        'Content-Type': 'application/json',
        'X-API-Key': api_key
    }
    if request_body is None:
                data = {
            "name": request_name,
            "url": request_url,
            "method": request_method,
            "headers": request_headers,
            "dataMode": "none",
            "events": [
                {
                    "listen": "test",
                    "script": {
                        "id": "a8608e1a-ce4b-4129-8c89-930d26ae0f6a",
                        "exec": [test_script],
                        "type": "text/javascript"
                    }
                }
            ]
        }
    else:
        data = {
            "name": request_name,
            "url": request_url,
            "method": request_method,
            "headers": request_headers,
            "dataMode": "raw",
            "rawModeData": json.dumps(request_body, indent=2),
            "dataOptions": {
                "raw": {
                    "language": "json"
                }
            },
            "events": [
                {
                    "listen": "test",
                    "script": {
                        "id": "a8608e1a-ce4b-4129-8c89-930d26ae0f6a",
                        "exec": [test_script],
                        "type": "text/javascript"
                    }
                }
            ]
        }
    
    response = requests.post(url, headers=headers, json=data)
    print(response)
    return response