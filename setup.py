from setuptools import setup, find_packages

setup(
    name='contacts',
    version='0.1.0',
    packages=find_packages(include=['contacts', 'contacts.*']),
    install_requires=['numpy>=1.14.5']
)
