import os.path

import yaml

VERSION = 0.1


class Config:

    @staticmethod
    def get_instance():
        if not hasattr(Config, 'instance'):
            Config.instance = Config(f"{os.path.dirname(__file__)}/../config.yaml")
        return Config.instance

    @staticmethod
    def set_instance(config_):
        Config.instance = config_

    def __init__(self, output):
        with open(output, 'r') as f:
            self.data = yaml.safe_load(f)

    def get(self, section, key, default_value=None):
        if not self.exists(section, key):
            return default_value
        return self.data[section][key]

    def set(self, section, key, value):
        self.data[section][key] = value

    def exists(self, section, key):
        return section in self.data and key in self.data[section]
