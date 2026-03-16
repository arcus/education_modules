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

title: Python Lesson on Regression for Machine Learning

comment:  Understand the basics of linear regression, including how it works and when to use it in Python.

long_description: Understand linear regression in Python as a powerful and versatile tool that can be used to solve a wide variety of problems. By understanding the key concepts and techniques involved in linear regression, you can build and deploy models that can accurately predict the target variable of interest.

estimated_time_in_minutes: 20

@pre_reqs

This module assumes learners have been exposed to introductory statistics, Algebra, and probability.
There are coding exercises in Python, so programming experience is required.

@end

@learning_objectives  

-   Understand the concept of linear regression and its applications in machine learning
-   Learn how to implement the linear regression algorithm in Python
-   Apply linear regression to a real-world dataset

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

# Python Lesson on Regression for Machine Learning

@overview


## Summary of Key Concepts in Linear Regression

- **Definition**: Linear regression is a statistical method used to model and analyze the relationships between a dependent variable and one or more independent variables.

- **Applications**: Commonly used in machine learning to predict continuous outcomes.
  
- **Practical Application**:
  - Applying linear regression to real-world datasets, such as synthetic healthcare investments and the diabetes dataset.
  
- **Evaluation and Beyond**:
  - Recognize model limitations and explore further analysis, such as:
    - Nonlinear relationships.
    - Model assumptions.
    - Feature selection and engineering.
    - Regularization techniques (Ridge, Lasso).
    - Advanced models (Random Forests, Gradient Boosting).


- Linear regression is a starting point for data analysis and machine learning.
- The foundation built here prepares you for advanced techniques and complex challenges.
- Success in data analysis involves understanding data, asking the right questions, and critically evaluating results.



    
## Python Implementation of Linear Regression

To implement linear regression in Python using Scikit-learn, we can follow these steps:



### 1. Import Libraries
**Description**:
This code block imports necessary libraries for data manipulation and machine learning tasks. Specifically, it imports NumPy for numerical operations, Pandas for data manipulation, and scikit-learn (sklearn) for machine learning functionalities.

**Why this is important:**1
Importing libraries is the first step in any data analysis or machine learning project. These libraries provide tools and functions to efficiently handle data, perform mathematical operations, and build machine learning models.

* **numpy (np):** Provides tools for working with numerical arrays and mathematical operations.
* **pandas (pd):** Enables data manipulation and analysis with data structures like DataFrames.
* **sklearn:** A powerful machine learning library. We specifically use:
  * `train_test_split`: Splits data into training (model building) and testing (model evaluation) sets.
  * `StandardScaler`: Standardizes features to have zero mean and unit variance (often important for linear regression).
  * `LinearRegression`: The core linear regression model.


```python
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
```
@Pyodide.eval


**Output:**
There's no output generated from this code block. It simply imports the required libraries for subsequent steps in the machine learning workflow.



### 2.  Load the data:

**Description:**  

* `pd.read_csv("file")`: Reads data from a CSV file into a pandas DataFrame.  
* `data.info()`: Gives a summary of the data such as column names, data types, and any missing values.  

**Why this is important:**
Loading the data is the initial step in any data analysis or machine learning task. It's essential to understand the structure of the data, such as the number of features and their data types, before proceeding with further analysis.

```python @Pyodide.exec

import pandas as pd
import io
from pyodide.http import open_url

# URL of the CSV file
url = "https://raw.githubusercontent.com/arcus/education_modules/linear_regression/python_linear_regression/data/healthcare_investments_and_hospital_stay.csv"

# Open and read the contents of the URL
url_contents = open_url(url)
text = url_contents.read()

# Create a file-like object from the text content
file = io.StringIO(text)

# Read the CSV data into a pandas DataFrame
data = pd.read_csv(file)

# Analyze data and features
data.info()
```

**Output:**
After executing this code block, you will see a summary of the loaded data, including information about columns, data types, and non-null values. This helps them understand the dataset they will be working with.





### 3. **The `onehot_encode` Function**

**Description:**

   * This function handles categorical features (like "Location" in your data) by creating new columns where each column represents a unique category. The values are 1 if the data point belongs to that category and 0 otherwise.

**Why this is important:**
One-hot encoding is crucial when dealing with categorical data in machine learning models. Many machine learning algorithms cannot directly handle categorical data, so encoding them into numerical values allows algorithms to operate on the data effectively. By creating binary columns for each category, we ensure that each category is treated equally, without imposing any ordinality or magnitude among them.


```python
def onehot_encode(df, column):
    # Make a copy of the DataFrame to avoid modifying the original data
    df = df.copy()
    
    # Use pandas get_dummies function to one-hot encode the specified column
    dummies = pd.get_dummies(df[column])
    
    # Concatenate the one-hot encoded columns with the original DataFrame
    df = pd.concat([df, dummies], axis=1)
    
    # Drop the original categorical column since it's no longer needed
    df = df.drop(column, axis=1)
    
    return df
```
@Pyodide.eval





### 4. Make Data Copy and One-Hot Encode

**Description:**
The code creates a copy of the DataFrame df to ensure that the original data remains unchanged. It then applies one-hot encoding to the Location column using the onehot_encode function.

**Why this is important:**
Creating a copy of the DataFrame is essential to prevent unintentional modifications to the original data, which could lead to unexpected results or loss of information. One-hot encoding is necessary to convert categorical variables, such as the Location column, into numerical format, which is required for many machine learning algorithms to operate effectively.

* Creates a copy so we don't change the original data by accident.
* Applies one-hot encoding to the `Location` column.

```python
# Make a copy of the DataFrame to avoid modifying the original data accidentally
df = df.copy()

# Apply one-hot encoding to the 'Location' column
df = onehot_encode(df, column='Location')

# Print the resulting DataFrame to observe the effect of one-hot encoding
print(df.head())
```
**Output:**
While this code snippet itself does not produce direct output, we can demonstrate its usage by applying it to a DataFrame and printing the resulting DataFrame to observe the effect of one-hot encoding.




### 5.  Separate Target and Features
**Description:**

* This code snippet separates the target variable (`Hospital_Stay`) from the features in the DataFrame df.
* The target variable (`y`) is what we want to predict, while the features (`X`) are the information we'll use to make the prediction.

**Why this is important:**

* Separating the target variable from the features is a crucial step in machine learning model training.
* The target variable is the variable we aim to predict, while the features are the input variables that influence the prediction.
* By separating them, we ensure that the model trains on the features to predict the target accurately.


```python
# Separate the target variable 'Hospital_Stay' from the features
y = df['Hospital_Stay'].copy()
X = df.drop('Hospital_Stay', axis=1).copy()

# Print the target variable and features to verify the separation
print("Target variable (y):")
print(y.head())
print("\nFeatures (X):")
print(X.head())

```

**Output:**
While this code snippet doesn't produce any visible output, we can verify the separation by printing the y (target variable) and X (features) variables.



### 6.  Split into Training and Testing Sets
**Description:**
The `train_test_split` function divides the dataset into training and testing sets. Here, 70% of the data is used for training `(X_train, y_train)`, and the remaining 30% is held back for testing `(X_test, y_test)`.

**Why this is important:**
Splitting the data into training and testing sets is crucial in machine learning to assess the performance of the model. The training set is used to train the model, while the testing set is used to evaluate its performance on unseen data. This helps to detect overfitting and ensures that the model generalizes well to new data.

* `random_state=123` ensures we get the same split each time for reproducibility.


```python
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=123)

# Print the shapes of the resulting training and testing sets
print("Training set - X shape:", X_train.shape, "y shape:", y_train.shape)
print("Testing set - X shape:", X_test.shape, "y shape:", y_test.shape)

```
**Output:**
While this code block doesn't produce any output directly, we can demonstrate its usage by applying it to our data and printing the shapes of the resulting training and testing sets to confirm the split.


### 7.  Standardize Features
**Description:**

* The code initializes a `StandardScaler` object, which will be used to standardize (or z-score normalize) the features.
* It then fits the scaler to the training data (`X_train`), calculating the mean and standard deviation of each feature in the training set.
* Finally, it scales both the training and testing data to have zero mean and unit variance using the fitted scaler. This ensures that both datasets are scaled in the same way.

**Why this is important:**
Standardizing features is crucial, especially when working with algorithms that rely on distance metrics or gradient descent optimization, such as KNN, SVM, or logistic regression. By standardizing the features, we remove the mean and scale the data to unit variance, which can improve the convergence rate of optimization algorithms and prevent features with larger scales from dominating those with smaller scales.

```python
# Initialize a StandardScaler object
scaler = StandardScaler()

# Fit the scaler to the training data, calculating the mean and standard deviation of each feature
scaler.fit(X_train)

# Scale both training and testing data to have zero mean and unit variance
X_train = pd.DataFrame(scaler.transform(X_train), columns=X.columns)
X_test = pd.DataFrame(scaler.transform(X_test), columns=X.columns)

# Print the scaled training and testing data to observe the effect of standardization
print("Scaled Training Data:")
print(X_train.head())
print("\nScaled Testing Data:")
print(X_test.head())
```

**Output:**
While this code block doesn't produce any output directly, learners can observe the effect of standardization by printing the scaled `X_train` and `X_test` datasets after applying the scaler.



### 8.  Create and Train the Model
**Description:**

* This code segment creates a linear regression object using the `LinearRegression` class from the scikit-learn library.
* It then fits the model to the training data, finding the best-fit line (or plane, in higher dimensions) by minimizing the difference between predicted and actual values in the training data.

**Why this is important:**
Creating and training a model is the core of supervised machine learning. In this step, we instantiate a regression model and train it on our training data to learn the underlying patterns and relationships between the input features (`X`) and the target variable (`y`). This trained model will later be used to make predictions on new, unseen data.

```python
# Create a Linear Regression model object
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)
```
@Pyodide.eval



### 9.  Make Predictions
**Description:**
This line applies the trained machine learning model (`model`) to the testing data (`X_test`) to make predictions about hospital stay durations.

**Why this is important:**
Making predictions is the ultimate goal of any machine learning model. By applying the trained model to new, unseen data, we can obtain predictions that can be used for decision-making or further analysis.

```python
# Make predictions using the trained model and the testing data
y_pred = model.predict(X_test)

# Print the predicted hospital stay durations
print(y_pred)
```
@Pyodide.eval

**Output:**
While this line doesn't produce output directly, we can add a print statement to display the predictions generated by the model.



### 10.  Evaluate the Model
**Description:**

The code calculates and prints two evaluation metrics for the regression model:

* Mean Squared Error (MSE): A measure of how close the predictions are to the actual values on average. Lower values indicate better performance.
* R² Score: Indicates the proportion of variance in the target variable that is explained by the model. Ranges from 0 to 1, with 1 being the best possible score.

**Why this is important:**
Evaluating the model's performance is crucial to understand how well it is generalizing to unseen data. The Mean Squared Error provides a quantitative measure of the model's prediction accuracy, while the R² Score gives insight into the goodness of fit of the model.


```python
mse = np.mean((y_pred - y_test)**2)
print("MSE:", mse)
print(" R^2 Score: {:.5f}".format(model.score(X_test, y_test)))
```

**Output:**
This code snippet produces output showing the calculated MSE and R² Score, providing insights into the model's performance.


### Code Overview and Tips
This is a basic example of how to implement linear regression in Python using Scikit-learn. There are many other ways to implement linear regression in Python, but this is a good starting point.

Here are some additional tips for implementing linear regression in Python:

-   Make sure to scale the data before training the model. This will help to ensure that all features have equal importance in the model.
-   Use a validation set to evaluate the model and tune the hyperparameters. This will help to prevent overfitting.
-   Use regularization techniques, such as L1 or L2 regularization, to prevent overfitting.
-   Interpret the coefficients of the linear regression model to understand the relationship between the predictor variables and the target variable.
    



## Review your knowledge

Which function from Scikit-learn is used to split the dataset into training and testing sets?


A) data_splitter
B) train_test_split
C) train_validate_split
D) model_splitter


[( )]  `data_splitter`
[(X)] `train_test_split`
[( )] `train_validate_split`
[( )] `model_splitter`
***
<div class = "answer">

The `train_test_split` function from Scikit-learn is used to split the dataset into training and testing sets. This function is essential for evaluating the performance of a machine learning model by training it on one subset of the data and testing it on another.


</div>








## Conclusion

### Key Takeaways
By the end of this module, you'll have gained a solid grasp of linear regression as it is used in machine learning. You've learned how to implement and evaluate linear regression models using popular libraries like Scikit-learn. You've also seen how to apply these techniques to real-world datasets, both synthetic (healthcare investments) and established (diabetes dataset).

While the linear regression model for the diabetes dataset explains a reasonable amount of variance (51.8%), it's important to remember that real-world data analysis rarely ends with a single model.

### Beyond Linear Regression
**Further Analysis Needed:**  

* **Explore potential nonlinear relationships:** The relationship between diabetes progression and the predictor variables might not be strictly linear.
* **Evaluate model assumptions:** Linear regression assumes specific relationships between variables (e.g., linearity, independence, homoscedasticity) that may not hold in the data.
* **Feature selection and engineering:** Some predictors might be more important than others. Feature engineering techniques could create new, more informative features.
* **Regularization:** Techniques like Ridge or Lasso regression could help prevent overfitting and improve model generalization.
* **Advanced models:** Non-linear regression or machine learning models like Random Forests or Gradient Boosting might offer better predictive performance.

This module is just the beginning of your journey into data analysis and machine learning. With the foundation you've built here, you're well-prepared to explore more advanced techniques and tackle complex data-driven challenges.

Remember, the key to successful data analysis is not just about applying algorithms, but also about understanding your data, asking the right questions, and critically evaluating your results. As you continue learning, keep exploring, experimenting, and refining your skills to become a proficient data scientist.


## Additional Resources

### Full Code Implementation

At the end of this module, here you will find a "Full Code" section where all the code is consolidated into a single cell block. This allows for easy copying and pasting for those who want to implement the entire process quickly. While this single block of code isn't designed as a step-by-step educational tool, it serves as a convenient reference for future use and helps streamline the process for those already familiar with the concepts. Below is the complete code implementation:


```python
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

def onehot_encode(df, column):
    # Make a copy of the DataFrame to avoid modifying the original data
    df = df.copy()
    
    # Use pandas get_dummies function to one-hot encode the specified column
    dummies = pd.get_dummies(df[column])
    
    # Concatenate the one-hot encoded columns with the original DataFrame
    df = pd.concat([df, dummies], axis=1)
    
    # Drop the original categorical column since it's no longer needed
    df = df.drop(column, axis=1)
    
    return df

# URL of the CSV file
url = "https://raw.githubusercontent.com/arcus/education_modules/linear_regression/python_linear_regression/data/healthcare_investments_and_hospital_stay.csv"

# Open and read the contents of the URL
url_contents = open_url(url)
text = url_contents.read()

# Create a file-like object from the text content
file = io.StringIO(text)

# Read the CSV data into a pandas DataFrame
data = pd.read_csv(file)

# Analyze data and features
data.info()

# Make a copy of the DataFrame to avoid modifying the original data accidentally
df = data.copy()

# Apply one-hot encoding to the 'Location' column
df = onehot_encode(df, column='Location')

# Print the resulting DataFrame to observe the effect of one-hot encoding
print(df.head())

# Separate the target variable 'Hospital_Stay' from the features
y = df['Hospital_Stay'].copy()
X = df.drop('Hospital_Stay', axis=1).copy()

# Print the target variable and features to verify the separation
print("Target variable (y):")
print(y.head())
print("\nFeatures (X):")
print(X.head())

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=123)

# Print the shapes of the resulting training and testing sets
print("Training set - X shape:", X_train.shape, "y shape:", y_train.shape)
print("Testing set - X shape:", X_test.shape, "y shape:", y_test.shape)

# Initialize a StandardScaler object
scaler = StandardScaler()

# Fit the scaler to the training data, calculating the mean and standard deviation of each feature
scaler.fit(X_train)

# Scale both training and testing data to have zero mean and unit variance
X_train = pd.DataFrame(scaler.transform(X_train), columns=X.columns)
X_test = pd.DataFrame(scaler.transform(X_test), columns=X.columns)

# Print the scaled training and testing data to observe the effect of standardization
print("Scaled Training Data:")
print(X_train.head())
print("\nScaled Testing Data:")
print(X_test.head())

# Create a Linear Regression model object
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions using the trained model and the testing data
y_pred = model.predict(X_test)

# Print the predicted hospital stay durations
print(y_pred)

# Calculate Mean Squared Error (MSE)
mse = np.mean((y_pred - y_test)**2)

# Print MSE
print("MSE:", mse)

# Calculate and print R² Score
print("R² Score:", model.score(X_test, y_test))
```

## Feedback

@feedback
