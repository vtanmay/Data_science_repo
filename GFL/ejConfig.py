from configparser import ConfigParser


def readConfigFile(ejConfigFilePath=None):
    dict={}
    config = ConfigParser()
    config.read(ejConfigFilePath)
    for section in config.sections():
       section_name=section
       dict[section_name]={}
       for item in config.items(section):
           dict[section_name][item[0]]=item[1]
    return dict