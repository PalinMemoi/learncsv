# -*- coding: utf-8 -*-


from cleo import Command

from clevercsv.wrappers import detect_dialect
from ._utils import parse_int


class DetectCommand(Command):
    """
    Detect the dialect of a CSV file

    detect
        { path : The path to the CSV file }
        { --e|encoding= : Set the encoding of the CSV file }
        { --n|num-chars= : Limit the number of characters to read for 
        detection. This will speed up detection but may reduce accuracy. }
    """

    def handle(self):
        verbose = self.io.verbosity > 0
        num_chars = parse_int(self.option("num-chars"), "num-chars")
        dialect = detect_dialect(
            self.argument("path"),
            num_chars=num_chars,
            encoding=self.option("encoding"),
            verbose=verbose,
        )
        self.line(str(dialect))