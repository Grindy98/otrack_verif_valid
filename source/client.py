import re

import persistent
import exceptions as e

class Client:
    def __init__(self, name, email, phone):
        self._name = name
        self._email = email
        self._phone = phone

        #TODO: check for identical email after spec update
        if not self.validate():
            raise e.Error2()
        
        # Get list of ids and choose next one after max value
        max_id = max([c._id for c in persistent.get_class_list(Client)] + [0])
        self._id = max_id + 1

    def validate(self):
        # If name or email don't exist
        if self._name is None or self._email is None:
            return False
        # If email does not contain @
        if not self._email.contains('@'):
            return False
        # If phone exists and isn't made out of digits alone
        if self._phone is not None and not bool(re.match(r'^[0-9]+$', self._phone)):
            return False
        return True
    
    def __str__(self) -> str:
        if self._phone is None:
            return f"{self._name} - {self._email} - Id: {self._id}"
        return f"{self._name} - {self._email} - {self._phone} - Id: {self._id}"
    