import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="etherscan",
    version="0.0.1",
    author="Piotr Prokop",
    author_email="piotr.prok@gmail.com",
    description=("Simple REST server to get information about Ethereum accounts"
                 "and blocks."),
    license="Apache 2.0",
    keywords="etherscan client",
    packages=[
        'etherscan_server',
        'etherscan_server.resources',
        'etherscan_server.common'
    ],
    long_description=read('README.md'),
    install_requires=[
        "requests >= 2.10.0",
        "Flask >= 0.12.2",
        "Flask-RESTful >= 0.3.6",
        "pprint >= 0.1.0"
    ],
    entry_points={
        'console_scripts': [
            'etherscan_server = etherscan_server.app:main',
        ]
    }
)
