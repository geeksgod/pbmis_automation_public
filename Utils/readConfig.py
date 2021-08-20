import configparser

config = configparser.RawConfigParser()




class ReadConfig:
    def __init__(self,path):    
        config.read(path)