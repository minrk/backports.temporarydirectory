#!/usr/bin/env python
import sys

from distutils.core import setup

long_description = """
Use Python 3 tempfile.TemporaryDirectory on Python 2::

    try:
        from tempfile import TemporaryDirectory
    except ImportError:
        from backports.temporarydirectory import TemporaryDirectory
"""

setup_args = dict(
    name='backports.temporarydirectory',
    version='3.5.1',
    author="Min RK",
    author_email="benjaminrk@gmail.com",
    description="Backport of tempfile.TemporaryDirectory from Python 3.2",
    long_description=long_description,
    url="https://github.com/minrk/backports.temporarydirectory",
    packages=['backports'],
    license="Python Software Foundation License",
    cmdclass={},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Python Software Foundation License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
)

if 'bdist_wheel' in sys.argv:
    from wheel.bdist_wheel import bdist_wheel
    setup_args['cmdclass']['bdist_wheel'] = bdist_wheel

if __name__ == '__main__':
    setup(**setup_args)
