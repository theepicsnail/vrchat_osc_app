from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='vrc_osc_app',
    version='0.1dev0',
    author='snail', 
    author_email='vrc_osc_app@snail.rocks',
    packages=find_packages(),
    install_requires=[],
    long_description=open('README.md').read()
)