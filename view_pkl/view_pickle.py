import pickle
import pandas as pd

import sys
sys.path.append("/Users/chenxy/Code/VS Code WorkSpace/SREP/SREPSim/srep_simulator/srep.py")

# Specify the path to the .pickle file
file_path = "view_pkl/sim_experiments_52bc1d85.pickle"

data = pd.read_pickle(file_path)

# # Load the data from the .pickle file
# with open(file_path, "rb") as file:
#     data = pickle.load(file)

# View the loaded data
print("Contents of the .pickle file:")
print(data)