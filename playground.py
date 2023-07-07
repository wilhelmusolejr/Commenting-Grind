import os
import random

def typeOfMessage():
  typesFeeling = ["joy", "fun", "engaging", "supportive", "appreciation", "excitement", "wholesome"]
  randominium = random.randint(0, len(typesFeeling) -1)
  return typesFeeling[randominium]

def cli(status):
  # os.system('cls')
  # print("*************************************")
  # print("Account " + str(profCounter) + " out of " + str(len(profile)))
  # print("*************************************")
  # print("Profile name       : " + prof.fullName)
  # print("Current status     : " + str(threadCounter) + " out of " + str(len(facebook)))
  # print("Current activity   : " + status)
  print("*************************************")

class Facebook:
  def __init__(self, link, postType):
    self.link = "https://m.facebook.com/groups/phdream/"+link
    self.postType = postType
    self.threadMessage = ""
    self.messageFeeling = typeOfMessage()
    
class Profile:
  def __init__(self, fullName, browserNumber):
    self.fullName = fullName
    self.browserNumber = browserNumber
    self.grindComment = 0
    
    
facebook = []
facebook.append(Facebook("posts/759704576156040/?comment_id=759705089489322","comment"))

profile = []
profile.append(Profile("Jerome Calawing", 35))

profCounter = 1
# for prof in profile:
#   print(profCounter)
#   profCounter += 1
