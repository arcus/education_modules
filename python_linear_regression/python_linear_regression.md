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


    
### Python Implementation of Linear Regression

To implement linear regression in Python using Scikit-learn, we can follow these steps:



1. Import Libraries

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


2.  Load the data:

* `pd.read_csv("file")`: Reads data from a CSV file into a pandas DataFrame.
* `data.info()`: Gives a summary of the data such as column names, data types, and any missing values.

```python @Pyodide.exec

import pandas as pd
import io
from pyodide.http import open_url

url = "https://raw.githubusercontent.com/arcus/education_modules/linear_regression/python_linear_regression/data/healthcare_investments_and_hospital_stay.csv"

url_contents = open_url(url)
text = url_contents.read()
file = io.StringIO(text)

data = pd.read_csv(file)

# Analyze data and features
data.info()
```



3. **The `onehot_encode` Function**

   * This function handles categorical features (like "Location" in your data) by creating new columns where each column represents a unique category. The values are 1 if the data point belongs to that category and 0 otherwise.

```python
def onehot_encode(df, column):
    df = df.copy()
    dummies = pd.get_dummies(df[column])
    df = pd.concat([df, dummies], axis=1)
    df = df.drop(column, axis=1)
    return df
```
@Pyodide.eval

4. Make Data Copy and One-Hot Encode

* Creates a copy so we don't change the original data by accident.
* Applies one-hot encoding to the `Location` column.

```python
df = df.copy()
df = onehot_encode(df, column='Location')
```

5.  Separate Target and Features
* **y**: This is our target variable – what we want to predict (Hospital Stay).
* **X**: These are our features – the information we'll use to make the prediction.


```python
y = df['Hospital_Stay'].copy()
X = df.drop('Hospital_Stay', axis=1).copy()

```


6.  Split into Training and Testing Sets
* 70% of data is used for training (`X_train`, `y_train`).
* 30% is held back for testing (`X_test`, `y_test`).
* `random_state=123` ensures we get the same split each time for reproducibility.


```python
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=123)
```

7.  Standardize Features
* Calculates the mean and standard deviation of each feature in the training set.
* Scales both training and testing data to have zero mean and unit variance. This is often necessary for linear regression to work well.

```python
scaler = StandardScaler()
scaler.fit(X_train)
X_train = pd.DataFrame(scaler.transform(X_train), columns=X.columns)
X_test = pd.DataFrame(scaler.transform(X_test), columns=X.columns)
```

8.  Create and Train the Model
* Creates a linear regression object.
* Finds the best-fit line (or plane, in higher dimensions) by minimizing the difference between predicted and actual values in the training data.

```python
model = LinearRegression()
model.fit(X_train, y_train)
```
@Pyodide.eval

9.  Make Predictions
* Applies the model to the testing data to predict hospital stay.
```python
y_pred = model.predict(X_test)
```
@Pyodide.eval

10.  Evaluate the Model
* **Mean Squared Error (MSE):** A measure of how close the predictions are to the actual values on average. Lower is better.
* **R² Score:** Indicates the proportion of variance in the target variable that is explained by the model. Ranges from 0 to 1, with 1 being the best possible score.


```python
mse = np.mean((y_pred - y_test)**2)
print("MSE:", mse)
print(" R^2 Score: {:.5f}".format(model.score(X_test, y_test)))
```


This is a basic example of how to implement linear regression in Python using Scikit-learn. There are many other ways to implement linear regression in Python, but this is a good starting point.

Here are some additional tips for implementing linear regression in Python:

-   Make sure to scale the data before training the model. This will help to ensure that all features have equal importance in the model.
-   Use a validation set to evaluate the model and tune the hyperparameters. This will help to prevent overfitting.
-   Use regularization techniques, such as L1 or L2 regularization, to prevent overfitting.
-   Interpret the coefficients of the linear regression model to understand the relationship between the predictor variables and the target variable.
    








## Conclusion

By the end of this module, you'll have gained a solid grasp of linear regression as it is used in machine learning. You've learned how to implement and evaluate linear regression models using popular libraries like Scikit-learn. You've also seen how to apply these techniques to real-world datasets, both synthetic (healthcare investments) and established (diabetes dataset).

While the linear regression model for the diabetes dataset explains a reasonable amount of variance (51.8%), it's important to remember that real-world data analysis rarely ends with a single model. It's crucial to recognize the assumptions and limitations of linear regression. In the case of the diabetes dataset, further analysis is warranted to:

* **Explore potential nonlinear relationships:** The relationship between diabetes progression and the predictor variables might not be strictly linear.
* **Evaluate model assumptions:** Linear regression assumes specific relationships between variables (e.g., linearity, independence, homoscedasticity) that may not hold in the data.
* **Feature selection and engineering:** Some predictors might be more important than others. Feature engineering techniques could create new, more informative features.
* **Regularization:** Techniques like Ridge or Lasso regression could help prevent overfitting and improve model generalization.
* **Advanced models:** Non-linear regression or machine learning models like Random Forests or Gradient Boosting might offer better predictive performance.

This module is just the beginning of your journey into data analysis and machine learning. With the foundation you've built here, you're well-prepared to explore more advanced techniques and tackle complex data-driven challenges.

Remember, the key to successful data analysis is not just about applying algorithms, but also about understanding your data, asking the right questions, and critically evaluating your results. As you continue learning, keep exploring, experimenting, and refining your skills to become a proficient data scientist.


## Additional Resources

## Feedback

@feedback
