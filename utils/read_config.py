import configparser
import os
from dotenv import load_dotenv
# Load variables from .env file into the system environment
load_dotenv()

# Load the config file
config = configparser.RawConfigParser()
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'configs', 'config.ini'))
config.read(config_path)


class ReadConfig:
    @staticmethod
    def get_application_url():
        return config.get('common info', 'baseURL')

    @staticmethod
    def get_user_email():
        return config.get('common info', 'userEmail')

    @staticmethod
    def get_password():
        return config.get('common info', 'password')

    # Database Getters
    @staticmethod
    def get_db_host():
        return os.getenv('db_host')

    @staticmethod
    def get_db_user():
        return os.getenv('db_user')

    @staticmethod
    def get_db_password():
        return os.getenv('db_password')

    @staticmethod
    def get_db_name():
        return os.getenv('db_name')