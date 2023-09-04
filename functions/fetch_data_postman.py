
import requests
import re

def fetch_request_data():

    request_name = "Listar_Usuarios"
   
    request_method = "GET"
    request_url = "https://serverest.dev/usuarios"
    test_script = """
    var resbody = JSON.parse(responseBody)

    var statusCode = 200
    var messageError = "error"

    pm.test("Status code is" + statusCode, function(){
        pm.response.to.have.status(statusCode)
    })

    pm.test.skip("Validate message error" , function(){
        pm.expect(resbody).property('message').to.be.contains(messageError)
    })
    
    """

    return request_name, request_method, request_url, test_script

def extract_curl_data(curl_command):
    # Extrai a URL usando uma expressão regular
    url_match = re.search(r'\'(https?://[^\']+)', curl_command)
    request_url = url_match.group(1) if url_match else None

    # Extrai o corpo da solicitação usando uma expressão regular
    body_match = re.search(r'--data \'([^\']+)\'', curl_command)
    request_body = body_match.group(1) if body_match else ""

    # Extrai os parâmetros da solicitação usando uma expressão regular
    params_match = re.search(r'--data-raw \'([^\']+)\'', curl_command)
    request_params = params_match.group(1) if params_match else ""

    # Solicita ao usuário o método HTTP em inglês
    while True:
        request_method = input("\nWhich HTTP method do you want to use (GET/POST/PUT/DELETE, etc.)? ").upper()

        # Verifica se o método é válido
        if request_method in ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"]:
            break
        else:
            print("\n-----Invalid HTTP method. Please choose a valid method (GET/POST/PUT/DELETE, etc.)-----\n")

    return request_method, request_url, request_body, request_params
