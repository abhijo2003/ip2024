import os
from setuptools import setup

# Upgrade pip
os.system("/home/adminuser/venv/bin/python -m pip install --upgrade pip")

# Install scikit-learn
os.system("/home/adminuser/venv/bin/python -m pip install scikit-learn")

with open("README.md", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

if __name__ == "__main__":
    setup(
        name="YourPackageName",
        version="0.1.0",
        description="Your package description",
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        author="Your Name",
        author_email="your.email@example.com",
        url="https://github.com/yourusername/yourpackage",
        packages=["yourpackage"],
        install_requires=[
            "numpy",
            "scipy",
            "joblib",
            "threadpoolctl",
        ],
        extras_require={
            "tests": [
                "pytest",
                "pytest-cov",
                "nose",
                "coverage",
            ]
        },
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    )

