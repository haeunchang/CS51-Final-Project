CS51 Final Project: Evolutionary Haiku Generator
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

Guidelines for installation (with Python 3) in Mac/Unix:

To install PyHyphen:
	Download the zip file found on pyhyphen website. 
	cd to the temporary directory
	Install PyHyphen: 'sudo -E python3 setup.py install'

To install nltk: 
	Download the zip file found on nltk website for python 3
	cd to the temporary directory 
	Install nltk: 'sudo python3 setup.py install'

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
