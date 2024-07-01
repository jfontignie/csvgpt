import logging
from unittest import TestCase

from csvgpt.csvgpt import CSVGpt

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

class TestCSVGpt(TestCase):
    def test_run_simple(self):
        gpt = CSVGpt("../resources/sample.csv","../sandbox/out.csv", overwrite=True)
        gpt.run("Answer to the question '$question'")

    def test_run_complex(self):
        gpt = CSVGpt("../resources/sample.csv","../sandbox/out.csv", overwrite=True)
        gpt.run("concatene $col1 avec $col2")
