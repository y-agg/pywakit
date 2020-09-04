from __future__ import with_statement
import os,regex as re
try:
    from setuptools import setup , find_packages
except ImportError:
    from distutils.core import setup

name = "pywakit"

def read_file(filename):
    with open(filename, encoding="utf8") as f:
        return f.read()

def _get_version_match(content):
    regex = r"^__version__ = ['\"]([^'\"]*)['\"]"
    version_match = re.search(regex, content, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

def get_version(path):
    return _get_version_match(read_file(path))

def get_requirements():
     return read_file('requirements.txt').split('\n')


setup(
    name=name,
    version=get_version(os.path.join(name, '__init__.py')),
    description='Automate the sending process of message in whatsapp through selenium',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    keywords=['Send whatsapp message','message','auto','whatsapp','selenium','info'],
    author='Yash Aggarwal',
    author_email='yash.aggarwal.7545@gmail.com',
    maintainer='Yash Aggarwal',
    url='https://github.com/y-agg/pywakit',
    license='MIT',
    packages=find_packages(),
    install_requires= get_requirements(),
    python_requires='!=3.0.*, !=3.2.*, !=3.3.*, !=3.5.*, !=3.6.*, !=3.7.*',
    # see classifiers https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)