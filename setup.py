"""
SRU
Special Reconnaissance Unit
-----------
python SRU
Link
`````
* Source
  https://github.com/abusaidm/
"""
from setuptools import setup

version = "0.1.1"

setup(
    name="sru",
    version=version,
    author="Mohamed Abusaid",
    author_email="m.abusaid<at>yahoo<dot>com",
    packages=[
        "sru",
        "sru.conf",
        "sru.support",
        "sru.misc.service"
        ],
    include_package_data=True,
    url="http://github.com/abusaidm/sru/packages/{}/".format(version),

    # license="LICENSE.txt",
    description="sru",
    # long_description=open("README.txt").read() or just """ lots of text here too""",
    # Dependent packages (distributions)
    dependency_links=[
        "https://github.com/abusaidm/sru_pip/tarball/master#egg=sru_pip-0.1.0"
    ],
    install_requires=[
        "aiohttp",
        "sru_pip>=0.1.0"
    ]
)