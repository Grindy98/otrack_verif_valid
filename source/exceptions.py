from abc import ABC, abstractmethod
import main

class StandardError(ValueError, ABC):
    
    @abstractmethod
    def get_message():
        pass

class Error1(StandardError):

    def get_message():
        return "Missing required arguments to command.\n" + main.get_help()

class Error2(StandardError):

    def get_message():
        return "Invalid data format."

class Error3(StandardError):

    def get_message():
        return "No client matches with this information."

class Error4(StandardError):

    def get_message():
        return "No product matches with this information."

class Error5(StandardError):

    def get_message():
        return "Impossible to register the product: duplicate reference."

