# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:19:01 2019

@author: Umer khalifa
"""

game_app = pd.read_csv("appstore_games.csv")

# Basic checks and cleaning
game_app.columns = game_app.columns.str.replace(" ", "_")

for i in game_app.head():
    print(i)

game_app.describe()

game_app.info()

game_app.isnull().sum()

game_app.dropna(how = "any", inplace = True)

game_app[["Subtitle", "Average_User_Rating", "User_Rating_Count", "Price", "In-app_Purchases", "Languages", "Size"]].fillna(0, inplace = True)

# Separating year:
game_app[["day", "month", "year"]] = game_app["Original_Release_Date"].str.split("/", n=3 , expand = True)

# Data analysis:
# Growth of game production over years:
plt.figure(figsize = (12,8))
yr_pro = game_app.groupby("year")["Name"].count().plot(kind = "line")
plt.grid(b=None)

# Changes in price of games over years:
plt.figure(figsize = (12,8))
game_app.groupby("year")["Price"].sum().plot(kind = "line")
plt.grid(b=None)

# Changes in size of games over years:
plt.figure(figsize = (12,8))
game_app.groupby("year")["Size"].sum().plot(kind = "line")
plt.grid(b=None)

# Top 6 games with maximum count of ratings:
plt.figure(figsize = (12,8))
top_gam = game_app.groupby(["Name", "year"])["User_Rating_Count"].mean().sort_values(ascending = False).head(6).plot(kind = "Bar", color = ["r", "y", "g", "b", "m"], edgecolor = "B", Alpha = 0.5)
plt.xticks(rotation = 45)
plt.grid(b=None)

# Top age groups with maximum use of games 
age_group = game_app.groupby("Age_Rating")["Name"].count().sort_values(ascending = False)
plt.figure(figsize = (12,8))
age_group.plot(kind = "Bar", color = ["r", "y", "g"], edgecolor = "B", Alpha = 0.5)

# Top rated games age wise:
plt.figure(figsize = (12,8))
top_gam_4 = game_app.query("Age_Rating == '4+'").groupby(["Age_Rating","Name", "year"])["User_Rating_Count"].mean().sort_values(ascending = False).head(6).plot(kind = "Bar", color = ["r", "y", "g", "m"], edgecolor = "B", Alpha = 0.5)
plt.xticks(rotation = 45)
plt.grid(b=None)

plt.figure(figsize = (12,8))
top_gam_9 = game_app.query("Age_Rating == '9+'").groupby(["Age_Rating","Name", "year"])["User_Rating_Count"].mean().sort_values(ascending = False).head(6).plot(kind = "Bar", color = ["r", "y", "g", "b", "m"], edgecolor = "B", Alpha = 0.5)
plt.grid(b=None)

plt.figure(figsize = (12,8))
top_gam_12 = game_app.query("Age_Rating == '12+'").groupby(["Age_Rating","Name", "year"])["User_Rating_Count"].mean().sort_values(ascending = False).head(6).plot(kind = "Bar", color = ["r", "y", "g", "b", "m"], edgecolor = "B", Alpha = 0.5)
plt.grid(b=None)

plt.figure(figsize = (12,8))
top_gam_17 = game_app.query("Age_Rating == '17+'").groupby(["Age_Rating","Name", "year"])["User_Rating_Count"].mean().sort_values(ascending = False).head(6).plot(kind = "Bar", color = ["r", "y", "g", "b", "m"], edgecolor = "B", Alpha = 0.5)
plt.grid(b=None)

#Average user ratings for top 6 games:
user_rating = game_app.query("Name == ['Clash of Clans', 'Clash Royale', 'PUBG MOBILE', 'Plants vs. Zombies\u2122 2', 'Pok\xe9mon GO']").groupby("Name")["Average_User_Rating"].mean()

plt.figure(figsize = (12,8))
user_rating.plot(kind = "Bar", color = ["r", "y", "g"], edgecolor = "B", Alpha = 0.5)

# Top rated games and its information
gam = game_app.query("Name == ['Clash of Clans', 'Clash Royale', 'PUBG MOBILE', 'Plants vs. Zombies\u2122 2', 'Pok\xe9mon GO']").groupby(["Name", "Developer", "Age_Rating", "Size", "Genres", "Primary_Genre"])["User_Rating_Count"].mean().sort_values(ascending = False)

plt.figure(figsize = (12,8))
gam.plot(kind = "Bar", color = ["r", "y", "g"], edgecolor = "B", Alpha = 0.5)

# Languages:
game_lang = game_app.groupby(["Subtitle", "Languages"])["User Rating Count"].mean().sort_values(ascending = False).head(6)

# Update frequency of top games
game_app['Original Release Date'] = pd.to_datetime(game_app['Original Release Date'], format = '%d/%m/%Y')

game_app['Current Version Release Date'] = pd.to_datetime(game_app['Current Version Release Date'], format = '%d/%m/%Y')

game_app['update frequency'] = game_app['Current Version Release Date'] - game_app['Original Release Date']

up_frequency = game_app.groupby(["Subtitle", "update frequency"])["update frequency"].count().sort_values(ascending = False).head(5)

# State of market:
game_app.groupby(["Primary Genre", "Genres"])["User Rating Count"].mean().sort_values(ascending = False).head(5)

game_app["Genres"].str.split(",", n = 4, expand =True)

game_app['Genres'] = game_app['Genres'].str.replace(',', '').str.replace('Games', '').str.replace('Entertainment', '').str.replace('Strategy', '')

game_app["Languages"].count()


# Image download from URL:
icon = game_app["Icon URL"]

for i in game_app["Icon URL"]:
    resp = requests.get(i, stream = True)
    local_file = open('local_image.jpg', 'wb')
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, local_file)
    del resp
 
resp = requests.get(icon, stream = True)
local_file = open('local_image.jpg', 'wb')
resp.raw.decode_content = True
shutil.copyfileobj(resp.raw, local_file)
del resp     

for img in icon:
  file_name = img.split('/')[-1]
  print("Downloading file:%s"%file_name)
  r = requests.get(img, stream = True)
  with open("file_name", 'wb') as f:
    for chunk in r:
      f.write(chunk)


# Prediction:
