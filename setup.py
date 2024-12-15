from setuptools import setup, find_packages

setup(
    name="cipher_chest",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "cffi==1.17.1",
        "cryptography==44.0.0",
        "pycparser==2.22"
    ]
)
