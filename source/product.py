import re

import persistent
import exceptions as e

class Product:
    def __init__(self, ref, name, price):
        self.ref = ref
        self.name = name
        self.price = price

        if not self.validate():
            raise e.Error2

        # Check for unique ref
        if [c for c in self.get_list() if c.ref == ref]:
            raise e.Error5

    def validate(self):
        # If any fields don't exist
        if not self.ref or not self.name or not self.price:
            return False
        # If ref is not alphanum
        if not self.ref.isalnum():
            return False

        # If price is anything but a number that could have decimals
        if not bool(re.match(r'^-?(0|([1-9][0-9]*))(\.[0-9]+)?$', self.price)):
            return False

        return True
    
    def __str__(self) -> str:
        return f"{self.name} - €{self.price} - Ref: {self.ref}"
    
    @classmethod
    def get_list(cls):
        return persistent.get_class_list(cls)