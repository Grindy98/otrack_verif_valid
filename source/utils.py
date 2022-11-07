import json
from abc import ABC, abstractmethod

class jsonUtils(ABC):
    # jsonLoad will be used for editing, printing or getting various fields
    def jsonLoad(filename : str) -> dict:
        return json.load(open(filename))

    # jsonDump will be used for editing and creating
    @abstractmethod
    def jsonDump(object : dict, filename : str):
        with open(filename, 'w') as outputFile:
            outputFile.write(json.dumps(object, indent=4))