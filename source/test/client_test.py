import pytest
import re

from source.main import main
import source.persistent as pers
from source.client import Client
from source.test.general_test import run, FILENAME, pers_empty, get_help
from source.order import Order
from source.test.fixtures import pers_product_create, pers_product_create_mult, pers_client_create, pers_client_create_mult, pers_order_create

def test_B1(run, pers_empty, get_help):
    assert run(['clients_create']) == \
        'Missing required arguments to command.\n' + get_help()

def test_B2(run, pers_empty):
    outp = run(['clients_create', 'John Smith', 'john_smith@email.com'])
    assert re.match(r'John Smith - john_smith@email.com - Id: 1',
        outp), outp

def test_B3(run, pers_empty):
    outp = run(['clients_create', 'John Smith', 'john_smith@email.com', '768387991'])
    assert re.match(r'John Smith - john_smith@email.com - 768387991 - Id: \d+',
        outp), outp

def test_B4(run, pers_empty):
    assert run(['clients_create', 'John Smith', 'john_smith.com', '768387991']) == \
        'Invalid data format.'

def test_B5(run, pers_empty):
    assert run(['clients_create', 'John Smith', 'john_smith@email.org', '+34678987678']) == \
        'Invalid data format.'

def test_B6(run, pers_client_create):
    assert run(['clients_create', 'Jane Doe', 'jane.doe@hotmail.com', '34678987678']) == \
        'This email is already used, please choose another one.'

def test_B7(run, pers_empty):
    assert run(['clients_edit', '1', '-n', 'Jane Marcus']) == \
        'No client matches with this information.'

def test_B8(run, pers_client_create):
    assert run(['clients_edit', '1', '-n', 'Jane Marcus']) == \
        'Jane Marcus - jane.doe@hotmail.com - 674328876 - Id: 1'

def test_B9(run, pers_client_create):
    assert run(['clients_edit', '1', '-e', 'janed@gmail.com', '-p', '']) == \
        'Jane Doe - janed@gmail.com - Id: 1'

def test_B10(run, pers_client_create):
    assert run(['clients_edit', '1', '-p', '876']) == \
        'Jane Doe - jane.doe@hotmail.com - 876 - Id: 1'

def test_B11(run, pers_client_create):
    assert run(['clients_edit', '1', '-e', 'not_email', '-p']) == \
        'Invalid data format.'

def test_B12(run, pers_client_create, get_help):
    assert run(['clients_edit']) == \
        'Missing required arguments to command.\n' + get_help()

def test_B13(run, pers_empty):
    assert run(['clients_edit', 'i']) == \
        'No client matches with this information.'

def test_B14(run, pers_client_create_mult):
    assert run(['clients_edit', '1', '-e', 'jackson@hotmail.com']) == \
        'This email is already used, please choose another one.'

def test_B15(run, pers_empty):
    assert run(['clients_delete', 'i']) == \
        'No client matches with this information.'

def test_B16(run, pers_empty):
    assert run(['clients_delete', '1']) == \
        'No client matches with this information.'

def test_B17(run, pers_client_create):
    assert run(['clients_delete', '1']) == \
        ''

def test_B18(run, pers_client_create):
    assert run(['clients_show', '1']) == \
        'Jane Doe - jane.doe@hotmail.com - 674328876 - Id: 1'
    
def test_B19(run, pers_client_create):
    assert run(['clients_show', 'i']) == \
        'No client matches with this information.'

def test_B20(run, pers_empty):
    assert run(['clients_show', '1']) == \
        'No client matches with this information.'

def test_B21(run, pers_empty):
    assert run(['clients_getid', 'a']) == \
        'No client matches with this information.'

def test_B22(run, pers_client_create):
    assert run(['clients_getid', 'jane.doe@hotmail.com']) == \
        '1'
        
def test_A30(run, pers_order_create, get_help):
    assert run(['clients_delete', '1']) == \
        ""
        
def test_A31(run, pers_order_create, get_help):
    assert run(['clients_delete', '2']) == \
        ""
