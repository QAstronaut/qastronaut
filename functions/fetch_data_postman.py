
import requests

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