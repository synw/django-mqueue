from setuptools import setup, find_packages


version = __import__('mqueue').__version__

setup(
  name = 'django-mqueue',
  packages=find_packages(),
  include_package_data=True,
  version = version,
  description = 'Events queue application for Django',
  author = 'synw',
  author_email = 'synwe@yahoo.com',
  url = 'https://github.com/synw/django-mqueue', 
  download_url = 'https://github.com/synw/django-mqueue/releases/tag/'+version, 
  keywords = ['django', 'moderation', 'monitoring'], 
  classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
  zip_safe=False
)
