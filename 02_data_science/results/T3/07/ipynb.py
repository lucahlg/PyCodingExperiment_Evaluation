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

# Filter the data for clients that are restaurants, hotels, and cafés (Channel 2)
filtered_data = data[data['Channel'] == 2]
filtered_data.head()

# Normalize the data by computing the proportionate spending per product category
normalized_data = filtered_data.copy()
normalized_data.iloc[:, 1:] = normalized_data.iloc[:, 1:].div(normalized_data.iloc[:, 1:].sum(axis=1), axis=0)

normalized_data.head()

from sklearn.preprocessing import StandardScaler

# Standardize the data
scaler = StandardScaler()
standardized_data = normalized_data.copy()
standardized_data.iloc[:, 1:] = scaler.fit_transform(normalized_data.iloc[:, 1:])

standardized_data.head()



# Standardize the data
scaler = StandardScaler()
standardized_data.iloc[:, 1:] = scaler.fit_transform(normalized_data.iloc[:, 1:])

standardized_data.head()

import pandas as pd
from sklearn.preprocessing import StandardScaler

# Re-load the filtered and normalized data
data = pd.read_csv("Wholesale customers data.csv")
filtered_data = data[data['Channel'] == 2]
normalized_data = filtered_data.copy()
normalized_data.iloc[:, 1:] = normalized_data.iloc[:, 1:].div(normalized_data.iloc[:, 1:].sum(axis=1), axis=0)

# Standardize the data
scaler = StandardScaler()
standardized_data = normalized_data.copy()
standardized_data.iloc[:, 1:] = scaler.fit_transform(normalized_data.iloc[:, 1:])

standardized_data.head()

from sklearn.cluster import KMeans

# Perform K-means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
standardized_data['Cluster'] = kmeans.fit_predict(standardized_data.iloc[:, 1:])

standardized_data.head()

import matplotlib.pyplot as plt

# Get the cluster centroids
centroids = kmeans.cluster_centers_

# Create a DataFrame for centroids
centroids_df = pd.DataFrame(centroids, columns=standardized_data.columns[1:-1])
centroids_df.index = [f'Cluster {i}' for i in range(centroids_df.shape[0])]

# Plot the centroids
centroids_df.plot(kind='bar', figsize=(12, 6))
plt.title('Cluster Centroids')
plt.ylabel('Standardized Spending')
plt.xlabel('Clusters')
plt.xticks(rotation=0)
plt.legend(title='Product Categories')
plt.show()

# Analyze the spending patterns for each cluster
cluster_descriptions = standardized_data.groupby('Cluster').mean()

cluster_descriptions

