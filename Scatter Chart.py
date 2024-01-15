#import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

file_path= 'E:/NewDrive/DataScienceProjects/DataSets/ESG Books/Solutions/Cleaned_DataSet.csv'
# Read the CSV file into a DataFrame
df_EDA = pd.read_csv(file_path)

# Code for Scope 3 cat(9) Emission of Highest and Lowest Emitter  Over the Year

df_EDA['year'] = df_EDA['year'].astype(str)

# Filter data for the USA
usa_data = df_EDA[df_EDA['CountryName'] == 'UNITED STATES']

# Aggregate the data for each year by summing up the 'Scope 3 (total)' values
usa_data_aggregated = usa_data.groupby('year').agg({'Scope 3 (cat 9)': 'sum'}).reset_index()

# Create a 3D scatter plot for the USA with aggregated 'Scope 3 (total)' values
fig = px.scatter_3d(usa_data_aggregated, x='year', y='Scope 3 (cat 9)', z='Scope 3 (cat 9)',
                    labels={'Scope 3 (cat 9)': 'Scope 3 (total) Emission', 'year': 'Year'},
                    title='USA CO2e emissions – Downstream Transportation and Distribution Over the Years',
                    color='Scope 3 (cat 9)', size='Scope 3 (cat 9)', opacity=0.7,
                    hover_name='Scope 3 (cat 9)')

# Set axis labels
fig.update_layout(scene=dict(xaxis_title='Year', yaxis_title='Emission in MT', zaxis_title='SUM'))

# Set color scale for better visualization
fig.update_traces(marker=dict(line=dict(width=0.5, color='DarkSlateGray')), selector=dict(mode='markers'))

# Show the plot
fig.show()

# Code for Scope 2 Emission of Highest and Lowest Emitters Over the Year 


df_EDA['year'] = df_EDA['year'].astype(str)

# Filter data for the USA
aus_data = df_EDA[df_EDA['CountryName'] == 'AUSTRALIA']
df_EDA['Scope 2'] = df_EDA['Scope 2 (location based)'] + df_EDA['Scope 2 (market based)']


# Aggregate the data for each year by summing up the 'Scope 3 (total)' values
aus_data_aggregated = aus_data.groupby('year').agg({'Scope 2': 'sum'}).reset_index()

# Create a 3D scatter plot for the USA with aggregated 'Scope 3 (total)' values
fig = px.scatter_3d(aus_data_aggregated, x='year', y='Scope 2', z='Scope 2',
                    labels={'Scope 2': 'Scope 2 (total) Emission', 'year': 'Year'},
                    title='AUSTRALIA CO2e emissions(Location+Market) Over the Years',
                    color='Scope 2', size='Scope 2', opacity=0.7,
                    hover_name='Scope 2')

# Set axis labels
fig.update_layout(scene=dict(xaxis_title='Year', yaxis_title='Emission in MT', zaxis_title='SUM'))

# Set color scale for better visualization
fig.update_traces(marker=dict(line=dict(width=0.5, color='DarkSlateGray')), selector=dict(mode='markers'))

# Show the plot
fig.show()
