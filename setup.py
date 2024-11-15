from setuptools import setup, find_packages

# Dynamically load requirements from requirements.txt
def parse_requirements(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()


setup(
    name="music-industry-insights",
    version="0.1.0",
    description="Music Industry Analysis Project for DS5610",
    python_requires=">=3.12",
    packages=find_packages(where="scripts"),
    package_dir={"": "scripts"},
    install_requires=parse_requirements("requirements.txt"),
    include_package_data=True,
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
