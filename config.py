#!/usr/bin/env python3

import configparser as ConfigParser
import io
import os
import pytoml

CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"


class SnipsConfigParser(ConfigParser.SafeConfigParser):
    def to_dict(self):
        return {section: {option_name: option for option_name, option in self.items(section)} for section in self.sections()}


def get_mqtt_config():
    '''
        Load the config from the SNIPS file
    '''
    if os.path.isfile('/etc/snips.toml'):
        with open('/etc/snips.toml') as confFile:
            configs = pytoml.load(confFile)
            if "snips-common" in configs:
                snips_common = configs['snips-common']
            else:
                print("Error al cargar configuración de SNIPS")
                return None
            return snips_common
    else:
        print("No se encuentra el archivo '/etc/snips.toml'")
        return None


def get_skill_config(_config_needed):
    '''
        Load config from Skill
    '''
    _config = _read_configuration_file()

    if not check_all_items(_config, _config_needed):
        print("Error en el config.ini")
        return None

    skill_config = _config['skill']
    return _config['skill']


def _read_configuration_file():
    '''
        Read the config file to parse the data
    '''
    try:
        with io.open(CONFIG_INI, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, ConfigParser.Error) as e:
        return dict()


def check_all_items(_config, _config_needed):
    '''
        Check all the needed infom in the _config
        TODO:
    '''
    for group in _config_needed:
        pass

    return True


def check_item(_configData, group_name, item_name):
    '''
        Check if the item exist in the group
    '''
    if (_configData.get("group_name").get("item_name") is None
            or len(_configData.get("group_name").get("item_name")) == 0):
        print("ERROR: No item_name in config.ini")
        return None
    else:
        return _configData.get("group_name").get("item_name")
