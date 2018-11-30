from setuptools import setup, find_packages

setup(
    name="hidy",
    version="0.1",
    description="A multi monitor high dpi display configurator",
    author="Peter Stein",
    author_email="peter.stein@protonmail.com",
    packages=find_packages(),
    entry_points={"console_scripts": ["hidy=hidy.main:main"]},
)