import logging
import os
import toml

config_logger = logging.getLogger(__name__)

# Add 
# @dataclass
# class RSSList:
#     websites: list

# @dataclass
# class Bot:
#     name: str
#     environment: str
#     email: str

class Config:

    def __init__(self, config_file) -> None:
        self.file: any = config_file
        self.loadTomlConfigs()
        config_logger.info("Instantiated Config Class")

    def loadTomlConfigs(self) -> None:
        if not os.path.exists(self.file):
            config_logger.info("Config file not found")
            raise Exception(f"Could not find {self.file}. Please locate or create file.")
        else:
            with open(file= self.file, mode= 'r') as file:
                self.config: dict[str, any] = toml.load(f= file)
                config_logger.info("Config file found and loaded.")
                
    
    def parseConfigs(self) -> None:
        self.name: str = self.config['bot']['botname']
        self.env: str = self.config['bot']['environment']
        self.fromemail: str = self.config['notifications']['from_email']
        self.toemail: str = self.config['notifications']['to_email']
        self.fromnumber: str = self.config['notifications']['from_number']
        self.tonumber: str = self.config['notifications']['to_number']
        
        config_logger.info("Config file parsed")


def main() -> None:
    dir_name: str = os.path.dirname(p=__file__)
    config_file: str = os.path.join(dir_name, "config.toml")
    Config(config_file= config_file)

if __name__=="__main__":
    main()
