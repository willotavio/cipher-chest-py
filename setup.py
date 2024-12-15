from setuptools import setup, find_packages

setup(
    name="enc_py",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "altgraph==0.17.4",
        "cffi==1.16.0",
        "cryptography==42.0.5",
        "packaging==24.1",
        "pefile==2023.2.7",
        "pycparser==2.22",
        "pyinstaller==6.9.0",
        "pyinstaller-hooks-contrib==2024.7",
        "pywin32-ctypes==0.2.2"
    ]
)
