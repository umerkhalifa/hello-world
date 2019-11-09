# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:41:09 2019

@author: Umer khalifa
"""

import pandas as pd 
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as num 
%matplotlib inline
import statsmodels.api as sm
from statsmodels.formula.api import ols
import scipy.stats as stat

# Amazon forest fire data analysis 
# Importing data
amazon_fire = pd.read_excel("Amazon.xlsx")

# Checking the column names and dimension of the data
amazon_fire.head()
amazon_fire.shape
amazon_fire['state'].unique()

# Basic arthimetics 
amazon_fire.describe()

# Grouping data
# Mean fire per year 
am_yr = amazon_fire.groupby("year")["number"].mean().sort_values()

plt.figure(figsize = (12,8))
sns.barplot(x = amazon_fire["year"], y = amazon_fire["number"], estimator = np.mean)
plt.title("Average fire incident per year")

# Mean fire per state
am_ste = amazon_fire.groupby("state")["number"].mean().sort_values(ascending = False)

plt.figure(figsize = (12,8))
sns.lineplot(x = amazon_fire['state'], y = amazon_fire['number'], estimator = 'mean')
plt.xticks(rotation = 50) 
plt.title("Average fire incident per state")

# mean forest fire per decade 
am_dec1 = amazon_fire.query("year == year < 2008")["number"].mean()

am_dec1plot = amazon_fire.query("year == year < 2008").groupby("year")["number"].mean().plot(kind = "Bar", Color = "Red")
plt.xlabel("Year")
plt.ylabel("Average fires per year")
plt.title("Forest fire between 1998 -2007")

am_dec2 = amazon_fire.query("year == year > 2007")["number"].mean()

am_dec2plot = amazon_fire.query("year == year > 2007").groupby("year")["number"].mean().plot(kind = "Bar", Color = "Yellow")
plt.xlabel("Year")
plt.ylabel("Average fires per year")
plt.title("Forest fire between 2008 -2017")


# Significant difference between decades 
# One way ANOVA

f, pvalue = stat.f_oneway(am_dec1, am_dec2)

# Data Homogeneity 
w, levene = stat.levene(am_dec1, am_dec2)

plt.figure(figsize = (12,8))
sns.lineplot(x = "year", y = "number", hue = "state", data = amazon_fire)

# Top 6 states of forest fire per decade 
top = amazon_fire.groupby("state")["number"].mean().sort_values(ascending = False)
# Grouping on the basis of year and state
am_ys1 = amazon_fire.query("year == year < 2008 and state == ['Sao Paulo', 'Mato Grosso', 'Bahia', 'Piau', 'Goias']").groupby(["state"])["number"].mean()

am_ys1.plot(kind = "Bar", Color = "Red")

am_ys2 = amazon_fire.query("year == year > 2007 and state == ['Sao Paulo', 'Mato Grosso', 'Bahia', 'Piau', 'Goias']").groupby(["state"])["number"].mean()
am_ys2.plot(kind = "Bar", Color = "Red")

# Significant difference between decades 
# One way ANOVA

f, pvalue = stat.f_oneway(am_ys1, am_ys2)

# Data Homogeneity 
w, levene = stat.levene(am_ys1, am_ys2)

# Averageforest fire per month 
am_ysm = amazon_fire.groupby("month")["number"].mean().sort_values(ascending = False)

# Average forest fire per month in each top states
am_ysm1 = amazon_fire.query("year == year < 2008 and state == ['Sao Paulo', 'Mato Grosso', 'Bahia', 'Piau', 'Goias'] and month == ['Julho', 'Outubor', 'Agosto', 'Novembro', 'Dezembro']").groupby(["year", "state", "month"])["number"].mean()
am_ysm2 = amazon_fire.query("year == year > 2007 and state == ['Sao Paulo', 'Mato Grosso', 'Bahia', 'Piau', 'Goias'] and month == ['Julho', 'Outubor', 'Agosto', 'Novembro', 'Dezembro']").groupby(["year", "state", "month"])["number"].mean()