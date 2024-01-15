#import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


file_path= 'E:/NewDrive/DataScienceProjects/DataSets/ESG Books/Solutions/Cleaned_DataSet.csv'
# Read the CSV file into a DataFrame
df_EDA = pd.read_csv(file_path)

#Group by 'CountryName' and sum the 'Scope1' values for each country
sum_scope_by_country = df_EDA.groupby('CountryName')['Scope 3 (cat 9)'].sum()

# Find the country with the highest and lowest values
max_country = sum_scope_by_country.idxmax()
min_country = sum_scope_by_country.idxmin()

# Plotting
ax = sum_scope_by_country.plot(kind='bar', color='skyblue')

# Highlighting bars with highest and lowest values
ax.patches[sum_scope_by_country.index.get_loc(max_country)].set_facecolor('orange')  # Highlight max
ax.patches[sum_scope_by_country.index.get_loc(min_country)].set_facecolor('green')  # Highlight min

# Adding labels and title
plt.xlabel('Country')
plt.ylabel('Emission Value(MT)')
plt.title('CO2e Emissions-Downstream Transportation and Distribution Vs Country')

# Displaying the plot
plt.show()
