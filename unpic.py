import pickle 
import os

if __name__ == "__main__":

    def unpickle(path):
        obj = None
        if(os.path.exists(path)):
            print(f"Path found - {path}, unpickling...\n")
            with open(path, 'rb') as f:
                obj = pickle.load(f)
        else:
            obj = f"Path - {path} not found..."
        return obj
