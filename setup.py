from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="teste1_image_processing",
    version="0.0.1",
    author="Rafael Souza",
    author_email="rafaelrodriguero@msn.com",
    description="Image Processing Package using skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rafarodriguero/image_processing_test",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
