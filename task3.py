import pandas as pd
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt
# Provide the correct path to the file using a raw string
file_path = r"C:\Users\hp\Downloads\customer_segmentation_dataset.xlsx"
df = pd.read_excel(file_path)

# Display the first few rows of the dataset to inspect it
print(df.head())

# Convert categorical variables to numerical values
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
df['Membership'] = df['Membership'].map({'No': 0, 'Yes': 1})

# Select features for clustering
features = ['Age', 'Gender', 'Annual Income', 'Spending Score', 
            'Purchase Frequency', 'Average Purchase Value', 'Total Expenditure', 'Membership']

# Normalize the data
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[features])

# Apply K-means clustering
kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_features)

# Analyze segment characteristics
cluster_summary = df.groupby('Cluster').mean()

# Plot the distribution of clusters
plt.figure(figsize=(10, 6))
sns.countplot(x='Cluster', data=df)
plt.title('Distribution of Clusters')
plt.show()

print(cluster_summary)
