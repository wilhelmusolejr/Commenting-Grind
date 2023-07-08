import random

from datetime import date


import pandas as pd
import openpyxl

# initialize
today = date.today()

# read excel
df = pd.read_excel("grind.xlsx", index_col=None)

# print(df)
profileName = "Tis"
todayDate = "July 08, 2023"

comments = df.loc[df.index[(df['Facebook Name'] == profileName) & (df['Date'] == todayDate)]]["Comments"].values[0]
print(comments)

exit()

# CREATE BLANK
# todayDate = today.strftime("%B %d, %Y")
todayDate = "July 13, 2023"
lastDate = df.iloc[df.shape[0] - 1]['Date']

print(lastDate)
print(todayDate)
print(todayDate == lastDate)

if lastDate != todayDate:
  df.loc[len(df)] = [" ", " ", " "]
  print("Create blank")
  
profileName = "Raddd"
comments = int(random.randint(1, 100))
# todayDate = today.strftime("%B %d, %Y")
# Check if profile exists
# profileExist = df[(df['Facebook Name'] == profileName)].size
profileExist = df[(df['Facebook Name'] == profileName) & (df['Date'] == todayDate)].size
if not profileExist:
  # add new profile
  df.loc[len(df)] = [profileName, todayDate, comments]
  

# df.to_excel('grind.xlsx', index=False)
print(df)

exit()

# update comments
df.at[df.index[df['Facebook Name'] == "Wilhelmus Ole"][0],'Comments'] = int(random.randint(1, 100))

profileName = "Sambo"
comments = int(random.randint(1, 100))
todayDate = today.strftime("%B %d, %Y")
# Check if profile exists
# profileExist = df[(df['Facebook Name'] == profileName)].size
profileExist = df[(df['Facebook Name'] == profileName) & (df['Date'] == todayDate)].size
if not profileExist:
  # add new profile
  df.loc[len(df)] = [profileName, todayDate, comments]

# save excel
df.to_excel('grind.xlsx', index=False)
# print(df)








# add new row
# df.loc[len(df)] = ['Amy', "July 09 2023", 93] 

# update comments
# df.at[0,'Comments'] = int(random.randint(1, 100))