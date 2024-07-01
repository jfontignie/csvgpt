"""
Module providing CSV parsing and answering to questions from chatgpt
"""
import csv
import logging
import os.path
from string import Template

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
        with open(self.dst, 'w', newline='',encoding="utf-8") as dst_file:

            with open(self.src, 'r', newline='',encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader)
                logging.info("Header: %s",header)
                template = Template(prompt)

                for row in reader:
                    substitution = {}
                    for i, col in enumerate(header):
                        substitution[col] = row[i]

                    logging.info(f"Substitution: {substitution}")
                    substitute = template.substitute(substitution)
                    answer = ask_chatgpt(substitute, intro)
                    logging.info(f"'{substitute}'->'{answer}'")

                    dst_file.write(answer)
                    dst_file.write("\n")
