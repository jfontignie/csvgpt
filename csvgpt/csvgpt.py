"""
Module providing CSV parsing and answering to questions from chatgpt
"""
import logging
import os.path
from string import Template

import pandas as pd

from csvgpt.chatgpt import ask_chatgpt


class CSVGpt:
    """
    The help class
    """

    def __init__(self, src: str, dst: str, overwrite: bool = False, delimiter: str = ','):
        """
        :param src: source file
        :param dst: destination file
        :param overwrite: overwrite existing file if it already exists
        :param delimiter: the delimiter used in the CSV file
        """
        self.delimiter = delimiter
        self.src = src
        self.dst = dst
        if not os.path.exists(src):
            raise FileNotFoundError(src)
        if not os.path.isfile(src):
            raise FileExistsError(f"'{src}' should be a file")
        if os.path.exists(dst) and not overwrite:
            raise FileExistsError(f"'{dst}' already exists")

    def run(self, prompt: str, intro: str = ""):
        """
        :param prompt: the prompt to ask to chatgpt with $col to templatize
        :param intro: the intro if needed
        :return: nothing but create the file
        """
        df = pd.read_csv(self.src)
        answers = []
        for row in df.values:
            template = Template(prompt)
            substitution = dict(zip(df.columns, row))
            logging.info("Substitution: %s", substitution)
            substitute = template.substitute(substitution)
            answer = ask_chatgpt(substitute, intro)
            logging.info("'%s'->'%s'", substitute, answer)
            answers.append(answer)
        df["chatgpt"] = answers
        df.to_csv(self.dst, index=False)
