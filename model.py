import pandas as pd
from sklearn.cluster import KMeans

def kmeans(df):
    # Select columns suitable for K-means clustering
    selected_columns = ['age', 'balance', 'duration']
    X = df[selected_columns]

    # Initialize KMeans model with k=3
    kmeans = KMeans(n_clusters=3, random_state=42)

    # Fit the model to the data
    kmeans.fit(X)

    # Get the cluster labels
    cluster_labels = kmeans.labels_

    # Count the number of records in each cluster
    cluster_counts = pd.Series(cluster_labels).value_counts().sort_index()

    # Save the cluster counts as a text file
    cluster_counts.to_csv("k.txt", header=False, index=False)
    
    return cluster_counts

# Load the dataset
df = pd.read_csv("Bank_Target_Marketing_Dataset.csv")

# Perform K-means clustering
cluster_counts = kmeans(df)

# Print the cluster counts
print(cluster_counts)