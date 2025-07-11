from setuptools import setup, find_packages

setup(
    name='aeslang',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['aeslang=aeslang.main:main']
    },
    python_requires='>=3.6',
)