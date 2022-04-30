import json

class parser():
    def __init__(self,file):
        print('Info - Initializing parser')
        with open(file,'r') as fi:
            self.config=json.load(fi)
            print('Info - Parsed configuration file is successful')
    def get_data(self):
        return self.config

