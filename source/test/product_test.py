import pytest
from source.main import main
import source.persistent as pers
from source.product import Product
from source.test.general_test import run, FILENAME, pers_empty, get_help
from source.order import Order
from source.test.fixtures import pers_client_create, pers_client_create_mult, pers_product_create, pers_product_create_mult, pers_order_create

def test_A4(run, pers_empty, get_help):
    assert run(['products_create', 'tmt01', 'Tomatoes', '21.2']) == \
        "Tomatoes - €21.2 - Ref: tmt01"
        
def test_A5(run, pers_empty, get_help):
    assert run(['products_create', 'tmt01', 'Tomatoes']) == \
        'Missing required arguments to command.\n' + get_help()
        
def test_A6(run, pers_product_create, get_help):
    assert run(['products_show', 'tmt01']) == \
        "Tomatoes - €21 - Ref: tmt01"

def test_A7(run, pers_product_create, get_help):
    assert run(['products_show']) == \
        'Missing required arguments to command.\n' + get_help()

def test_A8(run, pers_product_create, get_help):
    assert run(['products_show', 'tmt02']) == \
        "No product matches with this information."
        
def test_A9(run, pers_empty, get_help):
    assert run(['products_create', 'tmt01', 'Tomatoes', 'price22']) == \
        "Invalid data format."
        
def test_A10(run, pers_product_create, get_help):
    assert run(['products_create', 'tmt01', 'Tomatoes', '22']) == \
        "Impossible to register the product: duplicate reference."

def test_A11(run, pers_product_create, get_help):
    assert run(['products_delete', 'tmt01']) == \
        ""

def test_A12(run, pers_product_create, get_help):
    assert run(['products_delete', 'tmt02']) == \
        "No product matches with this information."
        
def test_A13(run, pers_product_create_mult, get_help):
    assert run(['products_find', 'Tomato']) == \
        "Tomatoes - €21 - Ref: tmt01\nCherry Tomatoes - €42 - Ref: ctmt01"
        
def test_A14(run, pers_product_create_mult, get_help):
    assert run(['products_find', 'Apple']) == \
        "No results."
        
def test_A15(run, pers_product_create_mult, get_help):
    assert run(['products_edit', 'tmt01', '-p', '120', '-r', 'tmt1', '-n', 'Tomata']) == \
        "Tomata - €120 - Ref: tmt1"
        
def test_A16(run, pers_product_create_mult, get_help):
    assert run(['products_edit', 'appl01', '-p', '78']) == \
        "No client matches with this information."

def test_A17(run, pers_empty, get_help):
    assert run(['products_create', '!tmt', 'Tomatoes', '1']) == \
        'Invalid data format.'

def test_A25(run, pers_product_create_mult, get_help):
    assert run(['products_edit', 'tmt01', '-p', '120', '-r', 'ctmt01', '-n', 'Tomata']) == \
        "Impossible to register the product: duplicate reference."

def test_A26(run, pers_product_create_mult, get_help):
    assert run(['products_edit', 'tmt01']) == \
        "Tomatoes - €21 - Ref: tmt01"

def test_A27(run, pers_product_create_mult, get_help):
    assert run(['products_edit', 'tmt01', '-p', 'price']) == \
        "Invalid data format."
        
def test_A28(run, pers_order_create, get_help):
    assert run(['products_delete', 'tmt01']) == \
        ""
        
def test_A29(run, pers_order_create, get_help):
    assert run(['products_delete', 'ctmt01']) == \
        ""

def test_B25(run, pers_empty):
    assert run(['products_create', 'refMissing', 'Nothing', '']) == \
        "Invalid data format."