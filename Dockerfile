FROM debian:stretch-slim

RUN apt update && apt install -y python3 \
python3-pip

ADD . /opt/etherscan/

RUN pip3 install /opt/etherscan/

ADD config.ini /etc/etherscan/config.ini

CMD etherscan_server
