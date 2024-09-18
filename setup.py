from setuptools import setup, find_packages

setup(
    name =          'info_tool_lib',
    version =       '0.0.7',
    packages =      find_packages(),
    description =   'Tools for better represent info for daily-work',
    author =        'Dmitry Klimenko',
    author_email =  'klimenko.dnk@gmail.com',
    zip_safe =      True,  
    install_requires = [
        'setuptools>=69.0.0',        
        'numpy>=1.26.4',
        'pandas>=2.1',
        'matplotlib>=3.8',
        'keyring>=24.0',
        'pyarrow>=15.0',
        'ipython>=8.23.0',
        'requests>=2.31.0',
            ],
    classifiers = [
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
            ],
    python_requires = '>=3.12',
)