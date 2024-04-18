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

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

As in many fields, machine learning involves a lot of technical language, some of which is unclear, redundant, or downright confusing.
For example:

**Outcome** variables are also called **response variables**, **dependent variables**, or **labels**.

**Input** variables are also called **predictors**, **features**, **independent variables**, or even just **variables**.

To make matters worse, sometimes the same words are used to mean different things in different subfields.
If you find yourself stumbling on vocabulary as you read about machine learning, know you're not alone!

</div>


[True/False] Clustering algorithms are always able to find the "correct" clusters in the data.


[( )] True
[(X)] False
***
<div class = "answer">

Clustering algorithms are helpful tools, but they're not magic. Here's why this statement is false:

- Clustering isn't about "right" or "wrong": There's often no single "correct" way to group data. Clustering depends on how you measure similarity and the type of patterns you're interested in finding.  
- Different setups, different results: The clusters you get can change based on the clustering algorithm you choose, how you measure distances between data points, and even the starting settings of the algorithm.  
Key takeaway: Clustering is an exploratory process. It can suggest interesting groupings in your data, but it's up to you to decide if those groupings make sense and are useful for your analysis.


</div>
***


[True/False] Clustering algorithms can be used to detect outliers in the data.


[( )] True
[(X)] False
***
<div class = "answer">

While clustering algorithms can sometimes help identify potential outliers, they are not specifically designed for this purpose. Here's why:  

- Clustering focuses on grouping:  Clustering algorithms aim to find groups of similar data points. Outliers, by definition, don't fit well into any group.  
- Outliers might influence clusters: A significant outlier might distort the clustering process, either by forming its own tiny cluster or being forced into a larger cluster where it doesn't truly belong.  


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
### Applications of Clustering in Biomedical Research

Clustering is an invaluable machine learning technique with wide-ranging applications in biomedical research. Here are some key areas where it can be used :

- **Patient Stratification:** Identify distinct subgroups within patient populations based on gene expression profiles, clinical data, or disease biomarkers. This can lead to insights into disease subtypes and more personalized treatment options.  
    - Specifically in research, ["Use of Latent Class Analysis and k-Means Clustering to Identify Complex Patient Profiles"](https://jamanetwork.com/journals/jamanetworkopen/article-abstract/2774074) employs statistical techniques to categorize patients into specific groups based on their gene expression profiles, clinical data, or biomarkers, allowing for the identification of unique disease subtypes and facilitating personalized treatment options. This approach aligns with patient stratification by utilizing clustering methods to segregate patients into distinct categories, enabling healthcare professionals to tailor interventions based on individualized characteristics and needs.  
- **Drug Development:** Clustering can help group compounds based on chemical structure, efficacy, or target interactions. This facilitates the identification of novel drug candidates or the repurposing of existing drugs.  
    - ["Integration of k-means clustering algorithm with network analysis for drug-target interactions network prediction"](https://www.inderscienceonline.com/doi/abs/10.1504/IJDMB.2018.094776) combines k-means clustering with network analysis to predict drug-target interactions, aiding in the identification of potential drug candidates or repurposing existing drugs by grouping compounds based on their interactions and properties. This study directly aligns with drug development goals by leveraging clustering to categorize compounds and enhance the understanding of their interactions, thereby facilitating the discovery and optimization of therapeutic agents.  

- **Gene Expression Analysis:** Clustering genes with similar expression patterns across different conditions or time points can help uncover regulatory networks and potential therapeutic targets.  
    - ["Clust: automatic extraction of optimal co-expressed gene clusters from gene expression data"](https://link.springer.com/article/10.1186/s13059-018-1536-8) automates the extraction of co-expressed gene clusters from gene expression data, aiding in the identification of regulatory networks and potential therapeutic targets by clustering genes with similar expression patterns across different conditions or time points. This tool directly aligns with gene expression analysis goals by utilizing clustering to group genes based on their expression profiles, facilitating the discovery of underlying biological mechanisms and potential targets for intervention.  

- **Medical Image Analysis:** Segment medical images (MRI, CT scans) to differentiate tissues, identify tumors and other abnormalities. Clustering can aid in diagnosis and disease tracking.  
    - ["Diagnosis of Brain Tumor Using Combination of K-Means Clustering and Genetic Algorithm"](http://www.ijmi.ir/index.php/IJMI/article/view/159) utilizes a combination of k-means clustering and genetic algorithms to accurately diagnose brain tumors by segmenting medical images, demonstrating how clustering techniques can aid in medical image analysis to differentiate tissues and identify abnormalities such as tumors, aligning with the objective of leveraging clustering for diagnosis and disease tracking in medical imaging.  

- **Disease-Risk Prediction:** Analyze patient data to cluster individuals based on risk factors and medical history, enabling the prediction of susceptibility to various diseases.  
    - ["A K-Means Approach to Clustering Disease Progressions"](https://ieeexplore.ieee.org/document/8031156) utilizes k-means clustering to categorize individuals based on disease progression patterns, facilitating disease-risk prediction by analyzing patient data to cluster individuals according to their risk factors and medical histories. This study directly relates to the objective of disease-risk prediction by employing clustering techniques to identify distinct groups of patients with similar disease progressions, thereby enabling more accurate predictions of susceptibility to various diseases based on individualized characteristics.



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
<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

To learn more about Linear Regression and for a visual explanation, watch [StatQuest: K-means clustering](https://youtu.be/4b5d3muPQmA?si=KMQxx23Ru8w7GOFP).

</div>


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





### Understanding Machine Learning Techniques

Before diving into the example, it's valuable to understand some key concepts used in machine learning. These techniques help us build more accurate and reliable models for clustering.

- **Normalization:**  Normalization is crucial for scaling the features of the dataset to a uniform range, typically between 0 and 1, ensuring that each feature contributes equally to the clustering process.  

        - By ensuring equitable treatment of all features, normalization prevents features with larger magnitudes from dominating distance calculations in clustering algorithms. This fosters the identification of clusters based on similarity across multiple dimensions and enhances the discovery of meaningful patterns and relationships within the data.   

- **Computing Distance from Cluster Centroid:** Calculating the distance from each data point to its assigned cluster centroid provides a quantitative measure of the data point's fit within its cluster.  

        - Distance metrics aid in assessing the compactness of clusters and the separation between clusters. In applications, distance calculations play a pivotal role in cluster validation and refinement, quantifying the similarity of data points within clusters and improving the overall efficacy of clustering algorithms in delineating coherent and distinct groups within the dataset.  
     
- **Visualization:** Visualizing clustering results facilitates intuitive interpretation and assessment of identified clusters.  

        - Visual representations, such as scatter plots, enable the identification of inherent data patterns, outliers, and delineation of cluster boundaries. In applications, visualization aids in informed decision-making by providing stakeholders with insights into the data's structure and characteristics, fostering actionable insights and informed decisions.  

    
### Python Implementation of K-Means Clustering
    

This dataset contains various clinical attributes of patients, including their age, sex, chest pain type (cp), resting blood pressure (trtbps), serum cholesterol level (chol), fasting blood sugar (fbs) level, resting electrocardiographic results (restecg), maximum heart rate achieved (thalachh), exercise-induced angina (exng), ST depression induced by exercise relative to rest (oldpeak), slope of the peak exercise ST segment (slp), number of major vessels (caa) colored by fluoroscopy, thalassemia (thall) type, and the presence of heart disease (output). The data seems to be related to the diagnosis of heart disease, with the output variable indicating whether a patient has heart disease (1) or not (0). Each row represents a different patient, with their respective clinical characteristics recorded.

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

3.  This code defines a function called normalize that performs min-max scaling normalization on a DataFrame df, specifically on the features specified by the features parameter. The normalized DataFrame is returned as the output. Then, it calls this function to normalize all columns of a DataFrame data and assigns the result to a variable named normalized_data.
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
```
@Pyodide.eval

4.  Train the clustering model and visualize:
```python
# Run KMeans
kmeans = KMeans(n_clusters = 2, max_iter = 500, n_init = 40, random_state = 2)
```
@Pyodide.eval

5.  Train the clustering model and visualize:
```python
# Predict clusters
identified_clusters = kmeans.fit_predict(normalized_data.values)
results = normalized_data.copy()
results['cluster'] = identified_clusters
```
@Pyodide.eval

6.  Train the clustering model and visualize:
```python
# Compute distance from cluster. Loop through each data point and calculate the Euclidean distance between the data point and its assigned cluster centroid.
distance_from_centroid = [distance.euclidean(val[:-1],kmeans.cluster_centers_[int(val[-1])]) for val in results.values]
results['dist'] = distance_from_centroid
```
@Pyodide.eval


7.  Train the clustering model and visualize. Scatter plot of 'chol' (Cholesterol) against 'trtbps' (Resting Blood Pressure), colored by cluster, with marker size proportional to the distance from the cluster centroid.
```python
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



### Real World Code Example

This dataset, derived and refined from a landmark study published in the New England Journal of Medicine in 1993, investigates the effectiveness of sulindac treatment in individuals with familial adenomatous polyposis (FAP), a hereditary condition characterized by the development of numerous adenomatous polyps in the colon and rectum. Enhanced from the original datasets "polyps" and "polyps3" in the {HSAUR} package, this dataset includes crucial variables such as participant ID, sex, age, baseline polyp count, assigned treatment (sulindac or placebo), and polyp counts at 3 and 12 months post-treatment. These enhancements involved meticulous referencing of the original paper and offer improved granularity and completeness for analyzing the impact of sulindac treatment on polyp progression in FAP patients. This dataset serves as a valuable resource for further research and analysis in the field of gastrointestinal medicine and pharmacology.

1.  Install Packages:
```python @Pyodide.exec

import pandas as pd
import io
from pyodide.http import open_url
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
```

2.  Load the data:
```python
# Load dataset and read to pandas dataframe
url = "https://raw.githubusercontent.com/arcus/education_modules/python_clustering/python_clustering/data/polyps.csv"
url_contents = open_url(url)
text = url_contents.read()
file = io.StringIO(text)
df = pd.read_csv(file)

# Analyze data and features
df.info()

# Select features for clustering
features = ['age', 'baseline', 'number3m', 'number12m']
X = df[features]

# Fill missing values with the mean of each column
X.fillna(X.mean(), inplace=True)

# Standardize the feature values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```
@Pyodide.eval


3.  Cluster Data:
```python
# Define the number of clusters
num_clusters = 3

# Apply KMeans clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X_scaled)

# Assign cluster labels to the original dataframe
df['cluster'] = kmeans.labels_
```
@Pyodide.eval


4.  Visualize Clusters:
```python
# Visualize clusters for 'number3m' vs 'number12m'
plt.figure(figsize=(10, 8))
colors = ['red', 'blue', 'green']  # Change colors as needed for more clusters

for i in range(num_clusters):
    cluster_data = df[df['cluster'] == i]
    plt.scatter(cluster_data['number3m'], cluster_data['number12m'], 
                color=colors[i], label=f'Cluster {i}')

plt.xlabel('Number of Polyps at 3 Months')
plt.ylabel('Number of Polyps at 12 Months')
plt.title('K-Means Clustering of Polyp Data: Number of Polyps at 3 Months vs Number of Polyps at 12 Months')
plt.legend()
plt.show()
```
@Pyodide.eval

If the K-Means algorithm identified distinct clusters with minimal overlap, it suggests there might be three underlying patient groups regarding polyp count progression:

- **Cluster 1 (Low Progression):** This cluster might represent participants who have a relatively low number of polyps at 3 months and a stable or slightly increased number at 12 months. This could be associated with effective treatment or naturally slow polyp growth.
- **Cluster 2 (Moderate Progression):** This cluster could include participants with a moderate number of polyps at 3 months and a somewhat steeper increase by 12 months. This might indicate a less effective treatment or a faster natural growth rate for polyps.
- **Cluster 3 (High Progression):** This cluster might contain participants with a high number of polyps at 3 months and a substantial increase by 12 months. This could be linked to factors like a particularly aggressive polyp type or treatment resistance.

**While clustering provides valuable insights into potential patient subgroups, further analysis of treatment effects and other relevant features is necessary to fully understand the underlying factors influencing polyp count progression.**

    



## Conclusion

At the end of the lesson, students should have a good understanding of the concept of clustering and how to implement the K-Means clustering algorithm in Python. They should also be able to apply K-Means clustering to real-world datasets to identify patterns and insights.

## Additional Resources

## Feedback

@feedback
