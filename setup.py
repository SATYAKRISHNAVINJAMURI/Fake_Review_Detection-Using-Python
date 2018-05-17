from distutils.core import setup
from setuptools import setup, find_packages
setup(
    name='Fake-Review-Detection',
    version='0.1.0',
    author='V.Satya Krishna',
    author_email='satyakrishnavinjamuri868@gmail.com',
    packages=find_packages(),
    scripts=["__main__.py"]
    url='https://github.com/SATYAKRISHNAVINJAMURI/Fake_Review_Detection-Using-Python.git',
    license='LICENSE',
    description='Determines genuinness of a review based on the Sentimental Scroe and Box Whisker Plot Statistical Method for Outlier Detection',
    long_description=open('README.txt').read(),
    install_requires=[ "nltk >= 3.0.0"],
)

