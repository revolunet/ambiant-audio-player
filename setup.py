#!/usr/bin/env python
from distutils.core import setup

setup(
    name='ambiantplayer',
    description='''Audio player for in-stores sound-system that offers a simple HTTP API ''',
    long_description=open('README.md').read(),
    version='0.1',
    author='Julien Bouquillon',
    author_email='julien@revolunet.com',
    url='http://github.com/revolunet/ambiantplayer',
    py_modules=['ambiant-audio-player'],
    scripts=['player.py'],
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Utilities'],
)
