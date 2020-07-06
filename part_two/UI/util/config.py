import ConfigParser


class Config(object):

    config_path = "UI/config/config.ini"

    def __init__(self):
        self.configParser = ConfigParser.RawConfigParser()
        self.configParser.read(self.config_path)

    def get_credentials(self, cred):
        return self.configParser.get('USER', cred)

    def get_api_user(self):
        return self.get_credentials('user'), self.get_credentials('password')

    def get_base_url(self):
        return self.configParser.get("URLS", "base")

    def get_grid(self):
        return self.configParser.get("URLS", "seleniumAddress")
