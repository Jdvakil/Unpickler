import pickle 
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file-name", help="file name to be unpickled")
args = parser.parse_args()
print(f"Config: {args}")