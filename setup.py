from glob import glob
from os.path import basename, splitext
from setuptools import setup, find_packages

VERSION='0.1.0'

setup(
    name='openstack-ansible-cli',
    version=VERSION,
    author='Jean-Philippe Evrard',
    author_email='jean-philippe@evrard.me',
    description='OpenStack-Ansible CLI helpers',
    long_description=open('README.rst').read(),
    packages=find_packages('src/'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    tests_require=['pytest','tox'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        osa=osa.main:cli
    ''',
    classifiers= [
        'Environment :: OpenStack',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ]
)
