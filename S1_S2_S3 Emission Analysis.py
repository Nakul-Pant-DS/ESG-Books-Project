#import necessary Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


file_path= 'E:/NewDrive/DataScienceProjects/DataSets/ESG Books/Solutions/Cleaned_DataSet.csv'
# Read the CSV file into a DataFrame
df_EDA = pd.read_csv(file_path)


# Create a new column 'Scope 2' by summing 'Scope 2 (location based)' and 'Scope 2 (market based)'
df_EDA['Scope 2'] = df_EDA['Scope 2 (location based)'] + df_EDA['Scope 2 (market based)']

# Columns to analyze
scope_columns = ['Scope 1', 'Scope 2', 'Scope 3 (total)']

# Sum each column individually
sums = df_EDA[scope_columns].sum()

# Create a line chart with appealing styling
plt.figure(figsize=(12, 6))

# Plot the sums for each category
plt.plot(sums.index, sums.values, marker='o', linestyle='-', color='b', label='Sum Value', linewidth=2, markersize=8)

# Highlight the highest and lowest values with markers
max_index = sums.idxmax()
min_index = sums.idxmin()
plt.scatter(max_index, sums[max_index], color='red', label=f'Highest Value ({max_index})', s=150, zorder=5)
plt.scatter(min_index, sums[min_index], color='green', label=f'Lowest Value ({min_index})', s=150, zorder=5)

# Add grid lines
plt.grid(True, linestyle='--', alpha=0.7)

# Set chart title and labels
plt.title('Sum of Emission Values for Each Scope', fontsize=16)
plt.xlabel('Scope Categories', fontsize=12)
plt.ylabel('Emission Value', fontsize=12)

# Set x-ticks to display all scope categories
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)

# Display the line chart with legend
plt.legend(fontsize=10, loc='upper left')

# Add a legend for the highlighted values
plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Highest Value'),
                    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label='Lowest Value')],
           loc='upper right')

# Show the plot
plt.tight_layout()
plt.show()
