from abc import ABC, abstractmethod
import source.main as main

class StandardError(ValueError, ABC):
    
    @abstractmethod
    def get_message(self):
        pass

class Error1(StandardError):

    def get_message(self):
        return "Missing required arguments to command.\n" + main.get_help()

class Error2(StandardError):

    def get_message(self):
        return "Invalid data format."

class Error3(StandardError):

    def get_message(self):
        return "No client matches with this information."

class Error4(StandardError):

    def get_message(self):
        return "No product matches with this information."

class Error5(StandardError):

    def get_message(self):
        return "Impossible to register the product: duplicate reference."

class Error6(StandardError):

    def get_message(self):
        return "This email is already used, please choose another one."

