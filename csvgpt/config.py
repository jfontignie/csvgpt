"""
Simple configuration file parser for CSVGPT
"""
import os.path

import yaml

VERSION = 0.1


class Config:
    """
    Class configuration for CSVGPT
    """
    @staticmethod
    def get_instance():
        """
        :return: singleton
        """
        if not hasattr(Config, 'instance'):
            Config.instance = Config(f"{os.path.dirname(__file__)}/../config.yaml")
        return Config.instance

    @staticmethod
    def set_instance(config_):
        """
        :param config_: the instance
        :return: Build instance
        """
        Config.instance = config_

    def __init__(self, output):
        """
        :param output: load the yaml file
        """
        with open(output, 'r', encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def get(self, section, key, default_value=None):
        """
        :param section: the section in yaml file
        :param key: the key in the yaml file
        :param default_value: the default value if the key is not found
        :return: the value
        """
        if not self.exists(section, key):
            return default_value
        return self.data[section][key]

    def set(self, section, key, value):
        """
        :param section: the section in yaml file
        :param key: the key in the yaml file
        :param value: the value to set
        :return: none
        """
        self.data[section][key] = value

    def exists(self, section, key):
        """
        :param section: the section in yaml file
        :param key: the key to look for
        :return: if it exists or not
        """
        return section in self.data and key in self.data[section]
