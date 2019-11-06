# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:27:49 2019

@author: Umer khalifa
"""

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
%matplotlib inline
from statsmodels.formula.api import ols
import statsmodels.api as sm
import scipy.stats as stat
import wordcloud import WordCloud
from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import r2_score

# Importing data 
airbnb = pd.read_csv("AB_NYC_2019.csv")
NYC_im = Image.open("New_York_City_.PNG")

# Headings and dimension 
airbnb.head()
for i in airbnb.head():
    print(i)
rows, columns = airbnb.shape

(f"Airbnb consists {rows} rows and {columns} columns")

# checking for missing vlaues or null 
airbnb.isnull().sum()

airbnb.dropna(how = "any", inplace = True)

airbnb.info()

# replacing null values with 0
airbnb["last_review"].fillna(0, inplace = True)
airbnb["reviews_per_month"].fillna(0, inplace = True)

# Room type and neighbourhood counts 

plt.figure(figsize = (12,8))
sns.countplot(airbnb["neighbourhood_group"])

plt.figure(figsize = (12,8))
sns.countplot(airbnb["room_type"])

# Number of different rooms in a neighbourhood 
neig_count = airbnb.groupby("neighbourhood")["neighbourhood"].count().sort_values(ascending = False)
neighbour = neig_count.head(13)

plt.figure(figsize = (12,8))
sns.scatterplot(airbnb["latitude"], airbnb["longitude"], hue = "neighbourhood_group", data = airbnb, alpha = "auto")

sns.scatterplot(airbnb["latitude"], airbnb["longitude"], hue = "neighbourhood_group", data = airbnb, alpha = "auto")

plt.figure(figsize = (12,8))
sns.scatterplot(airbnb["latitude"], airbnb["longitude"], hue = "room_type", data = airbnb, alpha = "auto")

# Filtering and grouping data 

rom_neig = airbnb.groupby(["room_type", "neighbourhood_group"])["price"]. mean()

bnb_pvt = airbnb.query("room_type == 'Private room'").groupby("neighbourhood_group")["price"].mean()

bnb_apt = airbnb.query("room_type == 'Entire home/apt'").groupby("neighbourhood_group")["price"].mean()

bnb_shr = airbnb.query("room_type == 'Shared room'").groupby("neighbourhood_group")["price"].mean()

anova =  stat.f_oneway(bnb_pvt, bnb_apt, bnb_shr)



plt.figure(figsize = (12,8))
plt.xticks(rotation = 45)
sns.barplot(x = airbnb["neighbourhood_group"], y = airbnb["price"], estimator = np.mean, saturation=.75)

# Customer review 

airbnb["number_of_reviews"].sum()
airbnb["reviews_per_month"].sum()
airbnb["calculated_host_listings_count"].sum()

# Reviews and listings in each state
no_rev = airbnb.groupby(["neighbourhood_group", "neighbourhood"])["number_of_reviews"].sum().sort_values(ascending = False).head(5)

no_lst = airbnb.groupby(["neighbourhood_group", "neighbourhood"])["calculated_host_listings_count"].sum().sort_values(ascending = False).head(5)

rev_per_mon = airbnb.groupby(["neighbourhood_group", "neighbourhood"])["reviews_per_month"].sum().sort_values(ascending = False).head(5)

# Reviews and listings in each state
no_of_rev_host = airbnb.query("neighbourhood_group == ['Brooklyn', 'Manhattan', 'Queens', 'Bronx', 'Staten Island']").groupby(["neighbourhood_group", "neighbourhood", "host_name",])["number_of_reviews"].sum().sort_values(ascending = False).head(5)

no_of_rev_host_mnth = airbnb.query("neighbourhood_group == ['Brooklyn', 'Manhattan', 'Queens', 'Bronx', 'Staten Island']").groupby(["neighbourhood_group", "neighbourhood", "host_name",])["reviews_per_month"].sum().sort_values(ascending = False).head(5)

no_of_host_lst = airbnb.query("neighbourhood_group == ['Brooklyn', 'Manhattan', 'Queens', 'Bronx', 'Staten Island']").groupby(["neighbourhood_group", "neighbourhood", "host_name",])["calculated_host_listings_count"].sum().sort_values(ascending = False).head(5)


# Prediction
# encoding coverting cateogoriacal varaible into numercial variable 
def Encode(airbnb):
    for column in airbnb.columns[airbnb.columns.isin(['neighbourhood_group', 'room_type'])]:
        airbnb[column] = airbnb[column].factorize()[0]
    return airbnb

airbnb_en = Encode(airbnb.copy())


plt.figure(figsize=(12,8))
sns.heatmap(airbnb_en.corr())

# Preparaing independent and dependent variable 
for i in airbnb_en.head():
    print(i)
x = np.array(pd.get_dummies(airbnb_en.iloc[:,[4,8,10,11,14]]))
y = np.array(airbnb_en["price"])

# Generating test and train data from variables linearregression 
x_train,x_test,y_train,y_test = train_test_split(x,y)

lm_mod = LinearRegression()

lm_train = lm_mod.fit(x_train, y_train)

lm_train.score(x,y)

# Intercept and Coefficient of each independent variable 
coeff_df = pd.DataFrame(lm_train.coef_, x.columns, columns=['Coefficient'])
lm_train.intercept_
lm_train.coef_

y_predict = lm_mod.predict(x_test)

r2_score(y_test,y_predict)

# Creating a dataframe with actual and predicted prices 

d_frame = pd.DataFrame({"Actual":y_test, "Predicted":y_predict})
d_frame["Actual"].sum()
d_frame["Predicted"].sum()

# To validate the regression model three steps has to be done 
# Mean Absolute Error
# Mean Squared Error
# Root Mean Squared Error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

Mean_Absolute_Error = mean_absolute_error(y_test,y_predict)

Mean_Squared_Error =  mean_squared_error(y_test,y_predict)

Root_Mean_Squared_Error = np.sqrt(mean_squared_error(y_test,y_predict))

# Generating test and train data from variables Decsion tree regression 
d_tree = DecisionTreeRegressor(min_samples_leaf = 0.0001)

dtree_train = d_tree.fit(x_train, y_train)

dtree_train.score(x,y)

dtree_y_predict = d_tree.predict(x_test)

r2_score(y_test,dtree_y_predict)