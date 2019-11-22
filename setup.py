import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mygrads",
    version="0.0.2",
    author="David Nielsen",
    author_email="davidnielsen@id.uff.br",
    description="A set of GrADS functions in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/davidmnielsen/mygrads",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy', 'matplotlib', 'xarray', 'cartopy']

)
