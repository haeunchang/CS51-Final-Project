CS51 Final Project: Evolutionary Haiku Generator
===========

Installation
------------

To clone the repo:

```
git clone https://github.com/haeunchang/CS51-Final-Project.git
```

For running the code, Natural Language Toolkit (NLTK) and
pyhyphen have to be installed and Python must be able to import both.

NLTK 3.0 can be found here: http://www.nltk.org/

pyhyphen can be found here: https://code.google.com/p/pyhyphen/

For running the code, Python 3 is recommended.
Most of the code should be compatible with both Python 2 and Python 3,
but because of unicode issues Python 2 is not able to run the code
out-of-the-box and additional tweaking may be necessary.

### Guidelines for installation in CS50 Appliance:

Install all dependencies (including Python 3)
```
sudo yum install python3 python3-setuptools python3-PyYAML python3-pip python3-devel python3-numpy
```

Install NLTK: download NLTK 3.0 alpha 3 from http://www.nltk.org/nltk3-alpha/
and extract contents

After extracting `cd` into directory and run
```
sudo python3 setup.py install
```

Add NLTK to PYTHONPATH
```
PYTHONPATH="/usr/lib/python3.3/site-packages/nltk-3.0a3-py3.3.egg/":"${PYTHONPATH}"
export PYTHONPATH
```

Install PyHyphen
```
sudo python3-pip install PyHyphen
```

Give right (or working) permissions for hyphen directory
```
sudo chmod -R 755 /usr/lib/python3.3/site-packages/hyphen
```

Download NLTK data
```
python3
>>> import nltk
>>> nltk.download()
Downloader> d all
```

### Guidelines for installation in Arch Linux:

NLTK can be found as community/python-nltk package
```
sudo pacman -S python-nltk
```
pyhyphen can be found from AUR: python-pyhyphen package

NLTK also needs to download necessary data, for that
```
python
>>> import nltk
>>> nltk.download()
Downloader> d all
```

### Guidelines for installation (with Python 3) in Mac/Unix:

To install PyHyphen:
	
	Download the zip file found on pyhyphen website. 

	cd to the temporary directory

	Install PyHyphen: sudo -E python3 setup.py install
	
To install nltk: 
	
	Download the zip file found on nltk website for python 3

	cd to the temporary directory 

	Install nltk: sudo python3 setup.py install

To download NLTK data:

In python shell:
```
>>> import nltk
>>> nltk.download()
Downloader> d all
```
	
Running the code
----------------

```
Usage: main.py [options]

Options:
  -h, --help            show this help message and exit
  -t FILE, --train=FILE
                        train using data from FILE
  -g, --generate        generate new haikus using data aquired from training
  -f, --fresh           overwrite old training databases (old information WILL
                        be lost)
  -m, --markov          generate a haiku using a markov chain process
  --vocabulary          only use training data for training vocabulary
```

Example usage:
```
python3 main.py -t data.txt # train using data.txt
python3 main.py -g # generate poems using evolutionary approach
python3 main.py -m # generate poems using markov approach
```

Organization
------------

Here is a description of what each file will do:
- data.txt: cleaned database of haikus (Basho, ...)
- dictionary.py: module for interacting with several external libraries
- training.py: training input data
- evaluate.py: evaluating the goodness of poems
- evolve_population.py: the poem evolution code
- evo_object.py: class Evo_object
- monogram.py: class Monogram
- bigram.py: class Bigram
- line_haiku.py: class Line_Haiku
- line_type.py: class Line_type
- population_haiku.py: class Population_haiku
- main.py: using the program
