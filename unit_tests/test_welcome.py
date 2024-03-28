from unittest.mock import patch
from functions.welcome import lost_api_key, welcome, names, get_user_request_names, default_test


import os
import json
import pytest

# Fixture para configurar o ambiente antes dos testes
@pytest.fixture
def setup():
    # Criação do arquivo api_key.json para os testes
    config_dir = 'config'
    api_key_file = os.path.join(config_dir, 'api_key.json')
    api_key_data = {'api_key': 'test_api_key'}

    os.makedirs(config_dir, exist_ok=True)
    with open(api_key_file, 'w') as f:
        json.dump(api_key_data, f)

    yield

    # Limpeza após os testes
    os.remove(api_key_file)

def test_welcome_existing_api_key(setup, monkeypatch):
    # Simula a entrada do usuário
    monkeypatch.setattr('builtins.input', lambda _: None)

    # Executa a função welcome()
    api_key = welcome()

    # Verifica se a função retorna a chave API correta
    assert api_key == 'test_api_key'

def test_welcome_no_api_key(setup, monkeypatch):
    # Remove o arquivo api_key.json para simular a ausência da chave API
    os.remove('config/api_key.json')

    # Simula a entrada do usuário
    monkeypatch.setattr('builtins.input', lambda _: 'new_api_key')

    # Executa a função welcome()
    api_key = welcome()

    # Verifica se a função solicita corretamente a entrada da chave API e a salva no arquivo
    assert api_key == 'new_api_key'
    with open('config/api_key.json') as f:
        data = json.load(f)
        assert data['api_key'] == 'new_api_key'

def test_names():
    collection_name, folder_name = names("Test Collection", "Test Folder")

    assert collection_name == "Test Collection"
    assert folder_name == "Test Folder"

def test_default_test():
    # Execute a função default_test()
    default_test()

    # Verifique se os arquivos foram criados corretamente
    assert os.path.exists("config/tests/body/nonexistent")
    assert os.path.exists("config/tests/body/empty")
    assert os.path.exists("config/tests/body/null")
    assert os.path.exists("config/tests/body/size")
    assert os.path.exists("config/tests/body/invalid")


def test_get_user_request_names(mocker):
    # Simule a abertura do arquivo com conteúdo simulado
    mocker.patch("builtins.open", mocker.mock_open(read_data="Request1,Request2,Request3"))

    expected_names = ["Request1", "Request2", "Request3"]
    result = get_user_request_names()
    
    assert result == expected_names  # Verifique a lista inteira
    assert result[0] == expected_names[0]  # Verifique o primeiro elemento
    assert result[1] == expected_names[1]  # Verifique o segundo elemento
    assert result[2] == expected_names[2]  # Verifique o terceiro elemento

@patch('builtins.open', create=True)

def test_api_key_exists(mock_open):
    mock_open.return_value.__enter__.return_value.read.return_value = '{"api_key": "test_api_key"}'
    assert lost_api_key() == 'test_api_key'
