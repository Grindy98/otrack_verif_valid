import pytest
from source.main import main
import source.persistent as pers
from source.client import Client

FILENAME = 'persistant_state_test.pkl'

def test_TC1(run, get_help, pers_client):
    assert run('clients_create') == \
        'Missing required arguments to command.\n' + get_help()


######## FIXTURES ########
# Empty fixture, client fixture
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

@pytest.fixture
def run():
    def wrapper(argstring):
        return main(argstring.split(), FILENAME).strip()
    return wrapper

@pytest.fixture
def get_help():
    def wrapper():
        return ('''
otrack help - Displays the following list of commands.

otrack clients_create fullname email [phone] - Creates a client and prints it
with the client id. Email must contain an '@', and the phone field should be only digits (see
Error 2 otherwise).

otrack clients_edit client_id [-n fullname] [-e email] [-p phone] -
Allows editing of a client (option -n to edit the name, option -p to edit the phone and option -e
to edit the email). Prints the new client after modification. Email must contain an '@', and the
phone field should be only digits (see Error 2 otherwise). If no client has the specified ID, an
error is triggered (see Error 3).

otrack clients_delete client_id - Deletes a client. If no client has the specified ID,
an error is triggered (see Error 3).

otrack clients_show client_id - Prints the specified client's information details. If no
client has the specified ID, an error is triggered (see Error 3).

otrack clients_getid client_email - Prints the unique number of the client
associated with the specified email. If no client has the specified email, an error is triggered
(see Error 3).

otrack products_create ref name price - Creates a product and prints it. Product
references can be any combination of alphanumeric characters. Price is a number potentially
with decimals (see Error 2 otherwise). Reference should be unique in the system (see Error
5).

otrack products_edit product_ref [-r ref] [-n name] [-p price] - Allows
editing the product (option -n to edit the name and option price). Prints the new product after
modification. Product data (ref, price) should meet the same format requirements as the
products_create command. If no product has the specified reference, an error is
triggered (see Error 3).

otrack products_delete product_ref - Deletes a product. If no product has the
specified reference, an error is triggered (see Error 4).

otrack products_show product_ref - Prints the specified product’s information
details. If no product has the specified reference, an error is triggered (see Error 4).

otrack products_find query_string - Prints the list of all products whose name
match (fully or partially) the query string, and print their names, unique reference and price. If
no products are found, the following message is displayed: “No results.”.

otrack orders_add client_id product_ref amount dd/mm/yyyy - Allows a
user to place the order of a client, for a specified amount of a product, for a specific date. If
no client has the specified client_id, Error 3 is triggered. If no product has the specified
product_ref, Error 4 is triggered. The amount field should be a positive non-zero integer, and
the date should follow this format: “dd/mm/yyyy” (see Error 2 otherwise).

otrack orders_show dd/mm/yyyy [--full] - Prints all the orders for a specific day.
The date field should follow this format: “dd/mm/yyyy” (see Error 2 otherwise). Adding the
--full option prints detailed information, including the names of the clients who ordered
each product.''')
    return wrapper