<!--

module_id: intro_linear_regression_ml
author:   Daniel Schwartz
email:    des338@drexel.edu
version:  0.0.0
current_version_description: Initial version
module_type: standard
docs_version: 4.0.0
language: en
narrator: UK English Female
mode: Textbook

title: Intro to Linear Regression for Machine Learning

comment:  Understand the basics of linear regression within the context of machine learning.

long_description: Understand linear regression is a powerful and versatile tool that can be used to solve a wide variety of problems. By understanding the key concepts and techniques involved in linear regression, you can build and deploy models that can accurately predict the target variable of interest.

estimated_time_in_minutes: 20

@pre_reqs

This module assumes learners have been exposed to introductory statistics, Algebra, and probability.

@end

@learning_objectives  

- Understand the concept of linear regression 
- applications in machine learning

@end

good_first_module: false
data_task: data_analysis
collection: machine_learning
coding_required: false

@sets_you_up_for
- python_linear_regression
@end

@depends_on_knowledge_available_in
- demystifying_machine_learning
- intro_to_nhst
@end

@version_history 
No previous versions.
@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
-->

# Intro to Linear Regression for Machine Learning

@overview

## What is linear regression?
- Linear regression is a supervised machine learning algorithm that learns to predict a continuous target variable based on one or more predictor variables. Linear regression models the relationship between the target variable and the predictor variables using a linear equation.
- In the case of linear regression, the target variable is a continuous variable. In a supervised learning problem, the machine learning algorithm is given a set of training data and asked to learn a function that can map the input variables to the output variable. The training data consists of pairs of input and output variables. The algorithm learns the function by finding the best fit line to the data. Once the algorithm has learned the function, it can be used to make predictions on new data. To make a prediction, the algorithm simply plugs the values of the input variables into the function.
- Linear regression is a popular supervised learning algorithm because it is simple to implement and understand. It is also a versatile algorithm that can be used to solve a variety of problems.

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

As in many fields, machine learning involves a lot of technical language, some of which is unclear, redundant, or downright confusing.
For example:

**Outcome** variables are also called **response variables**, **dependent variables**, or **labels**.

**Input** variables are also called **predictors**, **features**, **independent variables**, or even just **variables**.

To make matters worse, sometimes the same words are used to mean different things in different subfields.
If you find yourself stumbling on vocabulary as you read about machine learning, know you're not alone!

</div>

Which of the following is NOT a characteristic of linear regression?


[( )] Linear regression models the relationship between the target variable and the predictor variables using a linear equation.
[( )] Linear regression is a supervised learning algorithm.
[( )] Linear regression is a simple to implement and understand algorithm.
[(X)] Linear regression can be used to predict categorical variables.
[( )] Linear regression is a versatile algorithm that can be used to solve a variety of problems.
***
<div class = "answer">

This question presents a deeper challenge as it requires a solid understanding of linear regression's characteristics. To answer correctly, you need to identify the feature that doesn't align with linear regression. The incorrect option, "Linear regression can be used to predict categorical variables," deviates from the typical usage of linear regression, which is primarily for continuous variables. Understanding this distinction enhances your comprehension of linear regression's scope and limitations.

</div>
***


### Applications of linear regression in biomedical research
Linear regression finds extensive application in biomedical research, offering insights into various domains, such as:

- **Disease prognosis:** Linear regression aids in predicting the progression of diseases based on patient demographics, biomarkers, and clinical data. For instance, it can forecast the advancement of cancer stages or the deterioration of chronic conditions like diabetes.  
    - A specific example of this in research can be found in ["A longitudinal study defined circulating microRNAs as reliable biomarkers for disease prognosis and progression in ALS human patients"](https://www.nature.com/articles/s41420-020-00397-6) In the realm of disease prognosis, longitudinal research has illuminated the potential of circulating microRNAs as dependable biomarkers for assessing disease progression and prognosis in ALS patients. By integrating patient demographics, biomarkers, and clinical data, linear regression models can be leveraged to forecast the trajectory of diseases, akin to predicting cancer stages or the progression of chronic ailments like diabetes.  

- **Treatment efficacy:** Linear regression assists in evaluating the effectiveness of medical treatments by analyzing patient response data. Researchers can utilize it to assess the impact of medications, therapies, or interventions on disease outcomes and patient well-being.  
    - ["Meta-analysis of the Age-Dependent Efficacy of Multiple Sclerosis Treatments"](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2017.00577/full) demonstrates a specific application of linear regression.  This study uses linear regression to determine how the effectiveness of Multiple Sclerosis treatments changes as patients age.  


- **Genetic studies:** Linear regression plays a pivotal role in genetic research by exploring associations between genetic variants and phenotypic traits. It helps identify genetic markers linked to disease susceptibility, treatment response, and disease progression, contributing to personalized medicine approaches.  
    - The article ["Prediction of Gene Expression Patterns With Generalized Linear Regression Model"](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2019.00120/full) describes a method using generalized linear regression to predict how gene expression levels change in response to the binding intensity of the Oct4 transcription factor. This model aids researchers in understanding the complex regulatory mechanisms behind cell reprogramming and development.  

- **Public health analysis:** Linear regression facilitates the analysis of population-level health trends, aiding in the identification of risk factors, disease clusters, and health disparities. It enables researchers to model the impact of interventions, policies, and socio-economic factors on public health outcomes.  
    - The article ["Regression Analysis for COVID-19 Infections and Deaths Based on Food Access and Health Issues"](https://www.mdpi.com/2227-9032/10/2/324) investigates the relationship between food access, pre-existing health conditions, and the severity of COVID-19 outcomes. Researchers used regression models to discover potential correlations that could inform future pandemic preparedness efforts.

- **Epidemiological modeling:** Linear regression serves as a fundamental tool in epidemiology for modeling disease spread and understanding risk factors. It assists in forecasting disease outbreaks, estimating transmission rates, and evaluating interventions' effectiveness in controlling infectious diseases.  
    - The article ["SEIR and Regression Model based COVID-19 outbreak predictions in India"](https://arxiv.org/abs/2004.00958) utilizes a combination of SEIR modeling and regression analysis to forecast COVID-19 outbreaks in India, providing valuable insights into disease spread dynamics. This approach contributes to epidemiological modeling by showcasing how linear regression, alongside SEIR models, aids in predicting disease outbreaks, estimating transmission rates, and assessing the effectiveness of interventions, thereby informing proactive measures to control infectious diseases.



By leveraging linear regression in these contexts, biomedical researchers can glean valuable insights into disease mechanisms, treatment strategies, and public health interventions, ultimately advancing healthcare practices and improving patient outcomes.

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

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

To learn more about Linear Regression and for a visual explanation, watch [Linear Regression, Clearly Explained!!!](https://www.youtube.com/watch?v=nk2CQITm_eo).

</div>

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

### Understanding Machine Learning Techniques

Before diving into the example, it's valuable to understand some key concepts used in machine learning. These techniques help us build more accurate and reliable models for prediction.

- **Splitting Data (Training and Testing):**  Machine learning models 'learn' from data. We divide our dataset into two parts:  

    - **Training set:** This part is used to train the model, allowing it to find patterns. 

- **Testing set:** This is held-out data used to evaluate how well our model performs on unseen examples. This prevents overfitting, where the model becomes too specific to the training data and performs poorly on new data.  

- **Recoding Categorical Predictors:** Many machine learning models work best with numerical data. Categorical features (like 'gender' or 'treatment group') need to be converted into numbers. Label encoding is a common technique, where each category is assigned a unique numerical label.  
- **Scaling Continuous Predictors:** When features have vastly different scales (e.g., age vs. body temperature), some models might be biased towards features with larger ranges. Scaling brings features into a similar range, often between 0 and 1, or standardizing them to have a mean of 0 and a standard deviation of 1. This ensures all features are treated fairly during training.  
- **Evaluating Model Predictions (MSE):** To assess the performance of a model, we use these metrics:  

    - **Mean Squared Error (MSE):** This calculates the average of the squared differences between the model's predictions and the actual true values. A lower MSE indicates that a model's predictions are generally closer to the real targets.  
    
    - MSE and Outliers: MSE is sensitive to outliers because squaring the errors emphasizes larger deviations.
    
- **R-squared (R²):** This represents the proportion of the variance in the dependent variable that can be explained by the independent variables in the model.  It ranges from 0 to 1.  A higher R-squared value suggests a better model fit, meaning your model is doing a better job of explaining the variation in the data.  
    
    - R-squared and Additional Variables: R-squared tends to increase as you add more variables to your model, even if those variables don't actually improve the model's explanatory power. To address this, you can use the Adjusted R-squared, which takes the number of variables into account.

#### Why do we use these techniques?

- **Improved Accuracy:** These steps help our model identify true patterns and relationships within the data and not just memorize specific examples from the training set.  
- **Preventing Overfitting:** By testing the model on unseen data, we ensure it generalizes well to new situations.  
- **Fair Feature Influence:** Scaling makes sure no single feature dominates the model's predictions due to differences in measurement ranges.  

Here are some additional tips for implementing linear regression:

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

This is because of a condition called collinearity. Here's why it matters:  
- Understanding the impact: When two or more of your predictor variables are highly correlated (meaning they change in similar ways), it becomes difficult for linear regression to figure out which variable is really affecting the outcome.  
- Less reliable results: Collinearity can make the estimates for your model's coefficients less stable. A small change in your data might lead to big changes in how the model interprets the relationship between the variables.  
- Tricky interpretation: It becomes harder to say with confidence how much a change in one specific predictor variable will impact the outcome you're trying to predict.  

Key Takeaway: It's a good idea to be aware of collinearity and check for it before building a linear regression model.  

</div>
***


[True/False] Overfitting can be prevented by using regularization techniques.


[(X)] True
[( )] False
***
<div class = "answer">

Regularization techniques are designed to combat overfitting. Let's break down why:  

- Overfitting: Occurs when a machine learning model learns the training data too well, including the noise. This makes it perform well on the training set but poorly on new, unseen data. It's like memorizing answers instead of truly understanding a subject.  
- Regularization: It adds a penalty term to the model's loss function. This penalty discourages overly complex models, forcing them to generalize better to new data.  

Key takeaway:  Regularization techniques like L1 and L2 regularization help create models that are better at understanding the underlying patterns in data, not just the specific examples they were trained on.  
</div>
***


## Conclusion

By the end of this module, you'll have gained a solid grasp of linear regression as it's used in machine learning. You'll understand how linear regression models the relationships between variables to make predictions about continuous outcomes. You'll be able to identify when linear regression is the right tool for a given problem, prepare data for analysis, and evaluate the effectiveness of your model using metrics like MSE and R-squared.

But, you'll also be aware of linear regression's limitations and know when to consider alternative approaches.  With this knowledge, you're well-prepared to leverage linear regression in real-world scenarios, from biomedical research to epidemiological modeling, or any context where you need to make predictions from data. This foundational understanding opens the door to further exploration of the vast and ever-evolving landscape of data analysis and machine learning.

## Additional Resources

## Feedback

@feedback