import setuptools


VERSION = "1.0.0"

with open("README.md", "r", encoding="utf-8") as readme:
    DESC_LONG = readme.read()


setuptools.setup(
    name="conlay",
    version=VERSION,
    author="Salliii",
    description="Python library for easy console layout setups",
    long_description_content_type="text/markdown",
    long_description=DESC_LONG,
    url="https://github.com/Salliii/conlay",
    packages=setuptools.find_packages(),
    install_requires=[],
    keywords=["python", "library", "console", "layout"]
)