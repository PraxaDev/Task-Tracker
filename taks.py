from os.path import dirname, realpath, isfile
from json import dump, load

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
        
    def read_json(self, file):
        if isfile(self.path + file):
            with open(self.path + file) as f:
                data = load(f)
            return data
        else:
            return False
