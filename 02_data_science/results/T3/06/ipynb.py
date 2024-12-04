import pandas as pd
import zipfile
import requests
import os

# Download the dataset
url = "https://archive.ics.uci.edu/static/public/292/wholesale+customers.zip"
response = requests.get(url)

# Save the zip file
zip_file_path = "wholesale_customers.zip"
with open(zip_file_path, "wb") as f:
    f.write(response.content)

# Extract the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(".")

# Load the dataset into a DataFrame
data = pd.read_csv("Wholesale customers data.csv")

# Drop the Region column
data = data.drop(columns=["Region"])
data.head()

# Filter the data for clients that are restaurants, hotels, and cafés (Foodservice)
filtered_data = data[data["Channel"] == 2].drop(columns=["Channel"])
filtered_data.head()

# Normalize the data by computing the proportionate spending per product category
normalized_data = filtered_data.div(filtered_data.sum(axis=1), axis=0)
normalized_data.head()

from sklearn.preprocessing import StandardScaler

# Standardize the data
scaler = StandardScaler()
standardized_data = scaler.fit_transform(normalized_data)
standardized_data_df = pd.DataFrame(standardized_data, columns=normalized_data.columns)
standardized_data_df.head()



from sklearn.preprocessing import StandardScaler

# Standardize the data
scaler = StandardScaler()
standardized_data = scaler.fit_transform(normalized_data)
standardized_data_df = pd.DataFrame(standardized_data, columns=normalized_data.columns)
standardized_data_df.head()

from sklearn.cluster import KMeans

# Use K-means to cluster the customers into K = 4 groups
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(standardized_data)

# Add the cluster labels to the standardized data
standardized_data_df['Cluster'] = kmeans.labels_
standardized_data_df.head()

import matplotlib.pyplot as plt
import seaborn as sns

# Calculate the centroids
centroids = kmeans.cluster_centers_

# Create a DataFrame for centroids
centroids_df = pd.DataFrame(centroids, columns=normalized_data.columns)

# Plot the centroids
plt.figure(figsize=(10, 6))
sns.barplot(data=centroids_df)
plt.title('Cluster Centroids')
plt.xlabel('Product Categories')
plt.ylabel('Standardized Spending')
plt.xticks(rotation=45)
plt.legend(title='Cluster', labels=[f'Cluster {i}' for i in range(centroids_df.shape[0])])
plt.show()

# Create descriptions based on the cluster centroids
descriptions = {}

for i in range(centroids_df.shape[0]):
    descriptions[f'Cluster {i}'] = centroids_df.iloc[i].to_dict()

descriptions

