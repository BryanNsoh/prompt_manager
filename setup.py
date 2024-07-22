from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="llm_prompt_manager",
    version="0.1.2",
    author="Bryan Anye",
    author_email="bryan.anye.5@gmail.com",
    description="A flexible system for managing and processing prompt templates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BryanNsoh/prompt_manager",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "chardet",
    ],
)