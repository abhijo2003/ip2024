import os
import sys
from setuptools import setup

# Upgrade pip
os.system("/home/adminuser/venv/bin/python -m pip install --upgrade pip")

with open("README.md", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

if __name__ == "__main__":
    # We allow python setup.py sdist to always work to be able to create the
    # sdist and upload it to PyPI
    sdist_mode = len(sys.argv) == 2 and sys.argv[1] == "sdist"

    if not sdist_mode:
        # Install scikit-learn instead of the deprecated sklearn package
        os.system("/home/adminuser/venv/bin/python -m pip install scikit-learn")

    setup(
        description="Scikit-learn: A set of python modules for machine learning and data mining",
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        name="scikit-learn",
        version="0.24.3",  # Upgraded version to 0.24.3
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
    )
