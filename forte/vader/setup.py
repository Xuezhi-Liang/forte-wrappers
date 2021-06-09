import sys

import setuptools

if sys.version_info < (3, 6):
    sys.exit("Python>=3.6 is required by Forte.")

setuptools.setup(
    name="forte.vader",
    version="0.0.1",
    url="https://github.com/asyml/forte_wrappers/vader",
    description="Provide Forte implementations of a fantastic collection of "
    "NLP tools.",
    license="Apache License Version 2.0",
    packages=["forte.vader"],
    include_package_data=True,
    platforms="any",
    install_requires=[
        "forte @ git+https://git@github.com/asyml/forte.git",
        "vaderSentiment==3.2.1",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)