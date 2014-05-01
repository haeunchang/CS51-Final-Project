CS51 Final Project
===========

Installation
------------

To clone the repo:

```
git clone https://github.com/haeunchang/CS51-Final-Project.git
```

For running the code, Natural Language Toolkit (NLTK) and pyhyphen have to be installed and Python must be able to import both.

NLTK 3.0 can be found here: http://www.nltk.org/

pyhyphen can be found here: https://code.google.com/p/pyhyphen/

Guidelines for installation in Arch Linux:

NLTK can be found as community/python-nltk package
```
sudo pacman -S python-nltk
```
pyhyphen can be found from AUR: python-pyhyphen package

For running the code, Python 3 is recommended. Most of the code should be compatible with both Python 2 and Python 3, but because of unicode issues Python 2 may not be able to run the code out-of-the-box and additional tweaking may be necessary.

Guidelines for installation in Mac/Unix: 

Install Setuptools: http://pypi.python.org/pypi/setuptools
Install Pip: run sudo easy_install pip
Install Numpy (optional): run sudo pip install -U numpy
Install PyYAML and NLTK: run sudo pip install -U pyyaml nltk
Test installation: run python then type import nltk

Instructions for installation in Windows can be found on the nltk website. 

Running the code:
```
python main.py
```
Changing the input file: edit main.py `read_input` argument

Such way of having to modify source code should be a temporary solution.


Organization
------------

Here is a description of what each file will do:
- data.txt: cleaned database of haikus (Basho, ...)
- dictionary.py: module for interacting with several external libraries
- training.py: training input data
- haiku.py: class Haiku
- monogram.py: class Monogram
- bigram.py: class Bigram
- line_haiku.py: class Line_Haiku
- line_type.py: class Line_type
- population_haiku.py: class Population_haiku
