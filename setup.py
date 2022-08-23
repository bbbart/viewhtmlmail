from setuptools import setup

setup(
    name='viewhtmlmail',
    version='0.1.0',
    py_modules=['viewhtmlmail'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'viewhtmlmail = viewhtmlmail:cli',
        ],
    },
)
