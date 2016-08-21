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
from setuptools import setup, find_packages

version = "0.1.2"

setup(
    name="sru",
    version=version,
    author="Mohamed Abusaid",
    author_email="m.abusaid<at>yahoo<dot>com",
    packages=find_packages(),
    include_package_data=True,
    url="http://github.com/abusaidm/sru/packages/{}/".format(version),

    # license="LICENSE.txt",
    description="sru",
    # long_description=open("README.txt").read() or just """ lots of text here too""",
    # Dependent packages (distributions)
    dependency_links=[
        "https://github.com/abusaidm/sru_pip/tarball/master#egg=sru_pip-0.1.0",
        "https://github.com/abusaidm/sru_service/tarball/master#egg=sru_service-0.1.0",
        "https://github.com/ben-garside/sru_utils/tarball/master#egg=sru_utils-0.1.0",
        "https://github.com/abusaidm/sru_pkgmgr/tarball/master#egg=sru_pkgmgr-0.1.0"
    ],
    install_requires=[
        "aiohttp",
        "sru_pip>=0.1.0",
        "sru_service>=0.1.0",
        "sru_utils>=0.1.0",
        "sru_pkgmgr>=0.1.0"
    ]
)