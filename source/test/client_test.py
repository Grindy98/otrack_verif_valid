import pytest
from source.main import main
import source.persistent as pers
from source.client import Client
from source.test.general_test import run, FILENAME

# def test_TC1(run, pers_client):
#     assert run('clients_create') == \
#         'Missing required arguments to command.\n'


######## FIXTURES ########
@pytest.fixture
def pers_empty():
    pers._state_dict = {}
    pers.dump_to_save(FILENAME)
    
@pytest.fixture
def pers_client(pers_empty):
    pers.load_from_save(FILENAME)
    client = Client.__new__(Client)
    client.name = 'afawfwa'
    client.email = '1@2'
    client.phone = '12312'
    pers.get_class_list(Client).append(client)
    pers.dump_to_save(FILENAME)