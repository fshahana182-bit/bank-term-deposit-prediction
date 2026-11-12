# Bank Term Deposit Subscription Prediction

## Project Overview

This project uses Machine Learning to predict whether a customer is likely to subscribe to a bank term deposit.

The project focuses on **pre-call prediction**, aiming to identify potential customers before a marketing call is made. It uses customer information and previous campaign-related features to support more effective marketing strategies.

Features that are only available after a marketing call, such as call duration, are excluded from the prediction model to avoid data leakage.

## Project Objectives

- Predict customer subscription likelihood before a marketing call.
- Understand customer data through Exploratory Data Analysis (EDA).
- Perform data preprocessing and handle missing values.
- Handle class imbalance using SMOTENC.
- Train and compare different Machine Learning algorithms.
- Improve model performance using hyperparameter tuning.
- Develop an interactive prediction application using Streamlit.

## Technologies & Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn
- XGBoost
- Streamlit

## Machine Learning Algorithms

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost

## Project Workflow

1. Data loading and understanding
2. Data cleaning and preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature selection
5. Handling class imbalance using SMOTENC
6. Model training and comparison
7. Hyperparameter tuning using GridSearchCV
8. Model evaluation
9. Streamlit application development

## Application

An interactive Streamlit application that accepts customer details and displays the predicted probability of subscribing to a bank term deposit.

The application is designed to support pre-call customer targeting.

## How to Run the Project

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## Project Files

- `Bank_term_deposit_subscription_prediction.ipynb` – Machine Learning workflow and analysis.
- `app.py` – Streamlit application.
- `requirements.txt` – Required Python libraries.
- `bank_term_deposit_model.pkl` – Saved trained model (if included).

## Learning Outcomes

This project provided practical experience in:

- Data preprocessing and exploratory data analysis.
- Handling imbalanced datasets using SMOTENC.
- Machine Learning model development and comparison.
- Hyperparameter tuning and model evaluation.
- Building an interactive application using Streamlit.
- Understanding pre-call prediction and avoiding data leakage.