import sys
import io
from contextlib import redirect_stdout

import source.exceptions as excs
from source.operations import OperationWrapper
from source.persistent import dump_to_save, load_from_save

FILENAME = 'persistant_state.pkl'

def process_args(args):
    
    if not args:
        # Missing an operational arg
        raise excs.Error1

    if args[0] == "help":
        print(excs.get_help())        
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
    
    else:
        # Handles non-existent argument
        raise excs.Error1


def main(args, filename):
    load_from_save(filename)
    buf = io.StringIO() 
    with redirect_stdout(buf): 
        try:
            process_args(args)
        except excs.StandardError as e:
            print(e.get_message())
    x = buf.getvalue()
    dump_to_save(filename)
    return x
    

if __name__ == '__main__':
    print(main(sys.argv[1:], FILENAME))