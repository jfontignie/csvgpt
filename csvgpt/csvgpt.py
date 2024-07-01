"""
Module providing CSV parsing and answering to questions from chatgpt
"""
import csv
import logging
import os.path
from string import Template

from csvgpt.chatgpt import ask_chatgpt


class CSVGpt:
    def __init__(self, src: str, dst: str, overwrite: bool=False, delimiter: str= ','):
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
        answers = []
        with open(self.src, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            logging.info(f"Header: {header}")
            template = Template(prompt)

            for row in reader:
                substitution = {}
                for i, col in enumerate(header):
                    substitution[col] = row[i]

                logging.info(f"Substitution: {substitution}")
                substitute = template.substitute(substitution)
                answer = ask_chatgpt(substitute, intro)
                logging.info(f"'{substitute}'->'{answer}'")

                answers.append(answer)

        with open(self.dst, 'w', newline='') as csvfile:
            for answer in answers:
                csvfile.write(answer)
                csvfile.write('\n')




