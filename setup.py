from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="docprofiler",
    version="1.0.0",
    description="A Python package to generate document profiler or extract metadata from text in parallel using several Docker images",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Aayushpatel007/DocProfiler",
    author="Aayush Patel",
    author_email="patelaayush678@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    packages=["DocProfiler"],
    include_package_data=True,
    install_requires=["requests","asyncio","aiohttp"]
)