import pickle 
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file-name", help="file name to be unpickled")
args = parser.parse_args()
cwd = os.getcwd()
path = os.path.join(cwd, args.file_name)

if (os.path.exists(path)):
    print(path)
else:
    print("Path not found...")
