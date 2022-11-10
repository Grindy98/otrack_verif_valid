import re

import persistent
import exceptions as e

class Client:
    def __init__(self, name, email, phone):
        assert(all(x is not None for x in [name, email, phone]))
        self.name = name
        self.email = email
        self.phone = phone

        #TODO: check for identical email after spec update
        if not self.validate():
            raise e.Error2()
        
        # Get list of ids and choose next one after max value
        max_id = max([c.id for c in self.get_list()] + [0])
        self.id = max_id + 1

    def validate(self):
        # If name or email don't exist
        if not self.name or not self.email:
            return False
        # If email does not contain @
        if not self.email.contains('@'):
            return False
        # If phone exists and isn't made out of digits alone
        if self.phone and not bool(re.match(r'^[0-9]+$', self.phone)):
            return False
        return True
    
    def __str__(self) -> str:
        if self.phone:
            return f"{self.name} - {self.email} - Id: {self.id}"
        return f"{self.name} - {self.email} - {self.phone} - Id: {self.id}"
    
    @classmethod
    def get_list(cls):
        return persistent.get_class_list(cls)