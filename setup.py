from setuptools 
import setup

setup(
    name = "fakebook",
    version = "0.1",
    package_dir = {'': 'src'},
    packages = [
        'fakebook',
    ],

    install_requires = [
        'requests>=1.1.0',
    ],

    package_data = {},

    author = "Montana Mendy",
    author_email = "montana@getprowl.com",
    description = "Finding my informant on Facebook",
    license = "JSON License",
    keywords = "facebook test users",
)
