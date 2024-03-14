from functions.welcome import welcome, names, get_user_request_names



def test_welcome(monkeypatch):
    # Simule a entrada do usuário
    input_values = ["YourAPIKey"]
    input_mock = lambda _: input_values.pop(0)
    
    # Simule o KeyboardInterrupt para evitar a execução infinita do teste
    monkeypatch.setattr('builtins.input', input_mock)
    monkeypatch.setattr('sys.exit', lambda x: None)  # Simule o sys.exit
    
    api_key = welcome()

    # Verifique se a função retorna a chave API corretamente
    assert api_key == "PMAK-6502182664892529ac886db6-cba14f4d518e37dc849306d096060cd0da"

# Teste para a função names
def test_names(capsys):
    collection_name, folder_name = names("TestCollection", "TestFolder")
    assert collection_name == "TestCollection"
    assert folder_name == "TestFolder"

#OBS.: Por se tratar de um input, o teste da func test_names dará um erro, a menos que alteremos o input por um valor fixo. Parte do código alterada:
'''def names(collection_name, folder_name):
    return collection_name, folder_name'''


# Teste para a função get_user_request_names
def test_get_user_request_names(mocker):
    # Simule a abertura do arquivo com conteúdo simulado
    mocker.patch("builtins.open", mocker.mock_open(read_data="Request1,Request2,Request3"))

    expected_names = ["Request1", "Request2", "Request3"]
    result = get_user_request_names()
    
    assert result == expected_names  # Verifique a lista inteira
    assert result[0] == expected_names[0]  # Verifique o primeiro elemento
    assert result[1] == expected_names[1]  # Verifique o segundo elemento
    assert result[2] == expected_names[2]  # Verifique o terceiro elemento

#OBS.: Por se tratar de uma leitura de arquivo com uma lista, o teste da func test_get_user_requests_names dará um erro, a menos que alteremos o módulo pelo seguinte código:
'''def get_user_request_names():
    user_request_names = []

    try:
        with open(name_file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(',')
                for part in parts:
                    if part:
                        user_request_names.append(part)
    except FileNotFoundError:
        print("\nThe 'user_requests' file was not found. Please create the file and add request names.")
        exit()

    return user_request_names'''

