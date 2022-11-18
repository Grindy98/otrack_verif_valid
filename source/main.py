import sys
import io
from contextlib import redirect_stdout

import source.exceptions as excs
from source.operations import OperationWrapper

def get_help():
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

def process_args(args):
    
    if not args:
        # Missing an operational arg
        raise excs.Error1

    if args[0] == "help":
        print(get_help())
    elif args[0] == "clients_create":
        if len(args) < 3:
            # Missing necessary args
            raise excs.Error1
        elif len(args) == 3:
            OperationWrapper.clients_create(args[1], args[2], None)
        else:
            OperationWrapper.clients_create(args[1], args[2], args[3])

    elif args[0] == "clients_edit":
        if len(args) < 2:
            # Missing id
            raise excs.Error1
        new_name = new_email = new_phone = None
        id = args[1]
        args = args[2:]
        for i, arg in enumerate(args):
            if arg == '-n':
                new_name = args[i+1]
            elif arg == '-e':
                new_email = args[i+1]
            elif arg == '-p':
                if i == len(args)-1:
                    new_phone = ''
                else:
                    new_phone = args[i+1]

        OperationWrapper.clients_edit(id, new_name, new_email, new_phone)

    elif args[0] == "clients_delete":
        if len(args) < 2:
            # Missing id
            raise excs.Error1
        OperationWrapper.clients_delete(args[1])

    elif args[0] == "clients_show":
        if len(args) < 2:
            # Missing id
            raise excs.Error1
        OperationWrapper.clients_show(args[1])

    elif args[0] == "clients_getid":
        if len(args) < 2:
            # Missing email
            raise excs.Error1
        OperationWrapper.clients_getid(args[1])

    elif args[0] == "products_create":
        if len(args) < 4:
            # Missing necessary args
            raise excs.Error1
        OperationWrapper.products_create(args[1], args[2], args[3])

    elif args[0] == "products_edit":
        if len(args) < 2:
            # Missing ref
            raise excs.Error1
        new_name = new_ref = new_price = None
        ref = args[1]
        args = args[2:]
        for i, arg in enumerate(args):
            if arg == '-n':
                new_name = args[i+1]
            elif arg == '-r':
                new_ref = args[i+1]
            elif arg == '-p':
                new_price = args[i+1]

        OperationWrapper.products_edit(ref, new_ref, new_name, new_price)
    
    elif args[0] == "products_delete":
        if len(args) < 2:
            # Missing ref
            raise excs.Error1
        OperationWrapper.products_delete(args[1])

    elif args[0] == "products_show":
        if len(args) < 2:
            # Missing ref
            raise excs.Error1
        OperationWrapper.products_show(args[1])

    elif args[0] == "products_find":
        if len(args) < 2:
            # Missing query string
            raise excs.Error1
        OperationWrapper.products_find(args[1])

    elif args[0] == "orders_add":
        OperationWrapper.orders_add(args[1], args[2], args[3], args[4])

    elif args[0] == "orders_show":
        OperationWrapper.orders_show(args[1], len(args) > 2 and args[2] == "--full")


def main(args):
    buf = io.StringIO() 
    with redirect_stdout(buf): 
        try:
            process_args(args)
        except excs.StandardError as e:
            print(e.get_message())
    x = buf.getvalue()
    return x
    

if __name__ == '__main__':
    print(main(sys.argv[1:]))