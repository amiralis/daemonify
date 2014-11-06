try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import daemonify


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='daemonify',
      version=daemonify.__version__,
      description='daemonify: Python Daemon Class',
      long_description=readme(),
      author='Amirali Sanatinia',
      author_email='amirali@ccs.neu.edu',
      url='https://github.com/amiralis/daemonify',
      packages=['daemonify'],
      include_package_data=True)