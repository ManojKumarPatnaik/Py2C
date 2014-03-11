# import sys
# sys.argv.extend("test".split())

from setuptools import setup, find_packages

#--------------------------------------------------------------------------
# Description of package
description = (
    "An translator to translate implicitly statically typed Python code into "
    "human-readable C++ code."
)

long_description = open("README.md").read()

# Metadata
classifiers = [
    'Development Status :: 1 - Planning',
    'Programming Language :: C++',
    # Might support other versions, but not so sure (yet).
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Code Generators',
    'Topic :: Software Development :: Compilers',
]

# The main setup call
setup(
    # Package data
    name="py2c",
    version="0.1-dev",
    packages=find_packages(exclude=["tests"]),
    package_data={
        'py2c': ['_ast_nodes.cfg'],  # include the configration file
    },
    install_requires=["ply"],
    zip_safe=False,
    # Metadata
    description=description,
    long_description=long_description,
    author="Pradyun S. Gedam",
    author_email="pradyunsg@gmail.com",
    url="https://github.com/pradyun/Py2C",
    classifiers=classifiers,
    # Testing
    test_suite="tests",
)