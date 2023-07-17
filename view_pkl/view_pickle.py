import pickle
import pandas as pd


# Specify the path to the .pickle file
file_path = "view_pkl/10_10_100(1).pickle"

# data = pd.read_pickle(file_path)

# Load the data from the .pickle file
with open(file_path, "rb") as file:
    data = pickle.load(file)

# View the loaded data
print("Contents of the .pickle file:")
print(data)