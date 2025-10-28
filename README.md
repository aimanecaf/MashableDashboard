# 📰 Online News Popularity Analysis for Mashable Articles
## 📘 Project Description

Predicting the popularity of online information has significant practical value across various domains. For instance, by leveraging popularity prediction, news organizations can better understand different patterns of online news consumption among users. This enables them to proactively deliver more relevant and engaging content, while also optimizing resource allocation throughout a story’s lifecycle.

This project is part of an analytical study conducted on behalf of Mashable, aiming to analyze and predict the popularity of their online news articles.

Here's the link of the project : [View the Plotly App](https://93c51250-f60f-4c63-95e4-5b5569b7a1f5.plotly.app/)

<p align="center">
  <img src="./assets/Mashable Dashboard.png" alt="Mashable Dashboard" width="500"/>
</p>
## Project Goal & Process

Our objective was to collaboratively build and evaluate predictive models for online news popularity.
There was no strict division of tasks — all stages of the project were carried out jointly by the team.

## 📊 Data Description

**Source**: Fernandes, Vinagre, and Cortez (2015)

**Dataset**: Mashable news articles published between 2013 and 2015

**Total Articles**: 39,644

**Features**: 60 input variables

**Target Variable**: Number of shares per article

For analytical purposes:

New variables were derived.

The target variable was categorized into two classes:

Popular (above the median number of shares)

Unpopular (below the median number of shares)

**Dataset Reference**:
Fernandes, K., Vinagre, P., & Cortez, P. (2015). A Proactive Intelligent Decision Support System for Predicting the Popularity of Online News. Proceedings of the 17th Portuguese Conference on Artificial Intelligence (EPIA 2015).

## 🎯 Objective

To provide Mashable with a predictive model capable of estimating the popularity of news articles before publication, based on their intrinsic features.

## 🧠 Techniques & Methodology

This study focused on predicting article popularity using both parametric and machine learning approaches.
To address dimensionality and multicollinearity issues, several techniques were employed.

### Statistical Models

Regularized Logistic Regression (Elastic Net)

GETS (General-to-Specific Modeling)

Principal Component Analysis (PCA)

Machine Learning Models

CART (Classification and Regression Trees)

Bagging

Random Forest

K-Nearest Neighbors (KNN)

Support Vector Machine (SVM)

Neural Networks

### Model Evaluation

All models were trained and tested on separate data subsets.
Performance was assessed primarily based on the overall accuracy rate, and the best-performing model was selected accordingly.

## ⚙️ Tools & Libraries

Python 3.x
Pandas, NumPy
Scikit-learn, statmodels
Matplotlib, Seaborn, plotly

