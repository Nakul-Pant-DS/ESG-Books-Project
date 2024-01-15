#Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


file_path= 'E:/NewDrive/DataScienceProjects/DataSets/ESG Books/Solutions/Cleaned_DataSet.csv'
# Read the CSV file into a DataFrame
df_EDA = pd.read_csv(file_path)

df_EDA['Scope 2'] = df_EDA['Scope 2 (location based)'] + df_EDA['Scope 2 (market based)']

# Group by 'CountryName' and sum the 'Scope 2' values for each country
sum_scope_by_country = df_EDA.groupby('CountryName')['Scope 2'].sum()

# Find the country with the highest and lowest values
max_country = sum_scope_by_country.idxmax()
min_country = sum_scope_by_country.idxmin()

# Plotting
plt.figure(figsize=(10, 6))
ax = sum_scope_by_country.plot(kind='bar', color='grey')

# Highlighting bars with highest and lowest values
ax.bar(max_country, sum_scope_by_country.loc[max_country], color='orange', label='Highest Value')
ax.bar(min_country, sum_scope_by_country.loc[min_country], color='green', label='Lowest Value')

# Adding labels and title
plt.xlabel('Country')
plt.ylabel('Emission Value(MT)')
plt.title('Scope 2 CO2e Emissions(Location + Market) VS Countries')

# Adding legend
plt.legend()

# Displaying the plot
plt.show()
