#import important libraries
import pandas as pd

file_path = 'E:/NewDrive/DataScienceProjects/DataSets/ESG Books/Solutions/Cleaned_DataSet.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# List of columns to sum
scope_columns = [
    'Scope 1',
    'Scope 2 (location based)',
    'Scope 2 (market based)',
    'Scope 3 (total)',
    'Scope 3 (cat 1)',
    'Scope 3 (cat 2)',
    'Scope 3 (cat 3)',
    'Scope 3 (cat 4)',
    'Scope 3 (cat 5)',
    'Scope 3 (cat 6)',
    'Scope 3 (cat 7)',
    'Scope 3 (cat 8)',
    'Scope 3 (cat 9)',
    'Scope 3 (cat 10)',
    'Scope 3 (cat 11)',
    'Scope 3 (cat 12)',
    'Scope 3 (cat 13)',
    'Scope 3 (cat 14)',
    'Scope 3 (cat 15)'
]

# Create a new column 'Total_Scope' with the sum of all specified columns
df['Total_Scope'] = df[scope_columns].sum(axis=1)

# Group by 'CountryName' and sum the 'Total_Scope' column
result_df = df.groupby('CountryName')['Total_Scope'].sum().reset_index()

# Sort the result DataFrame in descending order by 'Total_Scope'
result_df_sorted = result_df.sort_values(by='Total_Scope', ascending=False)

# Print the sorted result
print(result_df_sorted)

# Create Folium Map

import folium
from folium.plugins import MarkerCluster

# Replace the following coordinates with the actual latitude and longitude values for each country
coordinates = {
    'UNITED STATES': (37.0902, 95.7129),
    'INDIA': (20.5937, 78.9629),
    'JAPAN': (36.2048, 138.2529),
    'CANADA': (56.1304, 106.3468),
    'UNITED KINGDOM': (55.3781, 3.4360),
    'CHINA': (35.8617, 104.1954),
    'CAYMAN ISLANDS': (19.3133, 81.2546),
}

# Assuming 'result_df' contains the 'CountryName' and 'Total_Scope' columns

# Sort the DataFrame by 'Total_Scope' in descending order
result_df_sorted = result_df.sort_values(by='Total_Scope', ascending=False)

# Get the top 5 countries
top_5_countries = result_df_sorted.head(5)

# Create a base map
map_center = [20, 0]  # Adjust the center as needed
my_map = folium.Map(location=map_center, zoom_start=2)

# Marker cluster for all countries
marker_cluster_all = MarkerCluster().add_to(my_map)

# Add markers for all countries
for index, row in result_df.iterrows():
    country_coordinates = coordinates.get(row['CountryName'], (0, 0))
    folium.Marker(
        location=country_coordinates,
        popup=f"{row['CountryName']}: {row['Total_Scope']}",
        icon=folium.Icon(color='blue')
    ).add_to(marker_cluster_all)

# Marker cluster for top 5 countries
marker_cluster_top_5 = MarkerCluster().add_to(my_map)

# Add markers for the top 5 countries with a different color
for index, row in top_5_countries.iterrows():
    country_coordinates = coordinates.get(row['CountryName'], (0, 0))
    folium.Marker(
        location=country_coordinates,
        popup=f"{row['CountryName']}: {row['Total_Scope']}",
        icon=folium.Icon(color='red')
    ).add_to(marker_cluster_top_5)

# Add title
title_html = """
    <h3 align="center" style="font-size:16px"><b>Top Five Countries With Highest Emission</b></h3>
    """
my_map.get_root().html.add_child(folium.Element(title_html))

# Display the map
my_map.save('E:/NewDrive/DataScienceProjects/DataSets/ESG Books/Solutions/Top_5_Emitter_Countries_MAP.html')  # Save the map as an HTML file
