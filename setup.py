import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scopus_harvester",
    version="0.0.1",
    author="Robert Jaworek",
    author_email="jaworek.robert@gmail.com",
    description="A set of functions to call Scopus Serial Title Metadata API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rbrtjwrk/scopus_harvester",
    project_urls = {
        "Bug Tracker": "https://github.com/rbrtjwrk/scopus_harvester/issues"
    },
    license="MIT",
    packages=["scopus_harvester"],
    package_data{"scopus_harvester": ["data/*.txt"]},
    install_requires=["requests", "pandas", "numpy"],
)


