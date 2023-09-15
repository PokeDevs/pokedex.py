from setuptools import setup, find_packages
from codecs import open

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

with open('requirements.txt', 'r', 'utf-8') as f:
    requirements = f.readlines()

setup(
    name='pokedex.py',
    version='2.0.0',
    description='Python wrapper library for the Pokédex API.',
    long_description=readme,
    url='https://github.com/PokeDevs/pokedex.py',
    author='iamtraction',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    keywords='pokemon pokedex api database pokeapi pokedb wrapper library',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
)
