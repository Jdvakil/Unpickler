import unpic
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--path", default=os.getcwd(), help="Path of the file with the filename")
args = parser.parse_args()

print(unpic.unpickle(args.path))