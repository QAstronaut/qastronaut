from unittest.mock import patch
from functions.welcome import lost_api_key, welcome, names, get_user_request_names, default_test_body, default_test_get


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


def test_names(mocker):
    # Simule a entrada do usuário com valores de teste
    mocker.patch('builtins.input', side_effect=['Test Collection', 'Test Folder'])
    
    collection_name, folder_name = names()
    
    assert collection_name == 'Test Collection'
    assert folder_name == 'Test Folder'

def test_default_test_body():
    # Execute a função default_test()
    default_test_body()

    # Verifique se os arquivos foram criados corretamente
    assert os.path.exists("config/tests/body/nonexistent")
    assert os.path.exists("config/tests/body/empty")
    assert os.path.exists("config/tests/body/null")
    assert os.path.exists("config/tests/body/size")
    assert os.path.exists("config/tests/body/invalid")

def test_default_test_get():
    # Execute a função default_test()
    default_test_get()

    # Verifique se os arquivos foram criados corretamente
    assert os.path.exists("config/tests/params/nonexistent")
    assert os.path.exists("config/tests/params/empty")
    assert os.path.exists("config/tests/params/null")
    assert os.path.exists("config/tests/params/size")
    assert os.path.exists("config/tests/params/invalid")


def test_get_user_request_names():
    # Simule a abertura do arquivo com conteúdo simulado
    with patch("builtins.open", mock_open(read_data="Request1\nRequest2\nRequest3\n")) as mock_file:
        assert get_user_request_names() == ['Request1', 'Request2', 'Request3']

@patch('builtins.open', create=True)

def test_api_key_exists(mock_open):
    mock_open.return_value.__enter__.return_value.read.return_value = '{"api_key": "test_api_key"}'
    assert lost_api_key() == 'test_api_key'
