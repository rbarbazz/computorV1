import sys
import argparse
import re

def get_input():
	parser = argparse.ArgumentParser()
	parser.add_argument('equation', help='Polynomial equation to be solved')
	return parser.parse_args().equation

def format_input(raw_input):
	return re.sub(r'\s+', '', raw_input)

raw_input = get_input()
equation = format_input(raw_input)
print(equation)