"""
Download Cplex by academic account

open the link: https://academic.ibm.com/a2mt/email-auth#/
submit your academic account

choose --> data science -->  IBM ILOG CPLEX Optimization Studio V22.1.1 for Windows x86-64

use anaconda to create environment (python=3.10)
open the anaconda prompt
$ conda create -n text_env python=3.10
$ conda activate text_env
$ pip install docplex

copy the "cplex" package in the Path C:\Program Files\IBM\ILOG\CPLEX_Studio2211\cplex\python\3.10\x64_win64
paste in the Path ...\.conda\envs\text_env\Lib\site-packages

Text:

open the anaconda prompt
$ conda activate text_env
$ python
>>> import cplex
>>> print(cplex.__version__)

>>> import docplex
>>> print(docplex.__version__)

if we can achieve the version of cplex and docplex, the cplex is deplaied.
"""
