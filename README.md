### Etherscan server

Etherscan server is a proxy server to etherscan api which expose REST API to fetch data about addresses and blocks.
Right now it only support GET requests and handle two queries:

```
<etherscan_server_address>/api/balance/<address_of_specific_ethereum_address>
```

which will respond with actual balance of given address and 

```
<etherscan_server_address>/api/block/<blockNumber>
```

which will show timestamp, blockMiner and blockReward and allows you to see other blocks mined by the same miner.

## Building and running server

In order to build docker image with etherscan server issue:

```sh
docker build -t etherscan_server .
```

than you can start etherscan_server with:

```sh
docker run -it  -p<port_to_listen>:8080 etherscan_server 
```

To override default configuration please prepeare a config.ini file with such content:

```
[etherscan]
host=<ip_address_to_listen_on> # defaults to 0.0.0.0
port=<port_to_listen_in> # defaults to 8080
```

and run etherscan_server with:
```sh
docker run -it -v <path_to_your_config>:/etc/etherscan/config.ini -p <port_to_listen_on>:<port_specified_in_config> etherscan_server
```

## Using client

Copy `etherscan_client/etherscan_client` to a directory under your PATH and issue:

```sh
etherscan_client <block/balance> <blockNumber/address_of_specific_ethereum_address> --server <address_of_etherscan_server>:<port_of_etherscan_server>
```
This script will show you current balance of specified ethereum account or will print informations about specified block.
