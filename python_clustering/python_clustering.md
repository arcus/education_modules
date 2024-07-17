<!--

author:   Daniel Schwartz
email:    des338@drexel.edu
version:  1.0.0
current_version_description: Initial version
module_type: standard
docs_version: 3.0.0
language: en
narrator: UK English Female
mode: Textbook

title: Python Lesson on Clustering for Machine Learning

comment:  Understand the basics of clustering, including how it works and when to use it in Python.

long_description: Understand clustering in Python as a powerful and versatile tool that can be used to solve a wide variety of problems. By understanding the key concepts and techniques involved in clustering, you can build and deploy models that can accurately cluster unlabeled data.

estimated_time_in_minutes: 20

@pre_reqs

This module assumes learners have been exposed to introductory statistics, Algebra, and probability.
There are coding exercises in Python, so programming experience is required.

@end

@learning_objectives  

-   Understand the concept of clustering and its applications in machine learning
-   Learn how to implement the K-Means clustering algorithm in Python
-   Apply K-Means clustering to a real-world dataset

@end

good_first_module: false
data_task: data_analysis
collection: machine_learning
coding_required: true
coding_level: basic
coding_language: python

@sets_you_up_for

@end

@depends_on_knowledge_available_in

@end

@version_history 
No previous versions.
@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
import: https://raw.githubusercontent.com/arcus/education_modules/pyodide_testing/_module_templates/macros_python.md
import: https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md
-->

# Clustering in Python

@overview



## Review of Clustering

**Clustering** is a machine learning technique used to group unlabeled data points into clusters based on their similarity. The goal is to identify groups of data points that are similar to each other and dissimilar to data points in other groups. In this lesson we will work through an example of K-Means clustering. Other common algorithms hierarchical clustering, and Gaussian Mixture Models.

For a more in-depth look at what clustering is, see the [_other clustering module_](link).

Clustering is a type of **unsupervised learning**.  Unsupervised learning algorithms are algorithms trained on unlabeled data to identify patterns and relationships without prior knowledge. This is different from supervised learning, where an algorithm is initially trained on labeled data in order to predict labels for new data points.

- **Applications:** Clustering finds applications in various fields such as customer segmentation, biomedical research, drug development, gene expression analysis, medical image analysis, and disease-risk prediction.



- **Understanding Techniques:** Techniques like normalization, computing distances from cluster centroids, and visualization aid in building accurate clustering models and interpreting results.

- **Challenges and Limitations:** Challenges include sensitivity to initialization, difficulty in choosing the number of clusters, handling outliers, and interpreting results in high-dimensional data.

- **Mitigating Sensitivity:** Techniques like running the algorithm multiple times with different initializations, using robust algorithms, and preprocessing data help mitigate sensitivity to initialization.

- **Conclusion:** Clustering is a powerful tool with diverse applications, but it's essential to understand its limitations and challenges. With foundational knowledge in clustering techniques, one can explore advanced methods and make informed decisions in data analysis and machine learning endeavors.


    
## The K-Means Clustering Algorithm

The **K-Means Clustering Algorithm**, sometimes refered to as simply "K-Means," works by iteratively assigning data points to clusters based on their distance to cluster centroids. 

The key steps of K-Means clustering are:
1. choosing the number of clusters (K), 
2. initializing centroids, assigning data points, 
3. recalculating centroids, and 
4. iterating until convergence.

### Clustering Patients

We are going to use use an dataset ***(add more details about its origin)*** 
This dataset contains various clinical attributes of patients, including their age, sex, chest pain type (cp), resting blood pressure (trtbps), serum cholesterol level (chol), fasting blood sugar (fbs) level, resting electrocardiographic results (restecg), maximum heart rate achieved (thalachh), exercise-induced angina (exng), ST depression induced by exercise relative to rest (oldpeak), slope of the peak exercise ST segment (slp), number of major vessels (caa) colored by fluoroscopy, thalassemia (thall) type, and the presence of heart disease (output). The data seems to be related to the diagnosis of heart disease, with the output variable indicating whether a patient has heart disease (1) or not (0). Each row represents a different patient, with their respective clinical characteristics recorded.

To implement k-means clustering in Python using Scikit-learn, we can follow these steps:

### 1.  Import Libraries

**Description:**
This step imports essential libraries needed for data manipulation, analysis, and visualization, as well as the KMeans clustering algorithm.

* **numpy (np):** This library provides tools for numerical operations and working with arrays, which are essential for data manipulation in machine learning.
* **pandas (pd):** Pandas is used for data analysis and manipulation, especially with tabular data. It makes it easy to load, clean, and organize your data.
* **matplotlib.pyplot (plt):** Matplotlib is a powerful plotting library for creating graphs and visualizations. We'll use it to visualize our data and clustering results.
* **sklearn.model_selection (train_test_split):** We'll use this function later if we need to split our data into training and testing sets for model evaluation.
* **sklearn.cluster (KMeans):** This is where the heart of our clustering algorithm lies. KMeans is the specific algorithm we'll use to group our data into clusters.
* **scipy.spatial (distance):** Scipy is a broader scientific computing library. The distance module provides functions to calculate distances between points, which we'll use in our KMeans analysis.

**Why is it important:**
These libraries provide the foundational tools and functions required to perform data preprocessing, clustering, and visualization. Without them, we wouldn't be able to efficiently handle the data or perform the clustering analysis.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from scipy.spatial import distance
```
@Pyodide.eval

**Output:**
There is no direct output for this step, as it is focused on importing necessary libraries. However, successful execution without errors indicates that the libraries are correctly imported and ready for use.




### 2.  Loading the Data

**Description:**
This step involves loading the patient data from a CSV file into a Pandas DataFrame and then examining the structure of the data.

* `data = pd.read_csv(file)`: This line reads the CSV (Comma-Separated Values) file, which presumably contains your patient data, into a Pandas DataFrame called `data`. DataFrames are like tables, where each row represents a patient, and each column represents a feature (e.g., age, cholesterol).
* `data.info()`: This function gives you a summary of the DataFrame, showing the column names, their data types, and how many non-null values are in each column. This helps you understand the structure of your data.

**Why it's important:**
Understanding the structure of your data is crucial before performing any data manipulation or analysis. It helps identify any missing values, understand data types, and get a general overview of the dataset.


```python @Pyodide.exec

import pandas as pd
import io
from pyodide.http import open_url

url = "https://raw.githubusercontent.com/arcus/education_modules/python_clustering/python_clustering/data/heart.csv"

url_contents = open_url(url)
text = url_contents.read()
file = io.StringIO(text)

data = pd.read_csv(file)


# Analyze data and features
data.info()
```


**Output:**

`data.info()` gives a summary of the DataFrame, including the number of non-null entries for each column and their data types.
`print(data.head())` displays the first few rows of the DataFrame to give learners a feel for what the data looks like.



### 3.  Visualize Data
**Description:** This code generates a scatter plot with `chol` (Cholesterol) on the x-axis and `trtbps` (Resting Blood Pressure) on the y-axis. The data points are colored based on the `output` column, using the `viridis` colormap. Labels and a title are added, and then the plot is displayed.  


**Why it's important:**
Understanding the structure of your data is crucial before performing any data manipulation or analysis. It helps identify any missing values, understand data types, and get a general overview of the dataset.

```python
# Create the scatter plot
data.plot.scatter(x='chol', y='trtbps', c='output', colormap='viridis')
plt.xlabel("Cholesterol")
plt.ylabel("Resting Blood Pressure")
plt.title("Scatter Plot of Cholesterol vs. Blood Pressure")
plt.show()
```
@Pyodide.eval


**Output:**
By adding the `print(data.head())` statement, you can see the first few rows of the data, which helps understand the dataset's structure and the columns being used in the plot.


### 4.  Normalize DataFrame

**Description:**

* The function `normalize(df, features)` is defined to perform min-max normalization of the features listed in `features` within the DataFrame `df`. It creates a copy `result` of the DataFrame and iterates over each feature to scale its values to the range [0, 1]. The normalized DataFrame `result` is returned.  
* The `normalize` function is then applied to the `data` DataFrame to normalize all columns, and the results are stored in `normalized_data`.

**Why it is important:**
Normalization is crucial because it scales the data to a common range without distorting differences in the ranges of values. This ensures that no single feature dominates the clustering algorithm due to its scale, leading to more meaningful and comparable results.


```python
# Normalize dataframe
def normalize(df, features):
    # Create a copy of the DataFrame to avoid modifying the original data.
    result = df.copy()

    # Iterate through each feature specified for normalization.
    for feature_name in features:
        # Find the maximum and minimum values of the current feature.
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()

        # Normalize the current feature using min-max scaling formula.
        # This ensures that all values of the feature are scaled between 0 and 1.
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result

# Call the normalize function with the entire DataFrame 'data' and all its columns.
# Store the result in 'normalized_data'.
normalized_data = normalize(data, data.columns)

# Print the normalized data to see the transformed values
print(normalized_data)
```
@Pyodide.eval

**Output:**
This code performs min-max normalization on the dataset and prints the resulting normalized_data. The output will show the scaled values of each feature, ensuring that all values are between 0 and 1. This step is critical for ensuring that the clustering algorithm treats each feature equally.





### 5. Run KMeans
**Description:** This line creates a KMeans object.  

**Why this is important:**
The KMeans algorithm is a popular clustering method that partitions the data into distinct groups (clusters) based on feature similarity. By configuring the parameters, we can control the behavior of the algorithm and ensure consistent results.

    * `n_clusters = 2` tells KMeans to find two clusters in your data.  
    * `max_iter = 500` sets a maximum of 500 iterations for the algorithm to converge.  
    * `n_init = 40` means the algorithm will be run 40 times with different random initializations, and the best result will be chosen.  
    * `random_state = 2` ensures reproducibility; you'll get the same clustering results each time you run the code.  


```python
# Create KMeans object
kmeans = KMeans(n_clusters=2, max_iter=500, n_init=40, random_state=2)
print("KMeans object created with the following parameters:")
print(f"Number of clusters: {kmeans.n_clusters}")
print(f"Maximum iterations: {kmeans.max_iter}")
print(f"Number of initializations: {kmeans.n_init}")
print(f"Random state: {kmeans.random_state}")

```
@Pyodide.eval

**Output:**
Since the KMeans object creation itself does not produce output, the impact of this step will be evident in the following steps where we fit the model and predict clusters.





### 6.  Predict Clusters
**Description:**

* `kmeans.fit_predict()` does two things:  

    1. It fits the KMeans model to your normalized data, meaning it finds the cluster centers.  
    2. It predicts which cluster each data point belongs to, returning an array `identified_clusters` where each element corresponds to the cluster assignment of a data point.  

* We create a copy `results` of the `normalized_data` and add a new column `cluster` to it, storing the identified cluster labels.  

**Why this is important:**
Fitting the KMeans model to the data and predicting clusters are crucial steps in the clustering process. By assigning each data point to a cluster, we can analyze patterns and group similar data points together. This can reveal underlying structures in the data and help in further analysis or decision-making processes.


```python
# Fit the KMeans model to the normalized data and predict the clusters
identified_clusters = kmeans.fit_predict(normalized_data.values)

# Create a copy of the normalized data to store the results
results = normalized_data.copy()

# Add the identified cluster labels as a new column 'cluster' in the results DataFrame
results['cluster'] = identified_clusters

# Print the results to observe the DataFrame with the cluster assignments
print(results.head())
```
@Pyodide.eval

**Output:**
The output will be a preview of the first few rows of the results DataFrame, which now includes the original normalized data along with the new cluster column. In this output:  

* Each row corresponds to a data point (e.g., a patient's data in a medical dataset).  
* The columns represent the normalized features (e.g., age, sex, cp, etc.).  
* The cluster column indicates the cluster assignment for each data point, with values such as 0 or 1 representing different clusters.  
* This output allows shows how their data points have been grouped into clusters based on the KMeans algorithm.  




### 7. Compute Distance from Cluster Centroid
**Description:** This line calculates the Euclidean distance between each data point and its assigned cluster centroid. This distance is stored in the list `distance_from_centroid` and added as a new column `dist` in the results DataFrame.

**Why this is important:**
Computing the distance from each data point to its cluster centroid provides insight into how well the data points are clustered around their centroids. It helps assess the compactness of clusters and can be useful for evaluating the quality of the clustering.

```python
# Calculate the Euclidean distance between each data point and its assigned cluster centroid
distance_from_centroid = [distance.euclidean(val[:-1], kmeans.cluster_centers_[int(val[-1])]) for val in results.values]

# Add the computed distances as a new column 'dist' in the results DataFrame
results['dist'] = distance_from_centroid

# Print the results to observe the DataFrame with the distance values
print(results.head())
```
@Pyodide.eval

**Output:**
The output will display the first few rows of the results DataFrame with the newly added dist column, representing the distances of each data point from its assigned cluster centroid. This output allows learners to understand how the distances are calculated and see the impact of the clustering on the data.


### 8. Train the clustering model and visualize
**Description:** Creates a scatter plot of `chol` (Cholesterol) against `trtbps` (Resting Blood Pressure), colored by the identified clusters, with marker size proportional to the distance from the cluster centroid.

**Why this is important:**
Visualization is crucial for understanding clustering results. By plotting the data points with identified clusters, we can visually inspect how well the clustering algorithm has grouped similar data points together. Additionally, using marker size to represent the distance from the cluster centroid provides insights into the compactness of each cluster.

```python
results.plot.scatter(x='chol', y='trtbps', c='cluster', colormap='viridis', s='dist')
plt.xlabel("Cholesterol")
plt.ylabel("Resting Blood Pressure")
plt.show()
```
@Pyodide.eval

**Output:**
The output is a scatter plot where each data point is represented by a marker. The markers are colored based on the identified clusters, and their sizes vary depending on the distance from the cluster centroid. This visualization allows learners to visually inspect how the data points are grouped into clusters and how compact each cluster is.



## Review your knowledge

```python
from sklearn.cluster import KMeans

# Create a KMeans instance with ____ clusters
kmeans = KMeans(n_clusters=____)

# Fit the model to the data
kmeans.fit(____)

# Get the cluster centroids
centroids = kmeans.cluster_centers_

# Predict the cluster labels for the data points
labels = kmeans.predict(____)
```


Fill in the blanks to implement the K-Means clustering algorithm in Python:

[( )]  `k`, `k`, `X`
[( )] `n_clusters`, `K`, `data`
[(X)] `K`, `n_clusters`, `data`
[( )] `data`, `n_clusters`, `K`
***
<div class = "answer">

This question tests your understanding of implementing the K-Means clustering algorithm using the scikit-learn library in Python. To answer correctly, you need to identify the correct placeholders for the number of clusters and the dataset in the code snippet. The correct option, "K, n_clusters, data," corresponds to the appropriate parameters and function calls required for the K-Means algorithm.

</div>




## Conclusion

Through this lesson, you've gained a solid foundation in clustering, a cornerstone of unsupervised machine learning. You've learned how the K-Means algorithm works, its strengths and limitations, and most importantly, how to harness it within Python's powerful data science ecosystem.

### Key Takeaways
Here's a summary of key takeaways to keep in mind:  

* **Clustering Unveils Hidden Structures:** K-Means can reveal meaningful groupings within your data that might not be immediately apparent. This is crucial for tasks like customer segmentation, anomaly detection, and even preliminary exploration before applying more complex models.  
* **Real-World Applications Abound:** Clustering isn't just theoretical. We've seen how it can be used in medical diagnostics (predicting heart disease risk based on patient attributes) and in pharmaceutical research (identifying patient subgroups responding differently to treatments). This demonstrates the algorithm's versatility across domains.  
* **Data Preprocessing is Key:** The quality of your clustering results depends heavily on how you prepare your data. Normalization and feature scaling are often essential steps to ensure that all features contribute equally to the clustering process.  
* **K-Means Isn't Perfect:** Remember that K-Means has its limitations. It assumes clusters are spherical and of equal size, which isn't always the case in real-world data. Additionally, choosing the optimal number of clusters (K) requires careful consideration and experimentation.  


### Beyond K-Means
While K-Means is a great starting point, the world of clustering is vast. As you progress in your machine learning journey, you'll encounter more sophisticated algorithms like DBSCAN, hierarchical clustering, and Gaussian mixture models. Each has its own strengths and use cases.

Consider exploring these areas to expand your clustering toolkit:  

* **Dimensionality Reduction:** Techniques like PCA can help visualize high-dimensional clustered data.  
* **Cluster Evaluation:** Learn metrics like silhouette score to assess the quality of your clusters objectively.  
* **Ensemble Clustering:** Combining multiple clustering algorithms can often lead to more robust and accurate results.  

The knowledge you've gained here equips you to tackle a wide range of data analysis challenges. By applying clustering thoughtfully and critically, you can unlock valuable insights and drive data-driven decision-making.

## Additional Resources

### Full Code Implementation

At the end of this module, here you will find a "Full Code" section where all the code is consolidated into a single cell block. This allows for easy copying and pasting for those who want to implement the entire process quickly. While this single block of code isn't designed as a step-by-step educational tool, it serves as a convenient reference for future use and helps streamline the process for those already familiar with the concepts. Below is the complete code implementation:

```python
# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from scipy.spatial import distance
import io
from pyodide.http import open_url

# Load Data
url = "https://raw.githubusercontent.com/arcus/education_modules/python_clustering/python_clustering/data/heart.csv"
url_contents = open_url(url)
text = url_contents.read()
file = io.StringIO(text)
data = pd.read_csv(file)
data.info()

# Visualize Data
data.plot.scatter(x='chol', y='trtbps', c='output', colormap='viridis')
plt.xlabel("Cholesterol")
plt.ylabel("Resting Blood Pressure")
plt.title("Scatter Plot of Cholesterol vs. Blood Pressure")
plt.show()

# Normalize DataFrame
def normalize(df, features):
    result = df.copy()
    for feature_name in features:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result

normalized_data = normalize(data, data.columns)

# Run KMeans
kmeans = KMeans(n_clusters = 2, max_iter = 500, n_init = 40, random_state = 2)

# Predict Clusters
identified_clusters = kmeans.fit_predict(normalized_data.values)
results = normalized_data.copy()
results['cluster'] = identified_clusters

# Compute Distance from Cluster Centroid
distance_from_centroid = [distance.euclidean(val[:-1], kmeans.cluster_centers_[int(val[-1])]) for val in results.values]
results['dist'] = distance_from_centroid

# Visualize Clusters
results.plot.scatter(x='chol', y='trtbps', c='cluster', colormap='viridis', s='dist')
plt.xlabel("Cholesterol")
plt.ylabel("Resting Blood Pressure")
plt.show()
```
@Pyodide.eval

## Feedback

@feedback
