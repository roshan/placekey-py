import setuptools
import os

version_data = {}
version_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), 'placekey', '__version__.py')
with open(version_path, 'r') as f:
    exec(f.read(), None, version_data)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="placekey",
    version=version_data['__version__'],
    author="SafeGraph Inc.",
    author_email="russ@safegraph.com",
    description="Utilities for working with Placekeys",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Placekey/placekey-py",
    packages=setuptools.find_packages(),
    install_requires=['h3', 'shapely', 'requests', 'ratelimit', 'backoff'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
