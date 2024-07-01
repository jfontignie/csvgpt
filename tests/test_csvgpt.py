from unittest import TestCase

from csvgpt.csvgpt import CSVGpt


class TestCSVGpt(TestCase):
    def test_run(self):
        gpt = CSVGpt("../resources/sample.csv","../sandbox/out.csv", overwrite=True)
        gpt.run("Answer to the question '$question'")
