import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="hackerpaper",
    version="0.0.1",
    author="Liam Scalzulli",
    author_email="liamscalzulli@gmail.com",
    description=("Hacker News to Instapaper"),
    license="BSD",
    keywords="hackernews, instapaper, cli",
    url="http://packages.python.org/hackerpaper",
    packages=find_packages(),
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
