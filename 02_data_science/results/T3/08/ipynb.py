import pandas as pd

# Load the dataset
file_path = 'Wholesale customers data.csv'
data = pd.read_csv(file_path)

# Drop the Region column
data = data.drop(columns=['Region'])
data.head()  # Display the first few rows of the modified dataset

# Filter the data for clients that are restaurants, hotels, and cafés (Channel = 2)
filtered_data = data[data['Channel'] == 2].drop(columns=['Channel'])
filtered_data.head()  # Display the first few rows of the filtered dataset

# Normalize the data by computing the proportionate spending per product category
normalized_data = filtered_data.div(filtered_data.sum(axis=1), axis=0)
normalized_data.head()  # Display the first few rows of the normalized dataset

from sklearn.preprocessing import StandardScaler

# Standardize the normalized data
scaler = StandardScaler()
standardized_data = scaler.fit_transform(normalized_data)

# Convert back to DataFrame for easier handling
standardized_data_df = pd.DataFrame(standardized_data, columns=normalized_data.columns)
standardized_data_df.head()  # Display the first few rows of the standardized dataset



from sklearn.preprocessing import StandardScaler

# Standardize the normalized data
scaler = StandardScaler()
standardized_data = scaler.fit_transform(normalized_data)

# Convert back to DataFrame for easier handling
standardized_data_df = pd.DataFrame(standardized_data, columns=normalized_data.columns)
standardized_data_df.head()  # Display the first few rows of the standardized dataset

from sklearn.cluster import KMeans

# Perform K-means clustering with K=4
kmeans = KMeans(n_clusters=4, random_state=42)
clusters = kmeans.fit_predict(standardized_data)

# Add the cluster labels to the standardized data
standardized_data_df['Cluster'] = clusters
standardized_data_df.head()  # Display the first few rows with cluster labels

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
plt.show()  # Display the plot

# Create a summary description for each cluster based on the centroids
cluster_descriptions = {}

for i in range(centroids_df.shape[0]):
    description = f"Cluster {i}: "
    for column in centroids_df.columns:
        spending = centroids_df.loc[i, column]
        description += f"{column} spending is {'high' if spending > 0 else 'low'}; "
    cluster_descriptions[i] = description.strip()

cluster_descriptions  # Display the descriptions for each cluster

