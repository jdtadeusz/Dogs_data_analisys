import pandas as pd

# Reading the original file dogs.csv
b = pd.read_csv("../Data/InputData/dogs.csv", sep=';')

# Changing the format of a birthday date to US
b["Date of Birth"] = pd.to_datetime(b["Date of Birth"], format='%d.%m.%Y', errors='coerce')

# Deleting the unnecessary rows
new_b = b.dropna()

# Deleting the unnecessary columns 
new_b = new_b.drop(columns=['Color'], errors='ignore')

# Adding a new column "Age"
today = pd.to_datetime('today')
new_b.loc[:, 'Age'] = today.year - new_b['Date of Birth'].dt.year

# Saving a new file
new_b.to_csv("../Data/IntermediateData/dogs_clean.csv", index=False, sep=";")