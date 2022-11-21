import re

import source.persistent as persistent
import source.exceptions as e
from source.product import Product
from source.client import Client

import datetime

class Order:
    def __init__(self, client, product, amount, date) -> None:
        self.product_ref = product
        self.date = date

        # Convert string to int
        try:
            self.client_id = int(client)
        except:
            raise e.Error3()

        # Convert string to float
        try:
            self.amount = float(amount)
        except:
            raise e.Error2()
        
        validate = self.validate()
        
        if validate == 3:
            raise e.Error3()
        if validate == 4:
            raise e.Error4()
        if validate == 2:
            raise e.Error2()
    
    def validate(self) -> int:
        # If no client has the specified id
        search_p = [p for p in Product.get_list() if p.ref == self.product_ref]
        search_c = [c for c in Client.get_list() if c.id == self.client_id]
        
        if not search_c:
            return 3
        # If no product has the specified product ref
        if not self.product_ref:
            return 4
        # TODO: If date exists and is not in date format
        if self.amount < 0:
            return 2
        if not bool(re.search("([0-9]|1[0-9]|2[0-9]|3[0-5])/([0-9]|1[0-9]|2[0-9]|3[0-5])/([0-9][0-9][0-9][0-9])", self.date)):
            return 2
        return 0
    
    def __str__(self) -> str:
        return f"{self.product_ref} - {self.amount}"
    
    @classmethod
    def get_list(cls):
        return persistent.get_class_list(cls)