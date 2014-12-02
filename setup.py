import sys
from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

install_requires = ['werkzeug']
if sys.version_info < (2, 7):
    install_requires.append("argparse == 1.2.1")

setup(name='repyt',
      version='0.1.0',
      description='Automatically re-run Python applications when files change.',
      long_description=readme(),
      url='https://github.com/di/repyt',
      author='Dustin Ingram',
      author_email='di@wiota.co',
      keywords='console command-line development re-run reload testing tests',
      entry_points = {
            'console_scripts': ['repyt = repyt.repyt:main']
      },
      license='MIT',
      packages=['repyt'],
      install_requires=install_requires,
      classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Natural Language :: English',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: POSIX :: Linux',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.0',
            'Programming Language :: Python :: 3.1',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Topic :: Utilities'
        ],
      zip_safe=False)
