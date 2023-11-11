<!--

author:   Daniel Schwartz
email:    des338@drexel.edu
version:  0.0.0
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

Previous versions: 

- [x.x.x](link): that version's current version description
- [x.x.x](link): that version's current version description
- [x.x.x](link): that version's current version description
@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
import: https://raw.githubusercontent.com/arcus/education_modules/pyodide_testing/_module_templates/macros_python.md
import: https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md
-->

# Python Lesson on Clustering for Machine Learning

@overview

### What is clustering?
- Clustering is an unsupervised machine learning technique that groups unlabeled data points into clusters based on their similarity. The goal of clustering is to identify groups of data points that are similar to each other and dissimilar to data points in other groups. Clustering algorithms work by measuring the similarity between data points and then grouping similar data points together. There are many different clustering algorithms, each with its own strengths and weaknesses. Some of the most common clustering algorithms include K-Means clustering, hierarchical clustering, and Gaussian Mixture Models (GMMs). 




[True/False] Clustering algorithms are always able to find the "correct" clusters in the data.


[( )] True
[(X)] False
***
<div class = "answer">

This question is designed to test the test-taker's understanding of the limitations of clustering algorithms. Clustering algorithms are heuristics, which means that they do not guarantee to find the "correct" clusters in the data. The results of a clustering algorithm will depend on the distance metric used, the initialization of the algorithm, and the parameters of the algorithm.


</div>
***


[True/False] Clustering algorithms can be used to detect outliers in the data.


[( )] True
[(X)] False
***
<div class = "answer">

This question is designed to test the test-taker's understanding of the difference between clustering and anomaly detection. Clustering algorithms are used to group similar data points together, while anomaly detection algorithms are used to identify data points that are significantly different from the rest of the data.


</div>
***

### Unsupervised vs. Supervised Learning
- **Unsupervised learning** is a type of machine learning where the algorithm is trained on unlabeled data. This means that the data does not have pre-defined labels or categories. The goal of unsupervised learning is to identify patterns and relationships in the data without any prior knowledge of the data.
- **Supervised learning** is a type of machine learning where the algorithm is trained on labeled data. This means that the data has pre-defined labels or categories. The goal of supervised learning is to train a model to predict the labels for new data points. 



Which of the following is a goal of supervised learning?



[( )] Identify patterns and relationships in the data
[( )] Group similar data points together
[( )] Detect outliers in the data
[(X)] Predict the labels for new data points
[( )] Understand the underlying structure of the data
***
<div class = "answer">

Predicting the labels for new data points is a goal of supervised learning, not unsupervised learning. Unsupervised learning algorithms are used to identify patterns and relationships in the data without any prior knowledge of the data. This can be useful for tasks such as market segmentation, fraud detection, and anomaly detection.



</div>
***





### Applications of clustering in machine learning
Clustering can be used for a variety of tasks, such as: 

-   **Customer segmentation:**  Clustering can be used to segment customers into different groups based on their demographics, purchase behavior, or other characteristics. This information can then be used to target marketing campaigns or product development efforts to specific customer segments.
-   **Product grouping:**  Clustering can be used to group products with similar characteristics, such as price, features, or customer reviews. This information can be used to improve product recommendations or to identify opportunities for cross-selling and up-selling.
-   **Image segmentation:**  Clustering can be used to segment images into different objects or regions. This information can be used in tasks such as object detection, image classification, and image compression.
-   **Anomaly detection:**  Clustering can be used to identify anomalous data points that are different from the rest of the data. This information can be used to detect fraud, identify errors in data collection, or predict future events.
-   **Medical diagnosis:**  Clustering can be used to group patients with similar symptoms or medical histories together. This information can be used to improve the accuracy of medical diagnosis and to develop more personalized treatment plans.
-   **Scientific research:**  Clustering can be used to identify patterns and relationships in scientific data. This information can be used to advance scientific knowledge and to develop new technologies. 

### Examples of clustering in real-world applications
-   **Netflix uses clustering to recommend movies and TV shows to its users.**  Netflix clusters its users based on their viewing history and then recommends movies and TV shows to users based on the clusters they belong to.
-   **Amazon uses clustering to recommend products to its customers.**  Amazon clusters its products based on customer reviews and purchase behavior. Amazon then recommends products to customers based on the clusters the products belong to and the customer's past purchase history.
-   **Google uses clustering to improve the accuracy of its search results.**  Google clusters search results based on the relevance of the results to the search query. Google then displays the most relevant results at the top of the search results page.
-   **Banks use clustering to detect fraudulent transactions.**  Banks cluster transactions based on their characteristics, such as the amount of money involved, the type of transaction, and the location of the transaction. Banks then flag anomalous transactions as potentially fraudulent.
-   **Medical researchers use clustering to identify new biomarkers for diseases.**  Medical researchers cluster patients based on their medical histories and symptoms. Researchers then look for patterns in the clusters to identify new biomarkers that can be used to diagnose and treat diseases.

## K-Means Clustering Algorithm
- The K-Means clustering algorithm works by iteratively assigning data points to clusters based on their distance to the cluster centroids. The cluster centroids are the average values of all the data points in a cluster. 

```
1. Choose the number of clusters (K):
    - This is an important step, as it will determine the outcome of the clustering process.
    - There is no one-size-fits-all answer to the question of how to choose K. One approach is to use the elbow method, which involves plotting the within-cluster sum of squares (WCSS) for different values of K.
    - The elbow point on the plot is the point where the WCSS starts to flatten out, and this is often a good choice for K.
2. Initialize the cluster centroids
    - The cluster centroids can be initialized randomly or by choosing K data points from the dataset.
3. Assign each data point to the cluster with the nearest centroid
    - The distance between a data point and a cluster centroid can be measured using any distance metric, such as Euclidean distance or Manhattan distance.
4. Recalculate the cluster centroids
    - The cluster centroids are recalculated by taking the average of all the data points in each cluster.
5. Repeat steps 3 and 4 until the cluster assignments no longer change

```



What is the goal of the K-Means clustering algorithm?


[( )] To identify the clusters with the highest within-cluster sum of squares (WCSS)
[( )] To identify the clusters with the lowest within-cluster sum of squares (WCSS)
[( )] To identify the clusters with the highest between-cluster sum of squares (BCSS)
[( )] To identify the clusters with the lowest between-cluster sum of squares (BCSS)
[(X)] To group similar data points together
***
<div class = "answer">

The goal of the K-Means clustering algorithm is to group similar data points together. This is achieved by iteratively assigning data points to clusters based on their distance to the cluster centroids.



</div>
***


    
### Python Implementation of K-Means Clustering
    

To implement k-means clustering in Python using Scikit-learn, we can follow these steps:

1.  Import the necessary libraries:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from scipy.spatial import distance
```
@Pyodide.eval


2.  Load the data:
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


3.  Visualize data
```python
# Create the scatter plot
data.plot.scatter(x='chol', y='trtbps', c='output', colormap='viridis')
plt.xlabel("Cholesterol")
plt.ylabel("Resting Blood Pressure")
plt.title("Scatter Plot of Cholesterol vs. Blood Pressure")
plt.show()
```
@Pyodide.eval

3.  Split the data into training and testing sets:
```python
# Normalize dataframe
def normalize(df, features):
    result = df.copy()
    for feature_name in features:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result

normalized_data = normalize(data, data.columns)
```
@Pyodide.eval

4.  Train the clustering model and visualize:
```python
# Run KMeans
kmeans = KMeans(n_clusters = 2, max_iter = 500, n_init = 40, random_state = 2)

# Predict clusters
identified_clusters = kmeans.fit_predict(normalized_data.values)
results = normalized_data.copy()
results['cluster'] = identified_clusters

# Compute distance from cluster
distance_from_centroid = [distance.euclidean(val[:-1],kmeans.cluster_centers_[int(val[-1])]) for val in results.values]
results['dist'] = distance_from_centroid
results.plot.scatter(x='chol', y='trtbps', c='cluster', colormap='viridis', s='dist')
plt.xlabel("Cholesterol")
plt.ylabel("Resting Blood Pressure")
plt.show()
```
@Pyodide.eval

    

### Applying K-Means Clustering to a Real-World Dataset

-   **Loading and cleaning the data:** The first step is to load the data into Python and clean it as needed. This may involve removing outliers, handling missing values, and scaling the data.
-   **Scaling the data:** It is important to scale the data before applying K-Means clustering. This helps to ensure that all features have equal importance in the clustering process.
-   **Choosing the number of clusters (K):** There is no one-size-fits-all answer to the question of how to choose the number of clusters (K). One approach is to use the elbow method, which involves plotting the within-cluster sum of squares (WCSS) for different values of K. The elbow point on the plot is the point where the WCSS starts to flatten out, and this is often a good choice for K.
-   **Training and evaluating the K-Means model:** Once you have chosen the number of clusters, you can train the K-Means model on the data. You can then evaluate the model by computing the silhouette score. The silhouette score is a measure of how well the data points are clustered, and a higher score indicates better clustering.
-   **Visualizing the clusters:** Once you have trained and evaluated the K-Means model, you can visualize the clusters using a scatter plot. This can help you to understand how the data is clustered and to identify any outliers.

### Important Notes
Clustering is a machine learning technique that groups unlabeled data points into clusters based on their similarity. It is a powerful tool that can be used to solve a variety of problems, such as customer segmentation, product grouping, and anomaly detection. However, clustering also has some limitations. Here are some of the most important limitations of clustering:

- **Sensitivity to the initialization:** Many clustering algorithms, such as k-means clustering, are sensitive to the initialization of the cluster centroids. If the cluster centroids are not initialized correctly, the clustering algorithm may not be able to find the optimal clusters.
- **Difficulty in choosing the number of clusters:** K-means clustering requires the user to specify the number of clusters (k) in advance. However, there is no one-size-fits-all answer to the question of how to choose k. Choosing the wrong number of clusters can lead to inaccurate results.
- **Inability to handle outliers:** Clustering algorithms are often sensitive to outliers, which are data points that are significantly different from the rest of the data. Outliers can have a large impact on the clustering results and can lead to inaccurate clusters.
- **Difficulty in interpreting the results:** It can be difficult to interpret the results of clustering algorithms, especially when the data is high-dimensional. It can be difficult to understand what the clusters represent and why the data points were assigned to the clusters they were assigned to.



Which of the following techniques can be used to mitigate the sensitivity of clustering algorithms to the initialization?



[( )] Running the clustering algorithm multiple times with different initializations and selecting the best results
[( )] Using a more robust clustering algorithm that is less sensitive to the initialization
[( )] Preprocessing the data to remove outliers
[(X)] All of the above
***
<div class = "answer">

All of the above techniques can be used to mitigate the sensitivity of clustering algorithms to the initialization.



</div>
***


## Conclusion

At the end of the lesson, students should have a good understanding of the concept of clustering and how to implement the K-Means clustering algorithm in Python. They should also be able to apply K-Means clustering to real-world datasets to identify patterns and insights.

## Additional Resources

## Feedback

@feedback
