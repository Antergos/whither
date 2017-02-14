# Always prefer setuptools over distutils
from setuptools import setup

setup(
    name='whither',
    version='0.2.5',
    packages=[
        'whither',
        'whither.base',
        'whither.toolkits',
        'whither.toolkits.qt',
        'whither.toolkits.gtk',
    ],
    url='https://github.com/antergos/whither',
    license='GPL-3.0',
    author='Antergos Linux Project',
    author_email='dustin@antergos.com',
    description='Desktop application SDK for creating Universal Linux Applications.',
    install_requires=[
        'PyQt5',
        'ruamel.yaml',
    ],
    package_data={
        '': ['whither.yml'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: JavaScript',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces',
    ],
    keywords='desktop-application-sdk framework sdk javascript universal html5'
)
