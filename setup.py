from setuptools import find_namespace_packages
from setuptools import setup

setup(
    name='gym_multi_armed_bandits',
    author='Mohamed Amine ZGHAL',
    packages=find_namespace_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.6.*',
    version='0.0.1',
    install_requires=['gym']
)
