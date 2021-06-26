import codecs
import os

from setuptools import find_packages, setup


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


def parse_requirements(rel_path):
    requirements_list = []
    for line in read(rel_path).splitlines():
        if "git+" in line:
            package_name = line.split("/")[-1].split(".git")[0]
            if "#egg=" in line:
                package_name = line.split("#egg=")[-1]
            line = f"{package_name} @ {line}"
        requirements_list += [line]
    return requirements_list


# Get the long description from the README file
name = "seewald_episodes"
version = get_version("src/seewaldEpisodes/__init__.py")
description = "Collects new episode of 'Seewald - Die Vermessung der Musik'"
long_description = read("README.md")
long_description_content_type = "text/markdown"
url = "https://github.com/stgrmks/seewaldEpisodes"
author = "Markus Steger"
author_email = "m.steger@pm.me"
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Topic :: Software Development",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3 :: Only",
]
keywords = "ego-fm, seewald, spider"
packages = find_packages(where="src")
package_dir = {"": "src"}
python_requires = ">=3.5, <4"
install_requirements = parse_requirements("requirements.txt")

project_urls = {  # Optional
    "Bug Reports": "https://github.com/stgrmks/seewaldEpisodes/issues",
    "Funding": "https://donate.pypi.org",
    "Say Thanks!": "https://www.steger.dev",
    "Source": "https://github.com/stgrmks/seewaldEpisodes",
}

setup(
    name=name,  # Required
    version=version,  # Required
    description=description,  # Optional
    long_description=long_description,  # Optional
    long_description_content_type=long_description_content_type,  # Optional (see note above)
    url=url,  # Optional
    author=author,  # Optional
    author_email=author_email,  # Optional
    classifiers=classifiers,  # Optional
    keywords=keywords,  # Optional
    packages=packages,  # Required
    package_dir=package_dir,
    python_requires=python_requires,
    install_requires=install_requirements,  # Optional
    project_urls=project_urls,
)
