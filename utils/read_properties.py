import json
import os


# Returns JSON data from a file
def get_json_config():
    try:
        with open('../config/config.json', 'r') as file:
            data = json.load(file)
    except:
        with open('config/config.json', 'r') as file:
            data = json.load(file)
    finally:
        return data


class ReadProperties:
    # Returns url value
    @staticmethod
    def get_config_url():
        return get_json_config()['baseUrl']

    # Returns browser value
    @staticmethod
    def get_config_browser():
        return get_json_config()['browser']
