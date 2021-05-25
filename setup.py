import setuptools
from distutils.core import setup


setup(
    name='pzSQL',
    version='0.0.4',
    description='Wrapper around psycopg2',
    author='John Reynolds',
    author_email='reynoldsjohngreg@gmail.com',
    url='https://github.com/jgr1204/pzSQL',
    install_requires=['psycopg2-binary'],
    setup_require=['wheel'],
    keywords=['postgres', 'psycopg2'],
    packages=['pzSQL'],
     )