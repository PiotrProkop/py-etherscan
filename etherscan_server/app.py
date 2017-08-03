#!/usr/bin/env python3

import os
import sys

from flask import Flask
from flask_restful import Api
from etherscan_server.resources.balance import Balance
from etherscan_server.resources.block import Block
import etherscan_server.common.utils as utils

CONFIG_DEFAULT_LOCATION = "/etc/etherscan/config.ini"

app = Flask(__name__)
api = Api(app)

# adding routes
api.add_resource(Balance, '/api/balance/<string:address>')
api.add_resource(Block, '/api/block/<string:block_number>')


def main():
    # possibilty to change config location by ENV
    config_env = os.getenv("ETHERSCAN_CONFIG")
    config_location = config_env if config_env else CONFIG_DEFAULT_LOCATION
    try:
        options = utils.parse_config(config_location)
    except utils.NoConfigException as e:
        print(e)
        sys.exit(1)

    # TODO(pprokop): make reading from config file less ugly
    app.run(host=options.get("host", "0.0.0.0"),
            port=int(options.get("port", "8080")))

if __name__ == '__main__':
    main()
