import pytest
from functions.fetch_data_postman import extract_curl_data  # Ajuste 'my_module' para o nome do módulo onde sua função está definida

def test_extract_curl_data_with_get_method(monkeypatch):
    curl_command = (
        "curl --location 'https://serverest.dev/produtos?vitor=nintendo&valor=300&id=1de3dg4t5h' "
        "--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IkFteTg0QGhvdG1haWwuY29tIiwicGFzc3dvcmQiOiJJTUlVQmpOU1hKSnN2RXMiLCJpYXQiOjE2OTMzNDkwNjcsImV4cCI6MTY5MzM0OTY2N30.B2Rc1H8iR0saTeY9FsX7bo2lDHla_frX0FR6Uz8AjLY' "
        "--header 'Content-Type: application/json'"
    )
    
    monkeypatch.setattr('builtins.input', lambda _: 'GET')
    
    method, url, body, headers = extract_curl_data(curl_command)
    
    expected_method = 'GET'
    expected_url = 'https://serverest.dev/produtos?vitor=nintendo&valor=300&id=1de3dg4t5h'
    expected_body = None
    expected_headers = (
        "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IkFteTg0QGhvdG1haWwuY29tIiwicGFzc3dvcmQiOiJJTUlVQmpOU1hKSnN2RXMiLCJpYXQiOjE2OTMzNDkwNjcsImV4cCI6MTY5MzM0OTY2N30.B2Rc1H8iR0saTeY9FsX7bo2lDHla_frX0FR6Uz8AjLY\nContent-Type: application/json"
    )
    
    assert method == expected_method
    assert url == expected_url
    assert body == expected_body
    assert headers == expected_headers

def test_extract_curl_data_with_post_method(monkeypatch):
    curl_command = (
        "curl 'https://serverest.dev/produtos' "
        "--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IkFteTg0QGhvdG1haWwuY29tIiwicGFzc3dvcmQiOiJJTUlVQmpOU1hKSnN2RXMiLCJpYXQiOjE2OTMzNDkwNjcsImV4cCI6MTY5MzM0OTY2N30.B2Rc1H8iR0saTeY9FsX7bo2lDHla_frX0FR6Uz8AjLY' "
        "--header 'Content-Type: application/json' "
        "--data '{\"nome\": \"Cheese IV\", \"preco\": 524}'"
    )
    
    monkeypatch.setattr('builtins.input', lambda _: 'POST')
    
    method, url, body, headers = extract_curl_data(curl_command)
    
    expected_method = 'POST'
    expected_url = 'https://serverest.dev/produtos'
    expected_body = {"nome": "Cheese IV", "preco": 524}
    expected_headers = (
        "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IkFteTg0QGhvdG1haWwuY29tIiwicGFzc3dvcmQiOiJJTUlVQmpOU1hKSnN2RXMiLCJpYXQiOjE2OTMzNDkwNjcsImV4cCI6MTY5MzM0OTY2N30.B2Rc1H8iR0saTeY9FsX7bo2lDHla_frX0FR6Uz8AjLY\nContent-Type: application/json"
    )
    
    assert method == expected_method
    assert url == expected_url
    assert body == expected_body
    assert headers == expected_headers
