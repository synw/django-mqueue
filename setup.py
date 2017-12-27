from setuptools import setup, find_packages


version = __import__('mqueue').__version__

setup(
    name='django-mqueue',
    packages=find_packages(),
    include_package_data=True,
    version=version,
    description='Events queue for Django',
    author='synw',
    author_email='synwe@yahoo.com',
    url='https://github.com/synw/django-mqueue',
    download_url='https://github.com/synw/django-mqueue/releases/tag/' + version,
    keywords=['django', 'logging', 'monitoring'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        'django<2',
        'redis',
        'influxdb',
        'django-fake-model',
    ],
    zip_safe=False
)
