import os
from setuptools import setup

def readme_to_description(readme):
    return open(readme).read()

setup(
        name = "Mapyle",
        version = "1.0",
        author = "Adam Berger, Jake Medal",
        author_email = "adam@mapyle.org",
        description = ("Python curses UI for compiling programs (among other things"),
        license = "Apache 2.0",
        keywords = "Compile Python",
        url = "http://www.mapyle.org",
        packages=['mapyle', 'tests'],
        long_description=readme_to_description('README.md'),
        )
