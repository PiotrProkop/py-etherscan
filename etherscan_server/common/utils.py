import os.path
import requests


def fetch_data(url):
    response = requests.get(url).json()
    if response["status"] != "1":
        raise EthereumException(response["message"])
    return response["result"]


# prepare unified response
def prepare_response(status, result=None, message=None):
    return {"status": status,
            "message": message,
            "result": result}


def parse_config(config_location):
    if os.path.exists(config_location):
        import configparser
        config = configparser.ConfigParser()
        config.read(config_location)
        # read etherscan section
        return dict(config.items("etherscan"))
    else:
        raise NoConfigException("No config was found")


class EthereumException(Exception):
    pass


class NoConfigException(Exception):
    pass
