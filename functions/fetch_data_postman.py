import re
import json

def extract_curl_data(curl_command):

    # Extrai a URL usando uma expressão regular
    url_match = re.search(r"curl\s+(?:--location\s+)?['\"]?([^'\"]+)['\"]?", curl_command)
    request_url = url_match.group(1) if url_match else None

    # Combinação de padrões para '--data' ou '--data-raw'
    body_match = re.search(r'--data(?:-raw)? \'([^\']+)\'', curl_command)
    request_body_raw = body_match.group(1) if body_match else ""

    # Verifica se há um corpo de solicitação antes de tentar analisá-lo
    if request_body_raw:
        # Substitua as aspas simples por aspas duplas para tornar o JSON válido
        request_body_json = request_body_raw.replace("'", '"')
        try:
            request_body = json.loads(request_body_json)
        except json.JSONDecodeError as e:
            print("\nError parsing request body JSON:", e)
            request_body = None
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