import os

from setuptools import setup


def find_packages(library_name):
    try:
        from setuptools import find_packages
        return find_packages()
    except ImportError:
        pass
    packages = []
    for directory, subdirectories, files in os.walk(library_name):
        if "__init__.py" in files:
            packages.append(directory.replace(os.sep, "."))
    return packages


display_name = "pymyadmin"
library_name = "pymyadmin"
version = "0.01"
description = ""
authors = ""
authors_email = ""
license = "LICENSE.txt"
url = "https://github.com/edvm/pymyadmin.git"


setup(
    name=display_name,
    version=version,
    author=authors,
    author_email=authors_email,
    description=description,
    url=url,
    license=license,
    packages=find_packages(library_name),
    install_requires=['Flask',
                      'Flask-Admin',
                      'Flask-SQLAlchemy',
                      'saw',],
    entry_points={
        'console_scripts':
            []
            },
    )
