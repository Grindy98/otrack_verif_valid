from client import Client
import exceptions as e

class OperationWrapper:
    @staticmethod
    def clients_create(fullname, email, phone):
        c = Client(fullname, email, phone)
        Client.get_list().append(c)

    @staticmethod
    def clients_edit(id, fullname, email, phone):
        search_l = [c for c in Client.get_list() if c.id == id]
        assert(len(search_l) <= 1)
        # If no matching ID was found
        if not search_l:
            raise e.Error3
        
        # Change client properties on the fly because incorrect modifications won't affect the save file
        to_edit = search_l[0]
        if fullname:
            to_edit.name = fullname
        if email:
            #TODO: check email uniqueness after spec update
            to_edit.email = email
        if phone:
            to_edit.phone = phone
        
        if not to_edit.validate():
            raise e.Error2
        
        # Print the new client
        print(to_edit)

    @staticmethod
    def clients_delete(id):
        search_l = [c for c in Client.get_list() if c.id == id]
        assert(len(search_l) <= 1)
        # If no matching ID was found
        if not search_l:
            raise e.Error3
        # TODO: past and future order modifications should be handled here after implementation

        Client.get_list().remove(search_l[0])
    
    @staticmethod
    def clients_show(id):
        search_l = [c for c in Client.get_list() if c.id == id]
        assert(len(search_l) <= 1)
        # If no matching ID was found
        if not search_l:
            raise e.Error3
        
        print(search_l[0])
    
    @staticmethod
    def clients_getid(email):
        search_l = [c for c in Client.get_list() if c.id == id]
        assert(len(search_l) <= 1)
        # If no matching email was found
        if not search_l:
            raise e.Error3
        
        print(search_l[0].id)
    
    @staticmethod
    def products_create(ref, name, price):
        pass
    
    @staticmethod
    def products_edit(ref, new_ref, name, price):
        pass
    
    @staticmethod
    def products_delete(ref):
        pass
    
    @staticmethod
    def products_show(ref):
        pass
    
    @staticmethod
    def products_find(query):
        pass
    
    @staticmethod
    def orders_add(client_id, product_ref, amount, date):
        pass
    
    @staticmethod
    def orders_show(date, show_full):
        pass