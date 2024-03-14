import pytest
import requests
import sys
import os

# Adicione o diretório contendo os módulos ao sys.path
module_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'functions'))
sys.path.insert(0, module_dir)

from functions.create_postman import create_collection, create_folder, create_request, create_test_empty, create_test_invalid, create_test_lenght, create_test_nonexistent, create_test_null


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

@pytest.fixture
def mock_create_request(monkeypatch):
    def mock_request(*args, **kwargs):
        class MockResponse:
            def __init__(self, status_code, json_data):
                self.status_code = status_code
                self.json_data = json_data

            def json(self):
                return self.json_data

        # Customize this part to return the desired mock response based on the arguments
        return MockResponse(200, {"data": {"id": "mock_request_id"}})

    monkeypatch.setattr("create_postman.create_request", mock_request)

API_KEY = "PMAK-6502182664892529ac886db6-cba14f4d518e37dc849306d096060cd0da"
COLLECTION_NAME = "TestCollection"
FOLDER_NAME = "TestFolder"
REQUEST_NAMES = "TestRequest"
REQUEST_METHOD = "POST"
REQUEST_HEADERS = {"Content-Type": "application/json"}
REQUEST_BODY = {"key": "value"}
REQUEST_URL = "https://example.com/api"
TEST_SCRIPT = "pm.test('Status code is 200', function () { pm.response.to.have.status(200); });"
COLLECTION_ID = "your_collection_id"
FOLDER_ID = "your_folder_id"


@pytest.mark.scripted_test
def test_create_collection():
    collection_id = create_collection(API_KEY, COLLECTION_NAME)
    assert collection_id is not None

@pytest.mark.scripted_test
def test_create_folder():
    collection_id = create_collection(API_KEY, COLLECTION_NAME)
    folder_id = create_folder(collection_id, FOLDER_NAME, API_KEY)
    assert folder_id is not None


# Testes para create_request
def test_create_request():
    collection_id = "mock_collection_id"
    folder_id = "mock_folder_id"
    request_name = "Test Request"
    request_method = "POST"
    request_headers = {"Content-Type": "application/json"}
    request_body = {"key": "value"}
    request_url = "https://example.com"
    test_script = "console.log('Test script');"
    api_key = "PMAK-6502182664892529ac886db6-cba14f4d518e37dc849306d096060cd0da"
    response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
    assert response.status_code == 200

def test_create_test_empty(mock_create_request):
    request_id = create_test_empty(API_KEY, COLLECTION_ID, FOLDER_ID, REQUEST_NAMES, REQUEST_METHOD, REQUEST_HEADERS, REQUEST_BODY, REQUEST_URL)
    assert request_id is not None

def test_create_test_null(mock_create_request):
    request_id = create_test_null(API_KEY, COLLECTION_ID, FOLDER_ID, REQUEST_NAMES, REQUEST_METHOD, REQUEST_HEADERS, REQUEST_BODY, REQUEST_URL)
    assert request_id is not None

def test_create_test_nonexistent(mock_create_request):
    request_id = create_test_nonexistent(API_KEY, COLLECTION_ID, FOLDER_ID, REQUEST_NAMES, REQUEST_METHOD, REQUEST_HEADERS, REQUEST_BODY, REQUEST_URL)
    assert request_id is not None

def test_create_test_invalid(mock_create_request):
    request_id = create_test_invalid(API_KEY, COLLECTION_ID, FOLDER_ID, REQUEST_NAMES, REQUEST_METHOD, REQUEST_HEADERS, REQUEST_BODY, REQUEST_URL)
    assert request_id is not None

def test_create_test_length(mock_create_request):
    request_id = create_test_lenght(API_KEY, COLLECTION_ID, FOLDER_ID, REQUEST_NAMES, REQUEST_METHOD, REQUEST_HEADERS, REQUEST_BODY, REQUEST_URL)
    assert request_id is not None

# Execute os testes usando o comando pytest

