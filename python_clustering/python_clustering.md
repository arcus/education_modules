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





    
### Python Implementation of K-Means Clustering
    

This dataset contains various clinical attributes of patients, including their age, sex, chest pain type (cp), resting blood pressure (trtbps), serum cholesterol level (chol), fasting blood sugar (fbs) level, resting electrocardiographic results (restecg), maximum heart rate achieved (thalachh), exercise-induced angina (exng), ST depression induced by exercise relative to rest (oldpeak), slope of the peak exercise ST segment (slp), number of major vessels (caa) colored by fluoroscopy, thalassemia (thall) type, and the presence of heart disease (output). The data seems to be related to the diagnosis of heart disease, with the output variable indicating whether a patient has heart disease (1) or not (0). Each row represents a different patient, with their respective clinical characteristics recorded.

To implement k-means clustering in Python using Scikit-learn, we can follow these steps:

1.  Import Libraries

* **numpy (np):** This library provides tools for numerical operations and working with arrays, which are essential for data manipulation in machine learning.
* **pandas (pd):** Pandas is used for data analysis and manipulation, especially with tabular data. It makes it easy to load, clean, and organize your data.
* **matplotlib.pyplot (plt):** Matplotlib is a powerful plotting library for creating graphs and visualizations. We'll use it to visualize our data and clustering results.
* **sklearn.model_selection (train_test_split):** We'll use this function later if we need to split our data into training and testing sets for model evaluation.
* **sklearn.cluster (KMeans):** This is where the heart of our clustering algorithm lies. KMeans is the specific algorithm we'll use to group our data into clusters.
* **scipy.spatial (distance):** Scipy is a broader scientific computing library. The distance module provides functions to calculate distances between points, which we'll use in our KMeans analysis.


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from scipy.spatial import distance
```
@Pyodide.eval


2.  Loading the Data
* `data = pd.read_csv(file)`: This line reads the CSV (Comma-Separated Values) file, which presumably contains your patient data, into a Pandas DataFrame called `data`. DataFrames are like tables, where each row represents a patient, and each column represents a feature (e.g., age, cholesterol).
* `data.info()`: This function gives you a summary of the DataFrame, showing the column names, their data types, and how many non-null values are in each column. This helps you understand the structure of your data.


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


3.  Visualize Data
This code generates a scatter plot with `chol` (Cholesterol) on the x-axis and `trtbps` (Resting Blood Pressure) on the y-axis. The data points are colored based on the `output` column, using the `viridis` colormap. Labels and a title are added, and then the plot is displayed.  

```python
# Create the scatter plot
data.plot.scatter(x='chol', y='trtbps', c='output', colormap='viridis')
plt.xlabel("Cholesterol")
plt.ylabel("Resting Blood Pressure")
plt.title("Scatter Plot of Cholesterol vs. Blood Pressure")
plt.show()
```
@Pyodide.eval

4.  Normalize DataFrame

* The function `normalize(df, features)` is defined to perform min-max normalization of the features listed in `features` within the DataFrame `df`. It creates a copy `result` of the DataFrame and iterates over each feature to scale its values to the range [0, 1]. The normalized DataFrame `result` is returned.  
* The `normalize` function is then applied to the `data` DataFrame to normalize all columns, and the results are stored in `normalized_data`.


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

5. Run KMeans
* This line creates a KMeans object.  

    * `n_clusters = 2` tells KMeans to find two clusters in your data.  
    * `max_iter = 500` sets a maximum of 500 iterations for the algorithm to converge.  
    * `n_init = 40` means the algorithm will be run 40 times with different random initializations, and the best result will be chosen.  
    * `random_state = 2` ensures reproducibility; you'll get the same clustering results each time you run the code.  


```python
# Run KMeans
kmeans = KMeans(n_clusters = 2, max_iter = 500, n_init = 40, random_state = 2)
```
@Pyodide.eval

6.  Predict Clusters
* `kmeans.fit_predict()` does two things:  
    1. It fits the KMeans model to your normalized data, meaning it finds the cluster centers.  
    2. It predicts which cluster each data point belongs to, returning an array `identified_clusters` where each element corresponds to the cluster assignment of a data point.  

* We create a copy `results` of the `normalized_data` and add a new column `cluster` to it, storing the identified cluster labels.  


```python
identified_clusters = kmeans.fit_predict(normalized_data.values)
results = normalized_data.copy()
results['cluster'] = identified_clusters
```
@Pyodide.eval

7. Compute Distance from Cluster Centroid
* This line calculates the Euclidean distance between each data point and its assigned cluster centroid. This distance is stored in the list `distance_from_centroid` and added as a new column `dist` in the results DataFrame.

```python
distance_from_centroid = [distance.euclidean(val[:-1],kmeans.cluster_centers_[int(val[-1])]) for val in results.values]
results['dist'] = distance_from_centroid
```
@Pyodide.eval


8. Train the clustering model and visualize
* Creates a scatter plot of `chol` (Cholesterol) against `trtbps` (Resting Blood Pressure), colored by the identified clusters, with marker size proportional to the distance from the cluster centroid.

```python
results.plot.scatter(x='chol', y='trtbps', c='cluster', colormap='viridis', s='dist')
plt.xlabel("Cholesterol")
plt.ylabel("Resting Blood Pressure")
plt.show()
```
@Pyodide.eval

    





## Conclusion

Through this lesson, you've gained a solid foundation in clustering, a cornerstone of unsupervised machine learning. You've learned how the K-Means algorithm works, its strengths and limitations, and most importantly, how to harness it within Python's powerful data science ecosystem.

Here's a summary of key takeaways to keep in mind:  

* **Clustering Unveils Hidden Structures:** K-Means can reveal meaningful groupings within your data that might not be immediately apparent. This is crucial for tasks like customer segmentation, anomaly detection, and even preliminary exploration before applying more complex models.  
* **Real-World Applications Abound:** Clustering isn't just theoretical. We've seen how it can be used in medical diagnostics (predicting heart disease risk based on patient attributes) and in pharmaceutical research (identifying patient subgroups responding differently to treatments). This demonstrates the algorithm's versatility across domains.  
* **Data Preprocessing is Key:** The quality of your clustering results depends heavily on how you prepare your data. Normalization and feature scaling are often essential steps to ensure that all features contribute equally to the clustering process.  
* **K-Means Isn't Perfect:** Remember that K-Means has its limitations. It assumes clusters are spherical and of equal size, which isn't always the case in real-world data. Additionally, choosing the optimal number of clusters (K) requires careful consideration and experimentation.  


**Looking Ahead: Beyond K-Means**

While K-Means is a great starting point, the world of clustering is vast. As you progress in your machine learning journey, you'll encounter more sophisticated algorithms like DBSCAN, hierarchical clustering, and Gaussian mixture models. Each has its own strengths and use cases.

Consider exploring these areas to expand your clustering toolkit:  

* **Dimensionality Reduction:** Techniques like PCA can help visualize high-dimensional clustered data.  
* **Cluster Evaluation:** Learn metrics like silhouette score to assess the quality of your clusters objectively.  
* **Ensemble Clustering:** Combining multiple clustering algorithms can often lead to more robust and accurate results.  

The knowledge you've gained here equips you to tackle a wide range of data analysis challenges. By applying clustering thoughtfully and critically, you can unlock valuable insights and drive data-driven decision-making.

## Additional Resources

## Feedback

@feedback
