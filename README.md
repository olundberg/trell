# trell
Trell case

Oscar Lundberg, 2021-09-06

## Introduction


### Environment

To create the environment

'''
conda env create -f environmeny.yml
'''

To export environment use 
'''
conda env export --from-history | grep -v "^prefix: " > environment.yml
'''

## Project structure

* data - folder where data is stored
* lib  - lib for python files
* presentation - folder for latex presentation
* tests - folder for python testing
* case_3.ipynb - Jupyter Notebook
* Case optin 3 - Demand prediction.pdf - Description of case 
* README.md - This file


