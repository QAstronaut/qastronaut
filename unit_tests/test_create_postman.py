import pytest
import requests
from functions.create_postman import create_collection, create_folder, create_request

# Mocking requests.post para evitar chamadas de rede durante os testes.
def mock_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, status_code, json_data):
            self.status_code = status_code
            self.json_data = json_data

        def json(self):
            return self.json_data

    if args[0] == "https://api.getpostman.com/collections":
        return MockResponse(200, {"collection": {"uid": "mock_collection_id"}})
    elif args[0].startswith("https://api.getpostman.com/collections/"):
        return MockResponse(200, {"data": {"id": "mock_folder_id"}})
    elif args[0].startswith("https://api.getpostman.com/collections/mock_collection_id/requests?folder=mock_folder_id"):
        return MockResponse(200, {"data": {"id": "mock_request_id"}})
    else:
        return MockResponse(500, {})

requests.post = mock_post

# Testes para create_collection
def test_create_collection():
    api_key = "your_api_key"
    collection_name = "Test Collection"
    collection_id = create_collection(api_key, collection_name)
    assert collection_id == "mock_collection_id"

# Testes para create_folder
def test_create_folder():
    collection_id = "mock_collection_id"
    folder_name = "Test Folder"
    api_key = "your_api_key"
    folder_id = create_folder(collection_id, folder_name, api_key)
    assert folder_id == "mock_folder_id"

# Testes para create_request
def test_create_request():
    collection_id = "mock_collection_id"
    folder_id = "mock_folder_id"
    request_name = "Test Request"
    request_method = "GET"
    request_headers = {"Content-Type": "application/json"}
    request_body = {"key": "value"}
    request_url = "https://example.com"
    test_script = "console.log('Test script');"
    api_key = "your_api_key"
    response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
    assert response.status_code == 200

# Execute os testes com pytest
if __name__ == "__main__":
    pytest.main()
