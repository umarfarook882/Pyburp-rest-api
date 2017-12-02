from distutils.core import setup

install_dependencies = (
    'requests == 2.8.14',
    'bs4 == 0.0.1'
)


setup(
    name='Pyburp-rest-api',
    version='0.1',
    packages=[''],
    package_dir={'': 'Pyburp-rest-api'},
    url='',
    license='MIT License',
    author='Umar Farook',
    author_email='Twitter: @umarfarook882',
    description='Pyburp-rest-api Python Package for Continuous Security Automation Pipeline'
)