from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "pydotted"
LONG_DESCRIPTION = "pydotted is a very simple low code python module that allows for dot notation access / updating of a dictionary instance, including nested dictionaries."

# Setting up
setup(
    name="pydotted",
    version=VERSION,
    author="Alex Redden",
    author_email="alexander.h.redden@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=["python", "dict", "dot", "dotdict", "dot notation", "pydotted"],
    classifiers=[],
)
