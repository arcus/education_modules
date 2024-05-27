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

Through this lesson, we've explored the fundamental concept of clustering as an unsupervised machine learning technique. We've delved into the inner workings of the K-Means algorithm, seeing how it iteratively groups similar data points together. We've also applied this knowledge to real-world scenarios, showcasing the potential of clustering in fields like customer segmentation and biomedical research.

However, clustering is not without its challenges. We've examined the importance of data preprocessing, including normalization, to ensure fair and accurate clustering results.  We've also discussed the limitations of clustering algorithms, such as sensitivity to initialization and the difficulty of determining the optimal number of clusters. By understanding these limitations, you're better equipped to make informed decisions and interpret clustering results with a critical eye.

With this foundational knowledge, you're now prepared to explore the wider landscape of clustering techniques, including variations like hierarchical clustering and density-based clustering. As you continue your journey in machine learning, remember that clustering is a versatile tool with far-reaching applications in data analysis, pattern recognition, and decision-making across diverse domains.

## Additional Resources

## Feedback

@feedback
