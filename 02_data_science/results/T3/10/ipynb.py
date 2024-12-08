import pandas as pd

# Load the dataset
file_path = './wholesale_customers/Wholesale customers data.csv'
data = pd.read_csv(file_path)

# Drop the Region column
data = data.drop(columns=['Region'])

# Display the first few rows of the modified DataFrame
data.head()

# Filter the data for clients that are restaurants, hotels, and cafés (Channel = 2)
filtered_data = data[data['Channel'] == 2].reset_index(drop=True)

# Display the first few rows of the filtered DataFrame
filtered_data.head()

# Normalize the data by computing the proportionate spending per product category
normalized_data = filtered_data.copy()
normalized_data.iloc[:, 1:] = normalized_data.iloc[:, 1:].div(normalized_data.iloc[:, 1:].sum(axis=1), axis=0)

# Display the first few rows of the normalized DataFrame
normalized_data.head()

from sklearn.preprocessing import StandardScaler

# Standardize the data
scaler = StandardScaler()
standardized_data = normalized_data.copy()
standardized_data.iloc[:, 1:] = scaler.fit_transform(normalized_data.iloc[:, 1:])

# Display the first few rows of the standardized DataFrame
standardized_data.head()



# Standardize the data
scaler = StandardScaler()
standardized_data = normalized_data.copy()
standardized_data.iloc[:, 1:] = scaler.fit_transform(normalized_data.iloc[:, 1:])

# Display the first few rows of the standardized DataFrame
standardized_data.head()

import pandas as pd
from sklearn.preprocessing import StandardScaler

# Re-load the dataset
file_path = './wholesale_customers/Wholesale customers data.csv'
data = pd.read_csv(file_path)

# Drop the Region column
data = data.drop(columns=['Region'])

# Filter the data for clients that are restaurants, hotels, and cafés (Channel = 2)
filtered_data = data[data['Channel'] == 2].reset_index(drop=True)

# Normalize the data
normalized_data = filtered_data.copy()
normalized_data.iloc[:, 1:] = normalized_data.iloc[:, 1:].div(normalized_data.iloc[:, 1:].sum(axis=1), axis=0)

# Standardize the data
scaler = StandardScaler()
standardized_data = normalized_data.copy()
standardized_data.iloc[:, 1:] = scaler.fit_transform(normalized_data.iloc[:, 1:])

# Display the first few rows of the standardized DataFrame
standardized_data.head()

from sklearn.cluster import KMeans

# Perform K-means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
standardized_data['Cluster'] = kmeans.fit_predict(standardized_data.iloc[:, 1:])

# Display the first few rows of the DataFrame with cluster assignments
standardized_data.head()

import matplotlib.pyplot as plt
import numpy as np

# Get the cluster centroids
centroids = kmeans.cluster_centers_

# Create a DataFrame for centroids
centroids_df = pd.DataFrame(centroids, columns=standardized_data.columns[1:-1])

# Plot the centroids
plt.figure(figsize=(10, 6))
for i, column in enumerate(centroids_df.columns):
    plt.plot(np.arange(centroids_df.shape[0]), centroids_df[column], marker='o', label=column)

plt.title('Cluster Centroids')
plt.xlabel('Cluster')
plt.ylabel('Standardized Spending')
plt.xticks(np.arange(centroids_df.shape[0]), ['Cluster 0', 'Cluster 1', 'Cluster 2', 'Cluster 3'])
plt.legend()
plt.grid()
plt.show()

# Display the centroids DataFrame
centroids_df

# Create descriptions based on the centroids
descriptions = []
for index, row in centroids_df.iterrows():
    description = f"Cluster {index}: "
    if row['Fresh'] > 0:
        description += "High spending on Fresh. "
    else:
        description += "Low spending on Fresh. "
    
    if row['Milk'] > 0:
        description += "High spending on Milk. "
    else:
        description += "Low spending on Milk. "
    
    if row['Grocery'] > 0:
        description += "High spending on Grocery. "
    else:
        description += "Low spending on Grocery. "
    
    if row['Frozen'] > 0:
        description += "High spending on Frozen. "
    else:
        description += "Low spending on Frozen. "
    
    if row['Detergents_Paper'] > 0:
        description += "High spending on Detergents and Paper. "
    else:
        description += "Low spending on Detergents and Paper. "
    
    if row['Delicassen'] > 0:
        description += "High spending on Delicassen."
    else:
        description += "Low spending on Delicassen."
    
    descriptions.append(description)

descriptions

