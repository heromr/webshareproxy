from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

VERSION = "0.0.10"
DESCRIPTION = "A Python client library for the Webshare Proxy API, providing easy access to various operations like managing proxies, IP authorizations, user profile, notifications, and more."

setup(
    name="webshareproxy",
    version=VERSION,
    description=DESCRIPTION,
    author="HeroMR",
    author_email="mrhero4006@gmail.com",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/heromr/webshareproxy",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    keywords=["python", "webshare.io", "webshare proxy", "free proxy", "premium proxy", "webshareproxy"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
