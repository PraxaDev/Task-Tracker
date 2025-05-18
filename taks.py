from os.path import dirname, realpath, isfile
from json import dump

class ManageJson():
    def __init__(self):
        self.path = dirname(realpath(__file__)) + '/'

    def create_json(self, file):

        data = {
            "id": "",
            "description": "",
            "status": "",
            "createAt": "",
            "updatedAt": ""        
        }
        path_data_file = self.path + file

        if not isfile(path_data_file):
            with open(path_data_file, 'w') as f:
                dump(data, f, indent=3)
            return True
        else:
            return False
