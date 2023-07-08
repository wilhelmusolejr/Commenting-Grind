# import pandas as pd

# fbThreadFileName = "facebook_thread.xlsx"
# fbThreadDF = pd.read_excel(fbThreadFileName, index_col=None)

# rowSize = int(fbThreadDF.shape[0])

# # print(fbThreadDF)

# facebook = []
# for i in range(rowSize):
#   # facebook.append()
#   fbLink = fbThreadDF.loc[fbThreadDF.index[i]]["Facebook Link"]
#   threadType = fbThreadDF.loc[fbThreadDF.index[i]]["Thread Type"]
#   print(fbLink)
#   print(threadType)
  
  
link="https://www.facebook.com/groups/phdream/posts/762186735907824/?comment_id=762235739236257"
print ()

print()

print(link[int(link.find("posts")):len(link)])