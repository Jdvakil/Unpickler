import pickle 
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file-name", help="file name to be unpickled")
parser.add_argument("--path", default=os.getcwd(), help="Path of the file without the filename")
args = parser.parse_args()
cwd = args.path
path = os.path.join(cwd, args.file_name)

if (os.path.exists(path)): 
    print(f"Path - {path}\n")
    with open(path, 'rb') as f:
        print(pickle.load(f))

else:
    print("Path not found...")
