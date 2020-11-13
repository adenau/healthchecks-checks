import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="healthchecks-checks-beshiros", # Replace with your own username
    version="0.0.1",
    author="Alexandre Denault",
    author_email="alexandre.denault@adinfo.qc.ca",
    description="Checks to be used with healthchecks.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adenau/healthchecks-checks",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
