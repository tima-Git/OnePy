# encoding: UTF-8

"""
OnePy - An Own Built Trading Framework in Python.

The OnePy project is an open-source quantitative trading framework.
The project is mainly written in Python.

"""


import os
from setuptools import setup, find_packages, Command


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system("rm -vrf ./build ./dist ./*.pyc ./*.egg-info")


setup(
    name="Onepy_trader",
    version="1.00.0",
    author="Chandler_Chan",
    author_email="chenjiayicjy@gmail.com",
    license="MIT",
    url = "https://github.com/Chandlercjy/OnePy",
    description="Python Backtesting library for trading strategies.",
    packages=find_packages(),
    cmdclass={
        "clean": CleanCommand,
    }, install_requires=["pandas", "numpy","TA-Lib","plotly","funcy","arrow"]
)
