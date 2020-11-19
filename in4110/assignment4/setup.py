#!/usr/bin/env python

from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(name='instapy',
      version='0.1',
      description='IN4110. Assignment 4.',
      author='Yauhen Khutarniuk',
      author_email='yauhenk@uio.no',
      packages=['instapy','instapy.bin'],
      ext_modules=cythonize("./instapy/*.pyx"),
      include_dirs=[numpy.get_include()],
      entry_points={
        'console_scripts': [
            'instapy = instapy.bin.instap:main',
        ]
     }
     )
