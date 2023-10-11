import re
import json

def extract_curl_data(curl_command):
    # Extrai a URL usando uma expressão regular
    url_match = re.search(r'\'(https?://[^\']+)', curl_command)
    request_url = url_match.group(1) if url_match else None

    # Extrai o corpo da solicitação usando uma expressão regular
    body_match = re.search(r'--data \'([^\']+)\'', curl_command)
    request_body = body_match.group(1) if body_match else ""

    # Verifica se há um corpo de solicitação antes de tentar analisá-lo
    if request_body:
        request_body = json.loads(request_body)
    else:
        request_body = None

    # Extrai os parâmetros do header usando uma expressão regular
    headers_match = re.findall(r'--header \'([^\']+)\'', curl_command)
    request_headers = '\n'.join(headers_match) if headers_match else ''

    # Solicita ao usuário o método HTTP em inglês
    while True:
        request_method = input("\nWhich HTTP method do you want to use (GET/POST/PUT/DELETE, etc.)? ").upper().strip()

        # Verifica se o método é válido
        if request_method in ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"]:
            break
        else:
            print("\n-----Invalid HTTP method. Please choose a valid method (GET/POST/PUT/DELETE, etc.)-----\n")

    return request_method, request_url, request_body, request_headers