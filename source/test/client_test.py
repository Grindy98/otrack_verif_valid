import pytest
import re

from source.main import main
import source.persistent as pers
from source.client import Client
from source.test.general_test import run, FILENAME, pers_empty, get_help

def test_B1(run, pers_empty, get_help):
    assert run('clients_create') == \
        'Missing required arguments to command.\n' + get_help()

def test_B2(run, pers_empty):
    assert re.fullmatch(r'John Smith - john.smith@email.com - Id: \d+\n',
        run('clients_create "John Smith" john_smith@email.org'))

def test_B3(run, pers_empty):
    assert re.fullmatch(r'John Smith - john.smith@email.com - 768387991 - Id: \d+\n',
        run('clients_create "John Smith" john_smith@email.org 768387991'))

def test_B4(run, pers_empty):
    assert run('clients_create "John Smith" john_smith.com 768387991') == \
        'Invalid data format.'

def test_B5(run, pers_empty):
    assert run('clients_create "John Smith" john_smith@email.org +34678987678') == \
        'Invalid data format.'

######## FIXTURES ########
@pytest.fixture
def pers_client_create(pers_empty):
    pers.load_from_save(FILENAME)
    client = Client.__new__(Client)
    client.name = 'Jane Doe'
    client.email = 'jane.doe@hotmail.com'
    client.phone = '674328876'
    pers.get_class_list(Client).append(client)
    pers.dump_to_save(FILENAME)