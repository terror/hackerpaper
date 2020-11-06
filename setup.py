import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="hackerpaper",
    version="1.0.0",
    author="Liam Scalzulli",
    author_email="liamscalzulli@gmail.com",
    description=("Hacker News to Instapaper"),
    long_description_content_type='text/markdown',
    license="BSD",
    keywords="hackernews, instapaper, cli",
    url="http://packages.python.org/hackerpaper",
    project_urls={
            "Source Code": "https://github.com/terror/hackerpaper",
    },
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    entry_points={"console_scripts": ["hackerpaper = hackerpaper.cli:cli"]},
    python_requires=">=3.7"
)
