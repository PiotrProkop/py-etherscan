from flask_restful import Resource
import etherscan_server.common.utils as utils


class Block(Resource):

    _block_url = ("https://api.etherscan.io/api?module=block&"
                  "action=getblockreward&blockno={}")
    _blocks_by_miner_url = ("https://api.etherscan.io/api?module=account&"
                            "action=getminedblocks&address={}&blocktype=blocks")

    def _get_block(self, block_number):
        url = self._block_url.format(block_number)
        result = utils.fetch_data(url)
        return result

    def _get_blocks_by_miner(self, miner):
        url = self._blocks_by_miner_url.format(miner)
        result = utils.fetch_data(url)
        return result

    def _parse_output(self, block, other_blocks_by_miner):
        # remove the specified block and extract only blockNumber
        parsed_block_by_miner = [b["blockNumber"] for b in
                                 other_blocks_by_miner if b["blockNumber"]
                                 is not block]
        # TODO(pprokop): move parsing output dict to separate function
        return {"blockNumber": block["blockNumber"],
                "timeStamp": block["timeStamp"],
                "blockMiner": block["blockMiner"],
                "blockReward": block["blockReward"],
                "blockMinedByTheSameMiner": parsed_block_by_miner}

    def get(self, block_number):
        try:
            block = self._get_block(block_number)
            other_blocks_by_miner = self._get_blocks_by_miner(
                block["blockMiner"])
        except utils.EthereumException as e:
            return utils.prepare_response("Error", message=str(e))

        return utils.prepare_response(
            "Success", self._parse_output(block, other_blocks_by_miner))
