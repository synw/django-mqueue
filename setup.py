from os import path
from setuptools import setup, find_namespace_packages


version = __import__("mqueue").__version__

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="django-mqueue",
    packages=find_namespace_packages(),
    include_package_data=True,
    version=version,
    description="Events queue for Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="synw",
    author_email="synwe@yahoo.com",
    url="https://github.com/synw/django-mqueue",
    download_url="https://github.com/synw/django-mqueue/releases/tag/" + version,
    keywords=["django", "logging", "monitoring"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django :: 1.11",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
    ],
    license="MIT",
    zip_safe=False,
    install_requires=["django-mcpx", "django-import-export"],
)
