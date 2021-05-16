from distutils.core import setup


setup(
    name='pzSQL',
    version='0.0.1',
    description='Wrapper around psycopg2',
    author='John Reynolds',
    author_email='reynoldsjohngreg@gmail.com',
    url='https://github.com/jgr1204/pzSQL',
    install_requires=['psycopg2'],
    packages=['pzSQL'],
     )