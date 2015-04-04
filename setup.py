# -*- coding: utf-8 -*-
# !/usr/bin/env python

# to install, use:
# python setup.py install --user

import numpy as np

__author__ = 'lgeorge & amazel'
__version__ = "0.0.1"
__maintainer__ = 'lgeorge & amazel'
__status__ = "Dev"


from distutils.core import setup

setup(
    name='protolab',
    version='0.0.1',
    author='lgeorge',
    packages=["protolab"],
    install_requires=["cv2", "numpy",],
    py_modules=["geometry", "gpx", "image", "sensors", "webcam"],
)
