#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from distutils.core import setup

use_fortran = False

if use_fortran:
    interface = 'fort'
else:
    interface = 'templated'


version_ = '0.1.10-dev'
name_ = 'finitediff'

if '--help'in sys.argv[1:] or sys.argv[1] in ('--help-commands', 'egg_info', 'clean', '--version'):
    cmdclass_ = {}
    ext_modules_ = []
else:
    # e.g. egg_info must not import from dependencies (pycompilation)
    import numpy
    from pycompilation.dist import clever_build_ext
    from pycompilation.dist import CleverExtension
    from pycompilation.util import ArbitraryDepthGlob

    cmdclass_ = {'build_ext': clever_build_ext}
    ext_modules_ = [
        CleverExtension(
            'finitediff._finitediff_'+interface,
            sources=[
                './src/finitediff_fort.f90',
                './src/c_finitediff_fort.f90',
                './external/newton_interval/src/newton_interval.c',
                './finitediff/_finitediff_'+interface+'.pyx'
            ],
            pycompilation_compile_kwargs={
                'per_file_kwargs': {
                    ArbitraryDepthGlob('*.c'): {'std': 'c99'}
                }
            },
            include_dirs=[
                './src',
                './external/newton_interval/include',
                numpy.get_include()
            ]
        )
    ]

setup(
    name=name_,
    version=version_,
    author='Björn Dahlgren',
    author_email='bjodah@DELETEMEgmail.com',
    description='Finite difference weights for any derivative order on arbitrarily spaced grids.',
    license = "BSD",
    url='https://github.com/bjodah/'+name_,
    download_url='https://github.com/bjodah/'+name_+'/archive/v'+version_+'.tar.gz',
    packages=[name_],
    cmdclass = cmdclass_,
    ext_modules = ext_modules_
)
