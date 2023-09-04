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
    return response.json()


def create_request(api_key, collection_name, collection_id, folder_name, folder_id, request_name, request_method, request_url, request_body=None, request_params=None, test_script=""):
    
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

    # Adiciona body se fornecido
    if request_body:
        request_item["request"]["body"] = {
            "mode": "raw",
            "raw": request_body
        }

    # Adiciona params se fornecidos
    if request_method == "GET" and request_params:
        request_item["request"]["url"]["query"] = request_params
    elif request_params:
        request_item["request"]["body"] = {
            "mode": "raw",
            "raw": request_params
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

    response = requests.put(url, headers=headers, data=json.dumps(data))
    return response.json()
