
Changelog
=========

Version 0.4.2
-------------


* Fix a failing build due to dependency version mismatch

Version 0.4.1
-------------


* Allow underscore in alphanumeric strings
* Update unix path regular expression
* Add more integration tests and log detection method

Version 0.4.0
-------------


* Update URL regular expression and add unit tests
* Add IPv4 type detection
* Add tie-breaker for combined quotechar and escapechar ties

Version 0.3.7
-------------


* Bugfix for console script ``code`` command
* Update readme

Version 0.3.6
-------------


* Cleanly handle failure to detect dialect in console application
* Remove any (partial) support for Python 2

Version 0.3.5
-------------


* Remove Python parser - this speeds up file reading and tie breaking

Version 0.3.4
-------------


* Ensure the C parser is used in the ``reader``.
* Update integration tests to improve error handling
* Readme updates

Version 0.3.3
-------------


* Ensure detected encoding is in the generated Python code for the ``clevercsv 
  code`` command.
* Ensure encoding is detected in ``wrappers.detect_dialect``.
* Bugfix in integration test
* Expand readme

Version 0.3.2
-------------


* Add documentation on `Read the Docs <https://clevercsv.readthedocs.io/>`_
* Use requirements.txt file for dependencies when packaging

Version 0.3.1
-------------


* Add help description to each CLI command
* Update README
* Add transpose flag for ``standardize`` and ``view`` commands

Version 0.3.0
-------------


* Rewrite console application using Cleo
* Add unit tests for console application
* Add ``detect_dialect`` wrapper function
* Add support for "unix_path" data type in type detection
* Add ``encoding`` and ``num_chars`` options to ``read_csv`` wrapper
* Add ``-p/--pandas`` flag to ``code`` command to generate Pandas output.

Version 0.2.5
-------------


* Rename ``read_as_lol`` to ``read_csv``.

Version 0.2.4
-------------


* Allow setting the number of characters to read
* Simplify printing of skipped potential dialects

Version 0.2.3
-------------


* Add ``read_as_lol`` wrapper function.

Version 0.2.2
-------------


* Add ``code`` command to ``clevercsv`` command line program.

Version 0.2.1
-------------


* Bugfix to update executable to new name

Version 0.2.0
-------------


* Rename package to clevercsv
