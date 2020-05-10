from setuptools import setup
setup(
    name = 'data-cli',
    version = '0.1.0',
    packages = ['data'],
    entry_points = {
        'console_scripts': [
            'data = data.__main__:main'
        ]
    })