import setuptools


classifiers = [f"Programming Language :: Python :: {version}" for version in ["3.7"]]


setuptools.setup(
    name="contest-website",
    version="0.0.1",
    license="MIT",
    platforms=["unix", "linux", "osx"],
    classifiers=classifiers,
    install_requires=[
        "django>=2.2.5,<3.0.0",
        "web3>=5.0.2,<6.0.0",
        "djangorestframework>=3.10.3,<4.0.0",
        "eth_utils>=1.7.0,<2.0.0",
    ],
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    zip_safe=False,
)
