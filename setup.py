from setuptools import find_packages
from setuptools import setup


setup(
    name="app",
    version="0.0.1",
    description="Web API",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "fastapi==0.68.1",
        "mangum==0.10.0",
    ],
    python_requires=">=3.9",
)

