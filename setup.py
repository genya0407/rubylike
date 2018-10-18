from setuptools import setup, find_packages

setup(
    name='rubylike',
    version='0.0.1',
    description='Provide ruby-like features.',
    author='Yusuke Sangenya',
    author_email='longinus.eva@gmail.com',
    url='https://github.com/genya0407/rubylike',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)
