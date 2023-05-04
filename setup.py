import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1' 
PACKAGE_NAME = 'cheatsheetDS' 
AUTHOR = '4bm4'
AUTHOR_EMAIL = 'AB_m4@outlook.com'
URL = 'https://github.com/4bm4/my-data-science-cheat-sheet'

LICENSE = 'MIT'
DESCRIPTION = 'here are the automations of the data analysis processes that I use most often' 
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
'contourpy==1.0.7',
'cycler==0.11.0',
'dmba==0.2.3',
'imbalanced-learn==0.10.1',
'imblearn==0.0',
'matplotlib==3.7.1',
'numpy==1.24.3',
'pandas==2.0.1',
'pygam==0.9.0',
'scikit-learn==1.2.2',
'scipy==1.10.1',
'seaborn==0.12.2',
'statsmodels==0.13.5',
    ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)