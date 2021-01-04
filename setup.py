import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bf-gen",
    version="0.1.0",
    author="capra314cabra",
    author_email="capra314cabra@gmail.com",
    description="Supports you to generate Brainf**k code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="brainfuck generator generate whitespace",
    url="https://github.com/capra314cabra/bf-gen",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
