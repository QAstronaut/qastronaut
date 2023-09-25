import requests
import json

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
        print(f"\nCollection '{collection_name}' created successfully!")
    else:
        print(f"\nFailed to create collection '{collection_name}'. Status code: {response.status_code}")

    return response.json()


def create_folder(api_key, collection_id, folder_name, collection_name):

    url = f"https://api.getpostman.com/collections/{collection_id}"

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
            "item": [
                {
                    "name": folder_name,
                    "item": []
                }
            ]
        }
    }

    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"Folder '{folder_name}' created successfully!\n")
    else:
        print(f"Failed to create folder '{folder_name}'. Status code: {response.status_code}\n")

    return response.json()
    
   
def create_request(api_key, collection_name, collection_id, folder_name, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script):

    url = f"https://api.getpostman.com/collections/{collection_id}"

    headers = {
        "X-Api-Key": api_key,
        "Content-Type": "application/json"
    }

    request_item = {
        "name": request_name,
        "request": {
            "url": request_url,
            "method": request_method,
            "header": request_headers,
        },
        "event": [
            {
                "listen": "test",
                "script": {
                    "type": "text/javascript",
                    "exec": [test_script]
                }
            }
        ]
    }

    if request_body is not None:
        request_item["request"]["body"] = {
            "mode": "raw",
            "raw": json.dumps(request_body, indent=2)
        }

    data = {
        "collection": {
            "info": {
                "name": collection_name,
                "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
            },
            "item": [
                {
                    "id": folder_id,
                    "name": folder_name,
                    "item": [request_item]
                }
            ]
        }
    }

    response = requests.put(url, headers=headers, json=data)
    return response.json()
