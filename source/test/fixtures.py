import pytest

from source.product import Product
from source.client import Client
from source.order import Order
import source.persistent as pers

from source.test.general_test import get_help, FILENAME, pers_empty

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
    
@pytest.fixture
def pers_client_create_mult(pers_empty):
    pers.load_from_save(FILENAME)
    client = Client.__new__(Client)
    client.name = 'Jane Doe'
    client.email = 'jane.doe@hotmail.com'
    client.phone = '674328876'
    client.id = 1
    pers.get_class_list(Client).append(client)

    client = Client.__new__(Client)
    client.name = 'Jackson'
    client.email = 'jackson@hotmail.com'
    client.phone = ''
    client.id = 2
    pers.get_class_list(Client).append(client)

    pers.dump_to_save(FILENAME)

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
    order2.date = '21/11/2025'
    order2.amount = 7
    pers.get_class_list(Order).append(order2)
    
    order2 = Order.__new__(Order)
    order2.client_id = 2
    order2.product_ref = 'ctmt01'
    order2.date = '21/11/1999'
    order2.amount = 7
    pers.get_class_list(Order).append(order2)
    pers.dump_to_save(FILENAME)
    
    
@pytest.fixture
def pers_client_create(pers_empty):
    pers.load_from_save(FILENAME)
    client = Client.__new__(Client)
    client.name = 'Jane Doe'
    client.email = 'jane.doe@hotmail.com'
    client.phone = '674328876'
    client.id = 1
    pers.get_class_list(Client).append(client)
    pers.dump_to_save(FILENAME)