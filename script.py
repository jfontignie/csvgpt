"""
Module providing the command line of csvhpt
"""
import argparse
import logging

from csvgpt.csvgpt import CSVGpt

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

parser = argparse.ArgumentParser(description='Parse a csv file and asks chatgpt about it')

parser.add_argument('--csv', help='CSV file to read', required=True)
parser.add_argument('--output', help='CSV file to write', required=True)
parser.add_argument('--overwrite', help='Override the file', required=False, action='store_true')
parser.add_argument('--intro', help='Introduction to share with GPT', required=False,default="")
parser.add_argument('--prompt', help="Prompt query to perform. Column name starts with $. "
                                     "For example: Answer to the question $question", required=True)
parser.add_argument("--delimiter", help="Sets the delimiter",required=False,default=",")

args = parser.parse_args()
logging.info(f"Prompt is: {args.prompt}")

csv = CSVGpt(args.csv,args.output, args.overwrite, args.delimiter)
csv.run(args.prompt, args.intro)
