import codecs
import os

try:
    from setuptools import setup
except:
    from distutils.core import setup

from sugar import __version__

with open('README.md', 'r') as fp:
    long_description = fp.read()

setup(
    name="Sugar",
    version=__version__,
    description="A minimal web framework by Python.",
    long_description=long_description,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords="web framework",
    author="taoliu0509",
    author_email="taoliu14@acm.org",
    url="https://github.com/ltoddy/sugar",
    license="MIT License",
    packages=["sugar","sugar.util"],
    include_package_data=True,
    zip_safe=True,
)
