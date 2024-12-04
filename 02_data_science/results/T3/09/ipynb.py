import pandas as pd

# Load the dataset
file_path = './wholesale_customers/Wholesale customers data.csv'
data = pd.read_csv(file_path)

# Drop the Region column
data = data.drop(columns=['Region'])

# Display the first few rows of the modified dataset
data.head()

# Filter the data for clients that are restaurants, hotels, and cafés (Channel 1 and 2)
filtered_data = data[data['Channel'].isin([1, 2])]

# Display the first few rows of the filtered dataset
filtered_data.head()

# Normalize the data by computing the proportionate spending per product category
normalized_data = filtered_data.copy()
normalized_data.iloc[:, 1:] = normalized_data.iloc[:, 1:].div(normalized_data.iloc[:, 1:].sum(axis=1), axis=0)

# Display the first few rows of the normalized dataset
normalized_data.head()

from sklearn.preprocessing import StandardScaler

# Standardize the data
scaler = StandardScaler()
standardized_data = normalized_data.copy()
standardized_data.iloc[:, 1:] = scaler.fit_transform(standardized_data.iloc[:, 1:])

# Display the first few rows of the standardized dataset
standardized_data.head()



from sklearn.preprocessing import StandardScaler

# Standardize the data
scaler = StandardScaler()
standardized_data = normalized_data.copy()
standardized_data.iloc[:, 1:] = scaler.fit_transform(standardized_data.iloc[:, 1:])

# Display the first few rows of the standardized dataset
standardized_data.head()

from sklearn.cluster import KMeans

# Use K-means to cluster the customers into K = 4 groups
kmeans = KMeans(n_clusters=4, random_state=42)
standardized_data['Cluster'] = kmeans.fit_predict(standardized_data.iloc[:, 1:])

# Display the first few rows of the dataset with cluster labels
standardized_data.head()

import matplotlib.pyplot as plt
import numpy as np

# Calculate the centroids
centroids = kmeans.cluster_centers_

# Create a DataFrame for centroids
centroids_df = pd.DataFrame(centroids, columns=standardized_data.columns[1:-1])

# Plot the centroids
plt.figure(figsize=(10, 6))
for i in range(centroids_df.shape[0]):
    plt.plot(centroids_df.columns, centroids_df.iloc[i], marker='o', label=f'Cluster {i}')
plt.title('Cluster Centroids')
plt.xlabel('Product Categories')
plt.ylabel('Standardized Spending')
plt.legend()
plt.grid()
plt.show()

# Create a summary description for each cluster based on the centroids
cluster_descriptions = {}

for i in range(centroids_df.shape[0]):
    cluster_descriptions[i] = centroids_df.iloc[i].to_dict()

cluster_descriptions

