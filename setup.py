# coding: utf-8

"""
    JOJ Horse

    Git version: 3b2baac@2021-06-08 19:39:58  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "horse-python-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="JOJ Horse",
    author_email="",
    url="",
    keywords=["Swagger", "JOJ Horse"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Git version: 3b2baac@2021-06-08 19:39:58  # noqa: E501
    """
)
