from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="geometry",
    version="0.0.1",
    author="Ariel Rokem",
    author_email="author@example.com",
    description="Calculating geometric things",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arokem/geometry",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering"
    ],
    python_requires='>=3.6',
    install_requires=["numpy>=1.19.1"]
)