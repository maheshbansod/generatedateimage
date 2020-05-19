from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pillow"]

setup(
    name="generatedateimage",
    version="0.0.1",
    author="Mahesh Bansod",
    author_email="mahesh0bansod@gmail.com",
    description="A package which creates an image which shows the current date",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/your_package/homepage/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
