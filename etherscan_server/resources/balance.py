from flask_restful import Resource
import etherscan_server.common.utils as utils


class Balance(Resource):

    _balance_url = ("https://api.etherscan.io/api?module=account&action=balance"
                    "&address={}&tag=latest")

    def _get_balance_for_address(self, address):
        url = self._balance_url.format(address)
        return utils.fetch_data(url)

    def get(self, address):
        try:
            return utils.prepare_response(
                "Success", self._get_balance_for_address(address))
        except utils.EthereumException as e:
            return utils.prepare_response("Error", message=e)
