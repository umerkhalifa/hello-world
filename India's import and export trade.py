# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 12:03:10 2019

@author: Umer khalifa
"""
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import statsmodels.formula.api as ols
import statsmodels.api as sm
import seaborn as sns
import scipy.stats as stat

export  = pd.read_csv("2018-2010_export.csv")

# Export data analysis 
# Indias most exported commodities 
# between 2010 - 2014
ex_com = export.groupby("Commodity")["value"].mean().sort_values(ascending = False)
plt.figure(figsize = (12,8))
ex_com.head(5).plot(kind = "Bar", Color = "Red")

ex_co = export.groupby("Commodity").agg({"value":"mean"})
sns.barplot(x = ex_co.index, y = ex_co.value)

# Trade between top 5 countries 
ex_con = export.groupby("country")["value"].mean().sort_values(ascending = False)
plt.figure(figsize = (12,8))
ex_con.head(5).plot(kind = "Bar", Color = "Red")


# growth of trade of each top countries over years
USA = export.query("country == 'U S A'").groupby("year")["value"].mean().plot(kind = "Bar")
UAE = export.query("country == 'U ARAB EMTS'").groupby("year")["value"].mean().plot(kind = "Bar")
H_KONG = export.query("country == 'HONG KONG'").groupby("year")["value"].mean().plot(kind = "Bar")
CHINA = export.query("country == 'CHINA P RP'").groupby("year")["value"].mean().plot(kind = "Bar")
SINGAPORE = export.query("country == 'SINGAPORE'").groupby("year")["value"].mean().plot(kind = "Bar")

# Top country wise export
EX_USA = export.query("country == 'U S A'").groupby("Commodity")["value"].mean().sort_values(ascending = False)
EX_USA.head(5).plot(kind = "bar")

EX_UAE = export.query("country == 'U ARAB EMTS'").groupby("Commodity")["value"].mean().sort_values(ascending = False)
EX_UAE .head(5).plot(kind = "bar")

EX_H_KONG = export.query("country == 'HONG KONG'").groupby("Commodity")["value"].mean().sort_values(ascending = False)
EX_H_KONG.head(5).plot(kind = "bar")

EX_CHINA = export.query("country == 'CHINA P RP'").groupby("Commodity")["value"].mean().sort_values(ascending = False)
EX_CHINA.head(5).plot(kind = "bar")

EX_SINGAPORE = export.query("country == 'SINGAPORE'").groupby("Commodity")["value"].mean().sort_values(ascending = False)
EX_SINGAPORE.head(5).plot(kind = "bar")




# IMPORT DATA ANALYSIS 
Import  = pd.read_csv("2018-2010_import.csv")

Import.head()
for i in export.head():
    print(i)
Import.shape

# Indias most imported commodities 
im_com = Import.groupby("Commodity")["value"].mean().sort_values(ascending = False)
plt.figure(figsize = (12,8))
im_com.head(5).plot(kind = "Bar", Color = "Red")
    
# Import trade between top 5 countries 
im_con = Import.groupby("country")["value"].mean().sort_values(ascending = False)
plt.figure(figsize = (12,8))
im_con.head(5).plot(kind = "Bar", Color = "Red")

# Growth of import from each top countries over years
Iraq = Import.query("country == 'IRAQ'").groupby("year")["value"].mean().plot(kind = "Bar")
China = Import.query("country == 'CHINA P RP'").groupby("year")["value"].mean().plot(kind = "Bar")
Saudi = Import.query("country == 'SAUDI ARAB'").groupby("year")["value"].mean().plot(kind = "Bar")
Venezuela = Import.query("country == 'VENEZUELA'").groupby("year")["value"].mean().plot(kind = "Bar")
Angola = Import.query("country == 'ANGOLA'").groupby("year")["value"].mean().plot(kind = "Bar")
Usa = Import.query("country == 'U S A'").groupby("year")["value"].mean().plot(kind = "Bar")

# Top country wise import
IM_Iraq =Import.query("country == 'U S A'").groupby("Commodity")["value"].mean().sort_values(ascending = False)
plt.figure(figsize = (12,8))
IM_Iraq.head(5).plot(kind = "bar")

IM_China = Import.query("country == 'CHINA P RP'").groupby("Commodity")["value"].mean().sort_values(ascending = False)
plt.figure(figsize = (12,8))
IM_China .head(5).plot(kind = "bar")

IM_H_Saudi = Import.query("country == 'SAUDI ARAB'").groupby("Commodity")["value"].mean().sort_values(ascending = False)
plt.figure(figsize = (12,8))
IM_H_Saudi.head(5).plot(kind = "bar")

IM_Venezuela = Import.query("country == 'VENEZUELA'").groupby("Commodity")["value"].mean().sort_values(ascending = False)
plt.figure(figsize = (12,8))
IM_Venezuela.head(5).plot(kind = "bar")

IM_Angola = Import.query("country == 'ANGOLA'").groupby("Commodity")["value"].mean().sort_values(ascending = False)
plt.figure(figsize = (12,8))
IM_Angola.head(5).plot(kind = "bar")

IM_Usa = Import.query("country == 'U S A'").groupby("Commodity")["value"].mean().sort_values(ascending = False)
IM_Usa.head(5).plot(kind = "bar")

# TRADE DEFICIT

ex = export["value"].mean()

im = Import["value"].mean()

deficit = ex - im

