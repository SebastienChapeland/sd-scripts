from setuptools import setup, find_namespace_packages
 
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name = "library", 
    packages = find_namespace_packages(),
    install_requires=requirements,
)