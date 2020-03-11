

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="cjakuc-lambdata-cjakuc",
    version="1.5",
    author="Chris Jakuc",
    author_email="chris.jakuc@gmail.com",
    description="Learning how to create a package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cjakuc/lambdata-cjakuc",
    packages=find_packages()

)