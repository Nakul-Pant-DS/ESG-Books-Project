#import important libraries
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
plt.title('CO2e Emissions-Downstream Transportation and Tistribution Vs Country')

# Displaying the plot
plt.show()


#Group by 'CountryName' and sum the 'Scope1' values for each country
sum_scope1_by_country = df_EDA.groupby('CountryName')['Scope 3 (total)'].sum()

# Find the country with the highest and lowest values
max_country = sum_scope1_by_country.idxmax()
min_country = sum_scope1_by_country.idxmin()

# Plotting
ax = sum_scope1_by_country.plot(kind='bar', color='skyblue')

# Highlighting bars with highest and lowest values
ax.patches[sum_scope1_by_country.index.get_loc(max_country)].set_facecolor('orange')  # Highlight max
ax.patches[sum_scope1_by_country.index.get_loc(min_country)].set_facecolor('green')  # Highlight min

# Adding labels and title
plt.xlabel('Country')
plt.ylabel('Sum of Scope 3')
plt.title('Sum of Scope 3 by Country')

# Displaying the plot
plt.show()



# Group by country and sum the specified columns
grouped_data = df_EDA.groupby('CountryName')[['Scope 1', 'Scope 2 (location based)', 'Scope 2 (market based)',
                                           'Scope 3 (total)', 'Scope 3 (cat 1)', 'Scope 3 (cat 2)',
                                           'Scope 3 (cat 3)', 'Scope 3 (cat 4)', 'Scope 3 (cat 5)',
                                           'Scope 3 (cat 6)', 'Scope 3 (cat 7)', 'Scope 3 (cat 8)',
                                           'Scope 3 (cat 9)', 'Scope 3 (cat 10)', 'Scope 3 (cat 11)',
                                           'Scope 3 (cat 12)', 'Scope 3 (cat 13)', 'Scope 3 (cat 14)',
                                           'Scope 3 (cat 15)']].sum()

# Calculate the total emissions for each country
grouped_data['Total Emissions'] = grouped_data.sum(axis=1)

# Sort by total emissions and select the top emitters
top_emitters = grouped_data.sort_values(by='Total Emissions', ascending=False).head(10)

# Plot the bar chart
top_emitters[['Scope 1', 'Scope 2 (location based)', 'Scope 2 (market based)',
              'Scope 3 (total)']].plot(kind='bar', stacked=True)
plt.title('Top 10 Emitter Countries')
plt.xlabel('Country')
plt.ylabel('Emission Value')
plt.legend(title='Emission Type', loc='upper right')
plt.show()
