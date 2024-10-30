
from setuptools import setup, find_packages

setup(
    name="quantum-enhanced-lwe",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "pytest>=7.0.0",
        "scipy>=1.7.0",
    ],
    author="Julius AI",
    author_email="team@julius.ai",
    description="A quantum-resistant encryption system using Learning With Errors",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/quantum-enhanced-lwe",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
