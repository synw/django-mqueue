from setuptools import setup, find_packages

setup(
  name = 'django-mqueue',
  packages=find_packages(),
  include_package_data=True,
  version = '0.1',
  description = 'Events queue application for Django',
  author = 'synw',
  author_email = 'synwe@yahoo.com',
  url = 'https://github.com/synw/django-mqueue', 
  download_url = 'https://github.com/synw/django-mqueue/releases/tag/0.1', 
  keywords = ['django', 'moderation', 'monitoring'], 
  classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
  install_requires=[
        "Django >= 1.8.0",
    ],
  zip_safe=False
)
