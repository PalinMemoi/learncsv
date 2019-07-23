
CleverCSV: A Clever CSV Parser
==============================


.. image:: https://travis-ci.org/alan-turing-institute/CleverCSV.svg?branch=master
   :target: https://travis-ci.org/alan-turing-institute/CleverCSV
   :alt: Build Status


.. image:: https://badge.fury.io/py/clevercsv.svg
   :target: https://pypi.org/project/clevercsv/
   :alt: PyPI version


.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/alan-turing-institute/CleverCSVDemo/master?filepath=CSV_dialect_detection_with_CleverCSV.ipynb
   :alt: Binder


*This package is currently in beta. If you encounter any problems, please open 
an issue or submit a pull request!*

Handy links:


* `CleverCSV on Github <https://github.com/alan-turing-institute/CleverCSV>`_
* `CleverCSV on PyPI <https://pypi.org/project/clevercsv/>`_
* `Demo of CleverCSV on Binder 
  (interactive!) <https://mybinder.org/v2/gh/alan-turing-institute/CleverCSVDemo/master?filepath=CSV_dialect_detection_with_CleverCSV.ipynb>`_
* `Paper on arXiv <https://arxiv.org/abs/1811.11242>`_
* `Reproducible Research Repo <https://github.com/alan-turing-institute/CSV_Wrangling/>`_

Introduction
------------


* CSV files are awesome: they are lightweight, easy to share, human-readable, 
  version-controllable, and supported by many systems and tools!
* CSV files are terrible: they can have many different formats, multiple 
  tables, headers or no headers, escape characters, and there's no support for 
  data dictionaries.

CleverCSV is a Python package that aims to solve many of the pain points of 
CSV files, while maintaining many of the good things. The package 
automatically detects (with high accuracy) the format (\ *dialect*\ ) of CSV 
files, thus making it easier to simply point to a CSV file and load it, 
without the need for human inspection. In the future, we hope to solve some of 
the other issues of CSV files too.

CleverCSV is `based on science <https://arxiv.org/abs/1811.11242>`_. We 
investigated thousands of real-world CSV files to find a robust way to 
automatically detect the dialect of a file. This may seem like an easy 
problem, but to a computer a CSV file is simply a long string, and every 
dialect will give you *some* table. In CleverCSV we use a technique based on 
the patterns of the parsed file and the data type of the parsed cells. With 
our method we achieve a 97% accuracy for dialect detection, with a 21% 
improvement on non-standard (\ *messy*\ ) CSV files.

We think this kind of work can be very valuable for working data scientists 
and programmers and we hope that you find CleverCSV useful (if there's a 
problem, please open an issue!) Since the academic world counts citations, 
please **cite CleverCSV if you use the package**. Here's a BibTeX entry you 
can use:

.. code-block:: bib

   @article{van2018wrangling,
       title={Wrangling Messy {CSV} Files by Detecting Row and Type Patterns},
       author={{van den Burg}, G. J. J. and Naz{\'a}bal, A. and Sutton, C.},
       journal={arXiv preprint arXiv:1811.11242},
       year={2018}
   }

And of course, if you like the package please *spread the word!* You can do 
this by Tweeting about it 
(\ `#CleverCSV <https://twitter.com/hashtag/clevercsv>`_\ ) or clicking the ⭐️ `on 
GitHub <https://github.com/alan-turing-institute/CleverCSV>`_\ !

Installation
------------

The package is available on PyPI:

.. code-block:: bash

   $ pip install clevercsv

Usage
-----

CleverCSV consists of a Python library and a command line tool 
(\ ``clevercsv``\ ).

Library
^^^^^^^

We designed CleverCSV to provide a drop-in replacement for the built-in CSV 
module, with some useful functionality added to it. Therefore, if you simply 
want to replace the builtin CSV module with CleverCSV, you only have to add 
one letter:

.. code-block:: python

   import clevercsv

CleverCSV provides an improved version of the dialect sniffer in the CSV 
module, but it also adds some useful wrapper functions. For instance, there's 
a wrapper for loading a CSV file using `Pandas <https://pandas.pydata.org/>`_\ , 
that uses CleverCSV to detect the dialect of the file:

.. code-block:: python

   from clevercsv import csv2df

   df = csv2df("data.csv")

Of course, you can also use the traditional way of loading a CSV file, as in 
the Python CSV module:

.. code-block:: python

   # importing this way makes it easy to port existing code to CleverCsv
   import clevercsv as csv

   with open("data.csv", "r", newline="") as fp:
     # you can use verbose=True to see what CleverCSV does:
     dialect = csv.Sniffer().sniff(fid.read(), verbose=False)
     fp.seek(0)
     reader = csv.reader(fp, dialect)
     rows = list(reader)

That's the basics! If you want more details, you can look at the code of the 
package or the test suite. Documentation will be provided in the future (but a 
lot of the functionality is similar to the CSV package in Python!)

Command-Line Tool
^^^^^^^^^^^^^^^^^

The ``clevercsv`` command line application has a number of handy features to 
make working with CSV files easier. For instance, it can be used to view a CSV 
file on the command line while automatically detecting the dialect. It can 
also generate Python code for importing data from a file with the correct 
dialect. The full help text is as follows:

.. code-block:: text

   CleverCSV version 0.3.1

   USAGE
     clevercsv [-h] [-v] [-V] <command> [<arg1>] ... [<argN>]

   ARGUMENTS
     <command>       The command to execute
     <arg>           The arguments of the command

   GLOBAL OPTIONS
     -h (--help)     Display this help message.
     -v (--verbose)  Enable verbose mode.
     -V (--version)  Display the application version.

   AVAILABLE COMMANDS
     code            Generate Python code for importing the CSV file.
     detect          Detect the dialect of a CSV file
     help            Display the manual of a command
     standardize     Convert a CSV file to one that conforms to RFC-4180.
     view            View the CSV file on the command line using TabView

Each of the commands has further options (for instance, the ``code`` command 
can generate code for importing a Pandas DataFrame). Use
``clevercsv help <command>`` for more information.

Contributors
------------

Code:


* `Gertjan van den Burg <https://gertjan.dev>`_

Scientific work:


* `Gertjan van den Burg <https://gertjan.dev>`_
* `Alfredo Nazabal <https://scholar.google.com/citations?user=IanHvT4AAAAJ>`_
* `Charles Sutton <https://homepages.inf.ed.ac.uk/csutton/>`_

Contributing
------------

If you want to encourage development of CleverCSV, the best thing to do now is 
to *spread the word!*

If you encounter an issue in CleverCSV, please open an issue or submit a pull 
request!

Notes
-----

License: MIT (see LICENSE file).

Copyright (c) 2019 `The Alan Turing Institute <https://turing.ac.uk>`_.