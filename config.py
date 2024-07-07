from dataclasses import dataclass
import toml

@dataclass
class Application:
    name: str
    input_type: str
    path: str

class Config:

    def __init__(self, target_file):
        self.file = target_file
        self.application = []
        self.loadTomlConfigs()

    def loadTomlConfigs(self):
        with open(self.file, 'r') as file:
            self.config = toml.load(file)
        print(self.config)
    
    def parseConfigs(self):
        self.application = []
        self.name = self.config['app']['name']
        if len(self.config['applications']) > 0:
            for app in self.config['applications']:
                self.application.append(Application(name = app['name'], input_type=app['input_type'], path=app['path']))

    def __str__(self):
        toReturn = f"Name: {self.name}"
        toReturn += f"Application: {self.application}"
        return toReturn

def main():
    target_file = "" 
    config = Config(target_file)
    config.parseConfigs()

if __name__=="__main__":
    main()