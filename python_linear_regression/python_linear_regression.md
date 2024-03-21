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

## What is linear regression?
- Linear regression is a supervised machine learning algorithm that learns to predict a continuous target variable based on one or more predictor variables. Linear regression models the relationship between the target variable and the predictor variables using a linear equation.
- In the case of linear regression, the target variable is a continuous variable. In a supervised learning problem, the machine learning algorithm is given a set of training data and asked to learn a function that can map the input variables to the output variable. The training data consists of pairs of input and output variables. The algorithm learns the function by finding the best fit line to the data. Once the algorithm has learned the function, it can be used to make predictions on new data. To make a prediction, the algorithm simply plugs the values of the input variables into the function.
- Linear regression is a popular supervised learning algorithm because it is simple to implement and understand. It is also a versatile algorithm that can be used to solve a variety of problems.

Which of the following is NOT a characteristic of linear regression?


[( )] Linear regression models the relationship between the target variable and the predictor variables using a linear equation.
[( )] Linear regression is a supervised learning algorithm.
[( )] Linear regression is a simple to implement and understand algorithm.
[(X)] Linear regression can be used to predict categorical variables.
[( )] Linear regression is a versatile algorithm that can be used to solve a variety of problems.
***
<div class = "answer">

This question is more difficult than the previous one because it requires the test-taker to have a deeper understanding of the characteristics of linear regression. The test-taker must be able to identify which of the answer choices is not a characteristic of linear regression, even though all of the other answer choices are valid characteristics.

</div>
***


### Applications of linear regression in machine learning
Linear Regression can be used for a variety of tasks, such as: 

-   **Prediction:**  Linear regression can be used to predict a wide range of continuous variables, such as house prices, stock prices, customer churn, and medical outcomes.
-   **Recommendation:**  Linear regression can be used to build recommender systems that recommend products, movies, or other items to users based on their past preferences.
-   **Fraud detection:**  Linear regression can be used to detect fraudulent transactions by identifying transactions that deviate from the expected behavior.
-   **Medical diagnosis:**  Linear regression can be used to help doctors diagnose diseases by identifying patterns in patient data.
-   **Scientific research:**  Linear regression can be used to identify relationships between variables in scientific data.
### Examples of linear regression in real-world applications
-   **Predicting house prices:**  Linear regression can be used to predict the price of a house based on its square footage, number of bedrooms, number of bathrooms, and other factors.
-   **Predicting stock prices:**  Linear regression can be used to predict the price of a stock based on its historical prices, financial data, and other factors.
-   **Predicting customer churn:**  Linear regression can be used to predict whether a customer is likely to churn based on their past purchase history, demographics, and other factors.
-   **Predicting the risk of a customer defaulting on a loan:**  Linear regression can be used to predict the risk of a customer defaulting on a loan based on their credit score, income, and other factors.
-   **Predicting the likelihood of a patient having a particular disease:**  Linear regression can be used to predict the likelihood of a patient having a particular disease based on their medical history, symptoms, and other factors.
-   **Predicting the number of visitors to a website:**  Linear regression can be used to predict the number of visitors to a website based on the website's past traffic data, marketing campaigns, and other factors.
-   **Predicting the sales of a product:**  Linear regression can be used to predict the sales of a product based on its price, marketing campaigns, and other factors.

## Linear Regression Algorithm
Linear regression works by fitting a linear equation to the data.

The linear equation is represented by the following formula: 

```
y = b0 + b1 * x1 + b2 * x2 + ... + bn * xn
``` 

where:  

- `y` is the target variable
- `b0` is the bias term
- `bi` is the coefficient for the ith predictor variable
- `xi` is the ith predictor variable

The coefficients of the linear equation are estimated using the ordinary least squares (OLS) method. The OLS method minimizes the sum of the squared residuals, which are the differences between the predicted values and the actual values of the target variable. Once the linear regression model is trained, it can be used to make predictions on new data. To make a prediction, we simply plug the values of the predictor variables into the linear equation. 

Which of the following is NOT a component of the linear regression formula?


[( )] Target variable
[( )] Bias term
[( )] Coefficient for the ith predictor variable
[( )] ith predictor variable
[(X)] Variance of the target variable
***
<div class = "answer">

The variance of the target variable is not a component of the linear regression formula. The linear regression formula is used to predict the mean value of the target variable, not the variance.

</div>
***


    
### Python Implementation of Linear Regression

To implement linear regression in Python using Scikit-learn, we can follow these steps:



1.  Import the necessary libraries:
```python
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
```
@Pyodide.eval


2.  Load the data:
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

3.  Split the data into training and testing sets:
```python

# Encode categorical data into numbers
def onehot_encode(df, column):
    df = df.copy()
    dummies = pd.get_dummies(df[column])
    df = pd.concat([df, dummies], axis=1)
    df = df.drop(column, axis=1)
    return df

def preprocess_inputs(df):
    df = df.copy()
    
    # One-hot encode Location column
    df = onehot_encode(df, column='Location')
    
    # Split df into X and y
    y = df['Hospital_Stay'].copy()
    X = df.drop('Hospital_Stay', axis=1).copy()
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=123)
    
    # Scale X with a standard scaler
    scaler = StandardScaler()
    scaler.fit(X_train)
    
    X_train = pd.DataFrame(scaler.transform(X_train), columns=X.columns)
    X_test = pd.DataFrame(scaler.transform(X_test), columns=X.columns)
    
    return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = preprocess_inputs(data)

```
@Pyodide.eval

4.  Train the linear regression model:
```python
# Create a linear regression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)
```
@Pyodide.eval

5.  Evaluate the model on the testing set:
```python
# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model using the mean squared error (MSE)
mse = np.mean((y_pred - y_test)**2)

# Print the MSE
print("MSE:", mse)

# Evaluate R^2 Score
print(" R^2 Score: {:.5f}".format(model.score(X_test, y_test)))
```
@Pyodide.eval


This is a basic example of how to implement linear regression in Python using Scikit-learn. There are many other ways to implement linear regression in Python, but this is a good starting point.

Here are some additional tips for implementing linear regression in Python:

-   Make sure to scale the data before training the model. This will help to ensure that all features have equal importance in the model.
-   Use a validation set to evaluate the model and tune the hyperparameters. This will help to prevent overfitting.
-   Use regularization techniques, such as L1 or L2 regularization, to prevent overfitting.
-   Interpret the coefficients of the linear regression model to understand the relationship between the predictor variables and the target variable.
    

### Applying Linear Regression to a Real-World Dataset
To apply linear regression to a real-world dataset, we can follow these steps: 

- **Choose a dataset:** The dataset should have at least one continuous target variable and one or more predictor variables. 
- **Prepare the data:** This may involve cleaning the data, handling missing values, and scaling the data. 
- **Split the data into training and testing sets:** This will help to prevent overfitting.
- **Train the linear regression model:** Use the training set to fit the model to the data. 
- **Evaluate the model on the testing set:** This will give you an estimate of how well the model will generalize to new data. 
- **Interpret the results:** Examine the coefficients of the model to understand the relationship between the predictor variables and the target variable. 
- **Make predictions on new data:** Use the trained model to make predictions on new data points.

### Important Notes
Linear regression is a powerful machine learning algorithm, but it has some limitations. Here are some of the most important limitations of linear regression: 

- **Linearity assumption:** Linear regression assumes that the relationship between the target variable and the predictor variables is linear. If the relationship is non-linear, then linear regression will not be able to accurately predict the target variable.
- **Overfitting:** Linear regression is prone to overfitting, which occurs when the model learns the training data too well and is unable to generalize to new data. Overfitting can be prevented by using regularization techniques such as L1 or L2 regularization.
- **Outliers:** Linear regression is sensitive to outliers, which are data points that are significantly different from the rest of the data. Outliers can have a large impact on the parameters of the linear regression model and can lead to inaccurate predictions.
- **Collinearity:** Linear regression is also sensitive to collinearity, which occurs when two or more predictor variables are highly correlated with each other. Collinearity can make it difficult to interpret the results of the linear regression model and can lead to inaccurate predictions.

[True/False] Linear regression is sensitive to collinearity.


[(X)] True
[( )] False
***
<div class = "answer">

This question is designed to test the test-taker's understanding of the concept of collinearity and its impact on linear regression models. Collinearity is a serious problem in linear regression because it can make it difficult to interpret the results of the model and can lead to inaccurate predictions.

</div>
***


[True/False] Overfitting can be prevented by using regularization techniques.


[(X)] True
[( )] False
***
<div class = "answer">

This question is designed to test the test-taker's understanding of the concept of overfitting and how to prevent it. Overfitting is a common problem in machine learning, and it is important to be able to identify and prevent it. Regularization techniques such as L1 and L2 regularization can be used to prevent overfitting in linear regression models.

</div>
***




### Real World Code Example

The Streptomycin for Tuberculosis dataset originates from a groundbreaking clinical trial published in 1948, often recognized as the first modern randomized clinical trial. It comprises data from a prospective, randomized, placebo-controlled study investigating the efficacy of streptomycin treatment for pulmonary tuberculosis. The dataset includes variables such as participant ID, study arm (Streptomycin or Control), doses of Streptomycin and Para-Amino-Salicylate in grams, gender, baseline conditions (categorized as good, fair, or poor), oral temperature at baseline, erythrocyte sedimentation rate at baseline, presence of lung cavitation on chest X-ray at baseline, streptomycin resistance at 6 months, radiologic outcomes at 6 months, numeric rating of chest X-ray at month 6, and a dichotomous outcome indicating improvement. These variables provide comprehensive information for analyzing the effectiveness of streptomycin treatment for tuberculosis, allowing for various statistical analyses such as logistic regression modeling.



1.  Install Packages:
```python @Pyodide.exec

import pandas as pd
import io
from pyodide.http import open_url
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error





```

2.  Load the data:
```python
# Load dataset and read to pandas dataframe
url = "https://raw.githubusercontent.com/arcus/education_modules/linear_regression/python_linear_regression/data/strep_tb.csv"

url_contents = open_url(url)
text = url_contents.read()
file = io.StringIO(text)
df = pd.read_csv(file)

# Analyze data and features
df.info()

# Encode Categorical Features
categorical_cols = [
    'arm', 'gender', 'baseline_condition', 'baseline_temp',
    'baseline_esr', 'baseline_cavitation', 'strep_resistance', 'radiologic_6m'
]
 # Create a LabelEncoder for transforming columns
le = LabelEncoder() 

# Apply label encoding to each categorical column
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])
```
@Pyodide.eval


3.  Compute Regression:
```python
# Feature Selection and Target Definition
features = [
    'patient_id', 'arm', 'dose_strep_g', 'dose_PAS_g', 'gender',
    'baseline_condition', 'baseline_temp', 'baseline_esr',
    'baseline_cavitation', 'strep_resistance', 'radiologic_6m', 'rad_num'
]
target = 'improved'

# Separate inputs (features) and output (target variable)
inputs = df[features]
output = df[target]

# SECTION 4: Linear Regression Modeling
model = LinearRegression()  # Create the regression model
model.fit(inputs, output)   # Train the model 
```
@Pyodide.eval


4.  Evaluate Model:
```python
# Predict data
predictions = model.predict(inputs) 

# Analyze predictions
print('R-squared:', r2_score(output, predictions))  
print('Mean Squared Error:', mean_squared_error(output, predictions))  
```
@Pyodide.eval

The results obtained from the Streptomycin for Tuberculosis dataset reveal promising findings regarding the efficacy of streptomycin treatment for pulmonary tuberculosis. Originating from a groundbreaking clinical trial in 1948, widely acknowledged as the first modern randomized clinical trial, this dataset offers a rich array of variables encompassing participant demographics, treatment dosages, baseline conditions, and clinical outcomes. The R-squared value of 0.834306790075451 indicates that the linear regression model explains approximately 83.4% of the variance in the outcome variable, showcasing a strong fit of the model to the data. Additionally, the low Mean Squared Error of 0.04139073983616123 suggests that the model's predictions are relatively accurate. However, it's essential to recognize that linear regression serves as an initial step in analyzing this dataset. While these results provide valuable insights, further analyses employing advanced statistical techniques such as logistic regression modeling are warranted to fully comprehend the effectiveness of streptomycin treatment for tuberculosis management.




## Conclusion

At the end of the lesson, students should have a good understanding of the concept of linear regression and how to implement the linear regression algorithm in Python. They should also be able to apply linear regression to real-world datasets to make predictions and insights.

## Additional Resources

## Feedback

@feedback
