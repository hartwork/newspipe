#!/usr/bin/env python
# Copyright (C) 2010 Sebastian Pipping <sebastian@pipping.org>
# Licensed under GPL v2 or later

from distutils.core import setup
from newspipe.main import __version__, __url__

setup(
    name='newspipe',
    description='RSS/Atom aggregation to e-mail',
    license='GPL v2 or later',
    version=__version__,
    url=__url__,
    author='Ricardo M. Reyes',
    author_email='reyesric@ufasta.edu.ar',
    packages=['newspipe', ],
    scripts=['scripts/newspipe', ],
    data_files=[
        ('share/doc/newspipe', [
            'manual.html',
            'test.opml',
            'newspipe.ini.sample',
        ]),
    ],
)
