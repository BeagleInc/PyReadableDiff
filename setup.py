import setuptools

import pydiff


setuptools.setup(
    name='pydiff',
    description='PyReadableDiff: Intuitive human-readable diff for text',
    author='Gevorg Davoian, Iulius Curt, Kevin Decker (the author of the original jsdiff library) and others',
    author_email='davoian.serf at gmail.com',
    url='https://github.com/BeagleInc/PyReadableDiff',
    version=pydiff.__version__,
    packages=setuptools.find_packages(),
    license='Apache-2.0'
)
