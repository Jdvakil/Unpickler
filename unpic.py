import pickle 
import os
#Add parser later
def unpic(path):
    obj = None
    with open(path, 'rb') as f:
        obj = pickle.load(f)
    return obj

dirpath = os.getcwd()
name = 'traj_rgbd_1.pkl'
path = os.path.join(dirpath, name)

print(unpic(path))