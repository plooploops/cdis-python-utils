from setuptools import setup, find_packages

setup(
    name="cdispyutils",
    version="0.2.0",
    description="General utilities for Gen3 development",
    license="Apache",
    install_requires=[
        "cryptography==2.1.2",
        "PyJWT==1.5.3",
        "requests==2.18.4",
        "six==1.11.0",
    ],
    packages=find_packages(),
)
