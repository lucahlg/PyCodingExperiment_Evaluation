import pandas as pd

# Load the dataset
file_path = 'wholesale_customers/Wholesale customers data.csv'
data = pd.read_csv(file_path)

# Drop the Region column
data = data.drop(columns=['Region'])

# Display the first few rows of the dataset to verify
data.head()

# Filter the data for clients that are restaurants, hotels, and cafés
filtered_data = data[data['Channel'] == 1]

# Drop the Channel column as it is no longer needed
filtered_data = filtered_data.drop(columns=['Channel'])

# Display the first few rows of the filtered dataset to verify
filtered_data.head()

# Normalize the data by computing the proportionate spending per product category
normalized_data = filtered_data.div(filtered_data.sum(axis=1), axis=0)

# Display the first few rows of the normalized dataset to verify
normalized_data.head()

from sklearn.preprocessing import StandardScaler

# Standardize the data
scaler = StandardScaler()
standardized_data = scaler.fit_transform(normalized_data)

# Convert the standardized data back to a DataFrame
standardized_data = pd.DataFrame(standardized_data, columns=normalized_data.columns)

# Display the first few rows of the standardized dataset to verify
standardized_data.head()



from sklearn.preprocessing import StandardScaler

# Standardize the data
scaler = StandardScaler()
standardized_data = scaler.fit_transform(normalized_data)

# Convert the standardized data back to a DataFrame
standardized_data = pd.DataFrame(standardized_data, columns=normalized_data.columns)

# Display the first few rows of the standardized dataset to verify
standardized_data.head()

from sklearn.cluster import KMeans

# Use K-means to cluster the data into 4 groups
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(standardized_data)

# Get the cluster labels
cluster_labels = kmeans.labels_

# Add the cluster labels to the standardized data
standardized_data['Cluster'] = cluster_labels

# Display the first few rows of the dataset with cluster labels to verify
standardized_data.head()

import matplotlib.pyplot as plt
import seaborn as sns

# Get the cluster centroids
centroids = kmeans.cluster_centers_

# Convert the centroids to a DataFrame
centroids_df = pd.DataFrame(centroids, columns=standardized_data.columns[:-1])

# Print the cluster centroids
print(centroids_df)

# Visualize the cluster centroids
plt.figure(figsize=(10, 6))
sns.heatmap(centroids_df, annot=True, cmap='coolwarm', xticklabels=standardized_data.columns[:-1])
plt.title('Cluster Centroids')
plt.show()

