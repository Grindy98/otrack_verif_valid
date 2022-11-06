class OperationWrapper:
    @staticmethod
    def clients_create(fullname, email, phone):
        pass

    @staticmethod
    def clients_edit(id, fullname, email, phone):
        pass
    
    @staticmethod
    def clients_delete(id):
        pass
    
    @staticmethod
    def clients_show(id):
        pass
    
    @staticmethod
    def clients_getid(email):
        pass
    
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