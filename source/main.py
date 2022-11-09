import sys
import io
from contextlib import redirect_stdout

from operations import OperationWrapper

def print_help():
    print('''
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

def process_args(args):
    arg_lst = args
    if arg_lst[0] == "help":
        print_help()
    elif arg_lst[0] == "clients_create":
        if len(arg_lst) == 3:
            OperationWrapper.clients_create(arg_lst[1], arg_lst[2], None)
        else:
            OperationWrapper.clients_create(arg_lst[1], arg_lst[2], arg_lst[3])

    elif arg_lst[0] == "clients_edit":
        new_name = new_email = new_phone = None
        id = arg_lst[1]
        arg_lst = arg_lst[2:]
        for i, arg in enumerate(arg_lst):
            if arg == '-n':
                new_name = arg_lst[i+1]
            elif arg == '-e':
                new_email = arg_lst[i+1]
            elif arg == '-p':
                if i == len(arg_lst)-1:
                    new_phone = ''
                else:
                    new_phone = arg_lst[i+1]

        OperationWrapper.clients_edit(id, new_name, new_email, new_phone)

    elif arg_lst[0] == "clients_delete":
        OperationWrapper.clients_delete(arg_lst[1])

    elif arg_lst[0] == "clients_show":
        OperationWrapper.clients_show(arg_lst[1])

    elif arg_lst[0] == "clients_getid":
        OperationWrapper.clients_getid(arg_lst[1])

    elif arg_lst[0] == "products_create":
        OperationWrapper.products_create(arg_lst[1], arg_lst[2], arg_lst[3])

    elif arg_lst[0] == "products_edit":
        new_name = new_ref = new_price = None
        ref = arg_lst[1]
        arg_lst = arg_lst[2:]
        for i, arg in enumerate(arg_lst):
            if arg == '-n':
                new_name = arg_lst[i+1]
            elif arg == '-r':
                new_ref = arg_lst[i+1]
            elif arg == '-p':
                new_price = arg_lst[i+1]

        OperationWrapper.products_edit(ref, new_ref, new_name, new_price)
    
    elif arg_lst[0] == "products_delete":
        OperationWrapper.products_delete(arg_lst[1])

    elif arg_lst[0] == "products_show":
        OperationWrapper.products_show(arg_lst[1])

    elif arg_lst[0] == "products_find":
        OperationWrapper.products_find(arg_lst[1])

    elif arg_lst[0] == "orders_add":
        OperationWrapper.orders_add(arg_lst[1], arg_lst[2], arg_lst[3], arg_lst[4])

    elif arg_lst[0] == "orders_show":
        OperationWrapper.orders_show(arg_lst[1], len(arg_lst) > 2 and arg_lst[2] == "--full")


def main(args):
    buf = io.StringIO() 
    with redirect_stdout(buf): 
        process_args(args)
    x = buf.getvalue()
    return x
    

if __name__ == '__main__':
    print(main(sys.argv[1:]))