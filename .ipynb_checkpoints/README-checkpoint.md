# Airline Satisfaction Analysis

## Problem Statement
- Provide a brief background or context for your analysis. Explain why the data is relevant or interesting.

- Clearly state the purpose of your analysis. What are you aiming to achieve or communicate through this analysis? Who would this benefit?

## Data Dictionary
Include a data dictionary to explain the meaning of each variable or field in the dataset. You can also link to an external data dictionary.

| Column Name | Description |
|------------|------------|
| Gender | Gender of the passenger (Female, Male) |
| Customer Type | Type of customer (Loyal customer, Disloyal customer) |
| Age | Age of the passenger |
| Type of Travel | Purpose of the flight (Personal Travel, Business Travel) |
| Class | Travel class of the passenger (Business, Eco, Eco Plus) |
| Flight Distance | Distance of the flight journey |
| Inflight WiFi Service | Satisfaction level of inflight WiFi service (0 = Not Applicable, 1–5 scale) |
| Departure/Arrival Time Convenient | Satisfaction level with departure and arrival time convenience |
| Ease of Online Booking | Satisfaction level with the online booking process |
| Gate Location | Satisfaction level with the gate location |
| Food and Drink | Satisfaction level with food and beverage service |
| Online Boarding | Satisfaction level with the online boarding process |
| Seat Comfort | Satisfaction level with seat comfort |
| Inflight Entertainment | Satisfaction level with inflight entertainment |
| On-board Service | Satisfaction level with on-board service |
| Leg Room Service | Satisfaction level with leg room service |
| Baggage Handling | Satisfaction level with baggage handling |
| Check-in Service | Satisfaction level with the check-in service |
| Inflight Service | Satisfaction level with inflight service |
| Cleanliness | Satisfaction level with aircraft cleanliness |
| Departure Delay in Minutes | Number of minutes the departure was delayed |
| Arrival Delay in Minutes | Number of minutes the arrival was delayed |
| Satisfaction | Overall airline satisfaction level (Satisfied, Neutral, or Dissatisfied) |


## Executive Summary

### Data Cleaning Steps
To clean the data, I first checked for missing values and looked at the distribution of the columns that have NaN values. Only one column had missing values, and it was a very right skewed distribution. After determining that there outliers were valid, I used the median to impute the missing values. Prior to that though, I created a new column that provided a missingness flag, so that the machine learning models would know that these values were originally missing and imputed. 

I also created new columns to create groups for departure/arrival delays as well as age groups for further analysis. 

### Key Visualizations

#### Visualization 1: [Departure Delay Group by Satisfaction]
This countplot shows that as the delays get bigger, customer satisfaction decreases.

We see that all the groups, even flights that are on time, the dissatisfaction is greater than the satisfaction. This tells us that when there is no delay, there is minimal affect on satisfaction. However, as the delay gets greater and greater, the difference between satisfied customers and dissatisfied customers grows. 

We see this in `very large delay`, where the number of dissatisfied customers nearly doubles that of satisfied customers. 

![Visualization 1](./images/depart_sat.png)

#### Visualization 2: [Age Group by Satisfaction]
The below pie charts show how different age groups rate their overall flight experience. We see that adults (bottom left) have the highest proportion of satisfied passengers, but still have more dissatisfaction than satisfaction. 

A potential cause of this could be empathy. It may be that adults are more likely to empathize with the difficulties faced and therefore are not as easily upset compared to children and seniors, or may be more likely to express their dissatisfaction.

![Visualization 2](./images/age_group_pie.png)

For more visualizations, please see [EDA Notebook](./EDA.ipynb)

## Conclusions/Recommendations
I trained multiple models to generate predictions of satisfaction or dissatisfaction. Specifcally, I trained a Logistic Regression model, a Random Forest model, and a K Nearest Neighbors (KNN) model. 

The results are below. 

| Model | Accuracy Score |
| ----- | -------------- |
| Logistic Regression | 87.54% |
| Random Forest | 96.06% |
| KNN | 92.79% |

The Random Forest model was the most accurate out of the 3 models. 

### Confusion Matrix

![confusion matrix](./images/rf_conf.png)

We can see that the random forest model also has a very good confusion matrix, getting less than 1000 wrong predictions in either satisfied or dissatsified classfiications across the entire dataset. 

### ROC Curve

![roc auc curve](./images/rf_roc.png)

This ROC curve shows that the model separates the classes very well, as indicated by the steep rise near the y-axis. This means the model achieves a high true positive rate while maintaining a low false positive rate across a range of thresholds

### Main Insights

Based on the exploratory data analysis, passenger satisfaction rarely appears to stem from a single service area; instead, it is often the result of shortcomings across multiple areas. The data show that even when passengers rated a particular service area highly (5/5), many still reported overall dissatisfaction. This suggests that strong performance in a few areas is not sufficient to ensure satisfaction if other aspects of the experience fall short.

Consequently, airlines should aim to improve the passenger experience holistically. Weakness in any single service area can negatively impact overall satisfaction, even when other areas perform well.

## Additional Information
Include any additional information, references, or resources that might be relevant for understanding the analysis.
