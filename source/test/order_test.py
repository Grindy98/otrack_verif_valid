import pytest
from source.main import main
import source.persistent as pers
from source.order import Order
from source.test.general_test import pers_empty, run, FILENAME, get_help
from source.test.client_test import pers_client_create_mult
from source.test.product_test import pers_product_create_mult


def test_B23(run, pers_product_create_mult, pers_client_create_mult):
    assert run(['orders_add', 1, 'bnn01', 3, '21/11/1999']) == \
        ''
        
def test_A18(run, pers_product_create_mult, pers_client_create_mult):
    assert run(['orders_add', 100, 'ctmt01', 3, '21/11/1999']) == \
        "No client matches with this information."
        
def test_A19(run, pers_product_create_mult, pers_client_create_mult):
    assert run(['orders_add', 1, 'axolotl', 70, '21/11/1999']) == \
        "No product matches with this information."
        
def test_A20(run, pers_product_create_mult, pers_client_create_mult):
    assert run(['orders_add', 1, 'ctmt01', -1, '21/11/1999']) == \
        "Invalid data format."
        
def test_A21(run, pers_product_create_mult, pers_client_create_mult):
    assert run(['orders_add', 1, 'ctmt01', 3, '21-11-1999']) == \
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

######## FIXTURES ########
@pytest.fixture
def pers_order_create(pers_product_create_mult, pers_client_create_mult):
    pers.load_from_save(FILENAME)
    order = Order.__new__(Order)
    order.client_id = 1
    order.product_ref = 'tmt01'
    order.date = '21/11/1999'
    order.amount = 1
    pers.get_class_list(Order).append(order)
    
    order2 = Order.__new__(Order)
    order2.client_id = 2
    order2.product_ref = 'ctmt01'
    order2.date = '21/11/1999'
    order2.amount = 7
    pers.get_class_list(Order).append(order2)
    pers.dump_to_save(FILENAME)