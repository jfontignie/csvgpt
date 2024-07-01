"""
Script test for csvgpt
"""
import logging
from unittest import TestCase

from csvgpt.csvgpt import CSVGpt

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


class TestCSVGpt(TestCase):
    """
    Test class
    """
    def test_run_simple(self):
        """
        Try to answer to colonne $question
        :return: nothing
        """
        gpt = CSVGpt("../resources/sample.csv", "../sandbox/simple.csv", overwrite=True)
        gpt.run("Answer to the question '$question'")

    def test_run_complex(self):
        """
        Try to append to the append question
        :return: nothing
        """
        gpt = CSVGpt("../resources/sample.csv", "../sandbox/complex.csv", overwrite=True)
        gpt.run("concatene '$col1' avec '$col2'",
                "ne répond qu'à la question sans rajouter de texte")
