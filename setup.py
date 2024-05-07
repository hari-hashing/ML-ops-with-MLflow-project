import setuptools 

with open("README.MD", "r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Mlops_with_mlflow_[project]"
AUTHOR_USER_NAME = "hari-hashing"
SRC_REPO = "mlops_project"
AUTHOR_EMAIL = "hari@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="py packg for ml proj",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

# this setup file will look for the constructor file wherever it is 
# here the constructor file is __init__.py and install it as my local package
# to import data lets say from src componenets you need the setup file to first
# install it as the local package and then import the data 