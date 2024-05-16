from setuptools import setup, find_packages

setup(
    name='MASAnalysis',
    version='0.1.0',
    packages=find_packages(include=['MASAnalysis', 'MASAnalysis.*']),
    install_requires=['numpy>=1.14.5','pytest']
)
