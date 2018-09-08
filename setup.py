from setuptools import setup, find_packages

import envconf

setup(
    name='envconf',
    version=envconf.__version__,
    description='Easy config setup from the environment',
    url='https://github.com/danielunderwood/envconf',
    author='Daniel Underwood',
    license='MIT',

    packages=find_packages(),

    extras_require={
        'test': ['pytest']
    },
)