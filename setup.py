from setuptools import setup, find_packages

setup(
    name="Arkane",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "arkane.data": ["payloads.json"],
    },
    install_requires=["rich"],
    entry_points={
        "console_scripts": [
            "arkane=arkane.cli:main",
        ],
    },
    description="Reverse and bind shell generator",
    author="0xf0xy",
    license="MIT",
)
