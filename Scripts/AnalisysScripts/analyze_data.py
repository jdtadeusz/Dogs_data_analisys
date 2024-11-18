import pandas as pd 
import matplotlib as plt

# Reading the file 
dogs_clean = pd.read_csv("./Data/IntermediateData/dogs_clean.csv")

# Grouping the file's columns 
breed_grouped = dogs_clean.groupby("Breed")[["Weight (kg), Height (cm)"]].mean()

# Saving the grouped file
breed_grouped.to_csv("./Data/AnalysisData/averageWeight.csv")

# Printing the result to the txt file
heaviest_one = breed_grouped["Weight (kg)"].idxmax()
heaviest_weight = breed_grouped["Weight (kg)"].max()

result = f"Heaviest breed is {heaviest_one} with an average weight of {heaviest_weight} kg."

print(result)

# Overwriting the file with the result
with open('./Output/Results/HeaviestBreed.txt', 'w') as f:
    f.write(result)


# Creating a visualization plot 
plt.figure(figsize=(8, 4))
plt.bar(breed_grouped.index, breed_grouped['Weight (kg)'], color='orange')
plt.title('Average Weight')
plt.xlabel('Breed')
plt.ylabel('Average Weight (kg)')

# Saving the plot
plt.savefig("AverageWeightPlot")