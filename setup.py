import setuptools

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Chicken-Disese"
AUTHOR_USER_NAME = "Virenkun"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "ch20btech11039@iith.ac.in"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Images Classification",
    long_description=long_description,
    long_description_content ="text/markdown",
    url=f"https://github.com/Virenkun/Chicken-Disese.git",
    project_urls={
        "Bug Tracker" : f"https://github.com/Virenkun/Chicken-Disese.git/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)