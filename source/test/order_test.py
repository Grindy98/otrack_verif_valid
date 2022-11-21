import pytest
from source.main import main
import source.persistent as pers
from source.order import Order
from source.test.general_test import pers_empty, run, FILENAME, get_help
from source.test.fixtures import pers_client_create_mult, pers_product_create_mult, pers_order_create


def test_B23(run, pers_product_create_mult, pers_client_create_mult):
    assert run(['orders_add', '1', 'bnn01', '3', '21/11/1999']) == \
        ''
        
def test_A18(run, pers_product_create_mult, pers_client_create_mult):
    assert run(['orders_add', '100', 'ctmt01', '3', '21/11/1999']) == \
        "No client matches with this information."
        
def test_A19(run, pers_product_create_mult, pers_client_create_mult):
    assert run(['orders_add', '1', 'axolotl', '70', '21/11/1999']) == \
        "No product matches with this information."
        
def test_A20(run, pers_product_create_mult, pers_client_create_mult):
    assert run(['orders_add', '1', 'ctmt01', '-1', '21/11/1999']) == \
        "Invalid data format."
        
def test_A21(run, pers_product_create_mult, pers_client_create_mult):
    assert run(['orders_add', '1', 'ctmt01', '3', '21-11-1999']) == \
        "Invalid data format."
        
def test_A22(run, pers_order_create):
    assert run(['orders_show', '21/11/1999']) == \
        "Orders for the 21/11/1999:\ntmt01 - 1\nctmt01 - 7"
        
def test_A23(run, pers_order_create):
    assert run(['orders_show', '21..11/1999']) == \
        "Invalid data format."

def test_A24(run, pers_order_create):
    assert run(['orders_show', '21/11/1999', '--full']) == \
        "Orders for the 21/11/1999:\ntmt01 - 1\n\tClient 1 - Jane Doe - 1\nctmt01 - 7\n\tClient 2 - Jackson - 7"