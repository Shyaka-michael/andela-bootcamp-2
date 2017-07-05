from setuptools import setup

setup(
    name='News App',
    version='1.0',
    py_modules=['app'],
    install_requires=[
        'Click', 'requests'
    ],
    entry_points='''
        [console_scripts]
        hello = app:cli,
    ''',
)