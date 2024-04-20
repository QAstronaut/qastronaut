import os
from functions.fetch_data_postman import extract_curl_data

def test_extract_curl_data():
    with open('config/requests/curl.txt', 'r') as file:
        curl_command = file.read()

    expected_method = 'POST'
    expected_url = 'https://serverest.dev/produtos'
    expected_body = {
        "nome": "Cheese IV",
        "preco": 524,
        "descricao": "Produto",
        "detalhes": {
            "peso": "100g",
            "fabricante": "Empresa XYZ"
        },
        "imagens": [
            "imagem1.jpg",
            "imagem2.jpg"
        ]
    }
    expected_headers = "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IkFteTg0QGhvdG1haWwuY29tIiwicGFzc3dvcmQiOiJJTUlVQmpOU1hKSnN2RXMiLCJpYXQiOjE2OTMzNDkwNjcsImV4cCI6MTY5MzM0OTY2N30.B2Rc1H8iR0saTeY9FsX7bo2lDHla_frX0FR6Uz8AjLY\nContent-Type: application/json"

    method, url, body, headers = extract_curl_data(curl_command)

    assert method == expected_method
    assert url == expected_url
    assert body == expected_body
    assert headers == expected_headers

