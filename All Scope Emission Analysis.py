#import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


file_path= 'E:/NewDrive/DataScienceProjects/DataSets/ESG Books/Solutions/Cleaned_DataSet.csv'
# Read the CSV file into a DataFrame
df_EDA = pd.read_csv(file_path)


# Assuming your DataFrame is named df
# Columns to analyze
scope_columns = ['Scope 1', 'Scope 2 (location based)', 'Scope 2 (market based)',
                 'Scope 3 (total)', 'Scope 3 (cat 1)', 'Scope 3 (cat 2)',
                 'Scope 3 (cat 3)', 'Scope 3 (cat 4)', 'Scope 3 (cat 5)',
                 'Scope 3 (cat 6)', 'Scope 3 (cat 7)', 'Scope 3 (cat 8)',
                 'Scope 3 (cat 9)', 'Scope 3 (cat 10)', 'Scope 3 (cat 11)',
                 'Scope 3 (cat 12)', 'Scope 3 (cat 13)', 'Scope 3 (cat 14)',
                 'Scope 3 (cat 15)']

# Sum each column individually
sums = df_EDA[scope_columns].sum()

# Find the index of the highest and lowest values
max_index = sums.idxmax()
min_index = sums.idxmin()

# Create a line chart with appealing styling
plt.figure(figsize=(12, 6))
plt.plot(sums.index, sums.values, marker='o', linestyle='-', color='b', label='Sum Value', linewidth=2)

# Highlight the highest and lowest values with markers
plt.scatter(max_index, sums[max_index], color='red', label='Highest Value', s=150, zorder=5)
plt.scatter(min_index, sums[min_index], color='green', label='Lowest Value', s=150, zorder=5)

# Add grid lines
plt.grid(True, linestyle='--', alpha=0.7)

# Set chart title and labels
plt.title('Sum of Emission Values for Each Scope', fontsize=16)
plt.xlabel('Scope Columns', fontsize=12)
plt.ylabel('Emission Sum', fontsize=12)

# Set x-ticks to display all scope column names
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)

# Display the line chart with legend
plt.legend(fontsize=12, loc='upper left')

# Add a legend for the highlighted values
plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Highest Value'),
                    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label='Lowest Value')],
           loc='upper right')

# Show the plot
plt.tight_layout()
plt.show()
