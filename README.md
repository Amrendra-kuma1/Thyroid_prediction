Thyroid disease is a very common problem in India, more than one crore people are suffering with the disease every year.
Thyroid disorder can speed up or slow down the metabolism of the body.

The main objective of this project is to predict if a person is having compensated hypothyroid, primary hypothyroid, secondary hypothyroid or negative (no thyroid) with the help of Machine Learning. 
Classification algorithms such as Random Forest, Logistic Regression and KNN Model have been trained on the thyroid dataset, 
UCI Machine Learning repository. After hyperparameter tuning on KNN model has performed well with better accuracy. 
Application has deployed on Azure Cloud with the help of flask framework.

For Deployment link Prediction
Azure: https://thyroidprediction.azurewebsites.net

Demo:
youtube_link: https://youtu.be/50kbXefhd98


Technical Aspects
Python 3.10 and more
Important Libraries: sklearn, pandas, numpy, matplotlib & seaborn
Front-end: HTML, CSS
Back-end: Flask framework
IDE: Jupyter Notebook, Pycharm & VSCode
Deployment: Azure Cloud

How to run this app
Code is written in Python 3.10 and more. If you don't have python installed on your system, 
click here https://www.python.org/downloads/ to install.

Create virtual environment - conda create -n myenv python=3.10
Activate the environment - conda activate myenv
Install the packages - pip install -r requirements.txt
Run the app - python run app.py

Workflow
Thyroid Disease Data Set from UCI Machine Learning Repository.

Link:https://archive.ics.uci.edu/ml/datasets/thyroid+disease


Data Pre-processing
Missing values handling by Simple imputation (KNN Imputer)
Outliers detection and removal by boxplot and percentile methods
Categorical features handling by ordinal encoding and label encoding
Feature scaling done by Standard Scalar method
Imbalanced dataset handled by SMOTE
Drop unnecessary columns


Model Creation and Evaluation
Various classification algorithms like Random Forest, Logistic Regression, KNN etc tested.
Random Forest, Logistic Regression and KNN were all performed well.
Hyper parameter tuning was performed using RandomizedSearchCV
Model performance evaluated based on accuracy, confusion matrix, classification report.


Model Deployment
The final model is deployed on Azure using Flask framework.

Batch File Prediction User Interface
Homepage: A very simple UI with single page

![WhatsApp Image 2024-02-12 at 13 29 01_70844053](https://github.com/Amrendra-kuma1/Thyroid_prediction/assets/97242459/7df374b4-c2c1-4ac6-8a1f-55ba0a178819)

Author: Amrendra Kumar








