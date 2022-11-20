import pytest
from source.main import main
import source.persistent as pers
from source.product import Product
from source.test.general_test import run, FILENAME, pers_empty, get_help

def test_A4(run, pers_empty, get_help):
    assert run('products_create tmt01 Tomatoes 21.2') == \
        "Tomatoes - €21.2 - Ref: tmt01"
        
def test_A5(run, pers_empty, get_help):
    assert run('products_create tmt01 Tomatoes') == \
        'Missing required arguments to command.\n' + get_help()
        
def test_A6(run, pers_product_create, get_help):
    assert run('products_show tmt01') == \
        "Tomatoes - €21 - Ref: tmt01"

def test_A7(run, pers_product_create, get_help):
    assert run('products_show') == \
        'Missing required arguments to command.\n' + get_help()

def test_A8(run, pers_product_create, get_help):
    assert run('products_show tmt02') == \
        "No product matches with this information."
        
def test_A9(run, pers_empty, get_help):
    assert run('products_create tmt01 Tomatoes price22') == \
        "Invalid data format."
        
def test_A10(run, pers_product_create, get_help):
    assert run('products_create tmt01 Tomatoes 22') == \
        "Impossible to register the product: duplicate reference."

def test_A11(run, pers_product_create, get_help):
    assert run('products_delete tmt01') == \
        ""

def test_A12(run, pers_product_create, get_help):
    assert run('products_delete tmt02') == \
        "No product matches with this information."
        
def test_A13(run, pers_product_create_mult, get_help):
    assert run('products_find Tomato') == \
        "Tomatoes - €21 - Ref: tmt01\nCherry Tomatoes - €42 - Ref: ctmt01"
        
def test_A14(run, pers_product_create_mult, get_help):
    assert run('products_find Apple') == \
        "No results."
        
def test_A15(run, pers_product_create_mult, get_help):
    assert run('products_edit tmt01 -p 120 -r tmt1 -n Tomata') == \
        "Tomata - €120 - Ref: tmt1"
        
def test_A16(run, pers_product_create_mult, get_help):
    assert run('products_edit appl01 -p 78') == \
        "No client matches with this information."

def test_A17(run, pers_empty, get_help):
    assert run('products_create !tmt Tomatoes 1') == \
        'Invalid data format.'

######## FIXTURES ########
@pytest.fixture
def pers_product_create(pers_empty):
    pers.load_from_save(FILENAME)
    product = Product.__new__(Product)
    product.ref = 'tmt01'
    product.name = 'Tomatoes'
    product.price = '21'
    pers.get_class_list(Product).append(product)
    pers.dump_to_save(FILENAME)

@pytest.fixture
def pers_product_create_mult(pers_empty):
    pers.load_from_save(FILENAME)
    product = Product.__new__(Product)
    product.ref = 'tmt01'
    product.name = 'Tomatoes'
    product.price = '21'
    pers.get_class_list(Product).append(product)
    
    product2 = Product.__new__(Product)
    product2.ref = 'ctmt01'
    product2.name = 'Cherry Tomatoes'
    product2.price = '42'
    pers.get_class_list(Product).append(product2)
    
    product3 = Product.__new__(Product)
    product3.ref = 'bnn01'
    product3.name = 'Banana'
    product3.price = '420'
    pers.get_class_list(Product).append(product3)
    pers.dump_to_save(FILENAME)