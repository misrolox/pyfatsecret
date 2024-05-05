from setuptools import setup, find_packages


with open("README.md") as readme_file:
    DESCRIPTION = readme_file.read()

setup(
    name="pyfatsecret",
    version="0.1",
    license="MIT",
    author="Andrew Mitri",
    author_email="mitriandrew@hotmail.com",
    description="A simple python wrapper for the Fatsecret API.",
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://https://github.com/misrolox/pyfatsecret",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=['requests']
)
