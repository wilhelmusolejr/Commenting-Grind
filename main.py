# ACCOUNTS
# Michael Castro - soledad.pose = 11 
# Jericho Yang - geraldine grant = 25
# Moana Alonzo - wilzone143 = 37
# Jenny Apakabago - wirma.ole3535 = 40
# Christian Abador - k63 = 2
# kenny sofer = 24
# Rhiana Alonzo - layla lorenjin = 18
# Brendan Eich - jenny humbong = 22
# James Alarte - Toyoyoy = 16
# Jerome Calawing - Soledad Pakshet  = 35
# Sofia Andrade - Sofia Andrade = 48
# Olgie Alonzo - Silverio Dragoe = 30
# Robert Hapiz - Roberthapiz = 6

import openai

import time
from datetime import date

import random
import os

import pandas as pd

# selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#--------------------------
# CHAT GPT CONFIGURATION
openai.api_key = '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'
messages = [{"role": "system", "content": "You are a kind helpful assistant."}]

today = date.today()
todayDate = today.strftime("%B %d, %Y")
# PANDAS
df = pd.read_excel("grind.xlsx", index_col=None)

lastDate = df.iloc[df.shape[0] - 1]['Date']
if lastDate != todayDate:
  df.loc[len(df)] = [" ", " ", " "]
  # print("Create blank")


# TIME FOR RECORDING
start_time = time.time()

def typeOfMessage():
  typesFeeling = ["joy", "fun", "engaging", "supportive", "appreciation", "excitement", "wholesome"]
  randominium = random.randint(0, len(typesFeeling) -1)
  return typesFeeling[randominium]

def cli(status):
  os.system('cls')
  print("*************************************")
  print("Account " + str(profCounter) + " out of " + str(len(profile)))
  print("*************************************")
  print("Profile name       : " + prof.fullName)
  print("Current status     : " + str(threadCounter) + " out of " + str(len(facebook)))
  print("Current activity   : " + status)
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
    

#--------------------------
# INITIAL

facebook = []

# facebook.append(Facebook("posts/761674715959026/?comment_id=761711155955382","comment"))
# facebook.append(Facebook("posts/761674715959026?comment_id=761733662619798","comment"))

# https://www.facebook.com/photo/?fbid=118774357934830&set=gm.761674715959026&idorvanity=734094518717046
# facebook.append(Facebook("posts/761674715959026/?comment_id=761849135941584","comment"))
# facebook.append(Facebook("posts/761674715959026/?comment_id=761772802615884","comment"))
# facebook.append(Facebook("posts/761674715959026/?comment_id=761722289287602","comment"))
# facebook.append(Facebook("posts/761674715959026/?comment_id=761718542621310","comment"))

# Solid ng PHDREAM ONLINE CASINO
# https://www.facebook.com/groups/phdream/posts/761379739321857/
# facebook.append(Facebook("posts/761379739321857/?comment_id=761533702639794","comment"))
# facebook.append(Facebook("posts/761379739321857/?comment_id=761755272617637","comment"))
# facebook.append(Facebook("posts/761379739321857/?comment_id=761710415955456","comment"))
# facebook.append(Facebook("posts/761379739321857/?comment_id=761397529320078","comment"))
# facebook.append(Facebook("posts/761379739321857/?comment_id=761713135955184","comment"))

# facebook.append(Facebook("posts/760803052712859/?comment_id=760875826038915","comment"))
# facebook.append(Facebook("posts/760935576032940/?comment_id=760936562699508","comment"))
facebook.append(Facebook("posts/759704576156040/?comment_id=759705089489322","comment"))
# facebook.append(Facebook("posts/759704576156040?comment_id=759787379481093","comment"))
facebook.append(Facebook("posts/759704576156040?comment_id=759776516148846","comment"))
# facebook.append(Facebook("posts/756628039797027/?comment_id=756721556454342","comment"))
# facebook.append(Facebook("posts/756628039797027?comment_id=756683659791465","comment"))
# facebook.append(Facebook("posts/756628039797027?comment_id=756796763113488","comment"))
# facebook.append(Facebook("permalink/760006666125831/?comment_id=760014389458392","comment"))
# facebook.append(Facebook("permalink/760006666125831/?comment_id=760019062791258","comment"))
# facebook.append(Facebook("permalink/759741329485698/?comment_id=759775512815613","comment"))
# facebook.append(Facebook("permalink/759741329485698/?comment_id=759819346144563","comment"))
# facebook.append(Facebook("permalink/760929932700171/?comment_id=760933352699829","comment"))
# facebook.append(Facebook("permalink/760929932700171/?comment_id=760932679366563","comment"))
# facebook.append(Facebook("permalink/760803052712859/?comment_id=760883152704849","comment"))
# facebook.append(Facebook("permalink/760803052712859/?comment_id=760902112702953","comment"))
# facebook.append(Facebook("permalink/760803052712859/?comment_id=760885906037907","comment"))
# facebook.append(Facebook("permalink/759741329485698/?comment_id=759988892794275","comment"))
# facebook.append(Facebook("permalink/759741329485698/?comment_id=760730616053436","comment"))
# facebook.append(Facebook("permalink/759741329485698/?comment_id=759839196142578","comment"))

profile = []
# profile.append(Profile("Michael Castro", 11))
# profile.append(Profile("Jericho Yang", 25))
# profile.append(Profile("Moana Alonzo", 37)) ---- suspended
# profile.append(Profile("Jenny Apakabago", 40))
# profile.append(Profile("Christian Abador", 2))

# profile.append(Profile("Kenny Sofer", 24))
# profile.append(Profile("Rhiana Alonzo", 18)) ---- suspended
profile.append(Profile("Brendan Eich", 22))
# profile.append(Profile("James Alarte", 16))
# profile.append(Profile("Jerome Calawing", 35))
# profile.append(Profile("Sofia Andrade", 48))
# profile.append(Profile("Olgie Alonzo", 30))
profile.append(Profile("Robert Hapiz", 6))

profCounter = 1
for prof in profile:
  profileName = prof.fullName
  totalComments = 0
  
  # check if Profile Exist
  profileExist = df[(df['Facebook Name'] == profileName) & (df['Date'] == todayDate)].size
  
  if profileExist:
    # get latest total comments in excel
    totalComments = df.loc[df.index[(df['Facebook Name'] == profileName) & (df['Date'] == todayDate)]]["Comments"].values[0]
  else:
    # create profile to excel
    df.loc[len(df)] = [profileName, todayDate, totalComments]
    df.to_excel('grind.xlsx', index=False)
  
  testing = 0
  # WEBDRIVER CONFIGURATION
  if not testing:
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data')
    options.add_argument('--profile-directory=Profile '+ str(prof.browserNumber))
    options.add_argument('lang=en')
    options.add_argument('--disable-blink-features=AutomationControlled')
    prefs = {
                    "profile.default_content_setting_values.geolocation": 2,
                    "credentials_enable_service": False,
                    "profile.password_manager_enabled": False,
                    "webrtc.ip_handling_policy": "disable_non_proxied_udp",
                    "webrtc.multiple_routes_enabled": False,
                    "webrtc.nonproxied_udp_enabled" : False,
                    "detach": True
                }
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('log-level=3')
    options.add_argument("--start-maximized")
    options.set_headless(headless=False)
    options.add_argument('--user-agent="Mozilla/5.0 (Linux; Android 12; SM-N9750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36 EdgA/112.0.1722.46"')
    browser = webdriver.Chrome(executable_path='driver\chromedriver.exe', options= options)


  #---------------------------------------------------
  waiting_time = 20;
  
  # STARTER
  errorCounter = 0
  threadCounter = 0
  for thread in facebook:
    isThreadGood = False
    while isThreadGood is False:
      try:
        cli("Thread opened")

        # Go to page
        browser.get(thread.link)
        
        commentElement = 'textarea'
        commentButtonElement = "div[aria-label='SEND']"
        
        chatGptFeedback = False
        randomSentence = ""

        # Comment
        cli("Waiting for precense of comment element")
        WebDriverWait(browser, waiting_time).until(EC.presence_of_element_located((By.TAG_NAME, commentElement)))
        thread.threadMessage = browser.execute_script('return document.querySelector("div[data-type=transactional] div[data-mcomponent=MContainer]").children[0].children[1].textContent') 
        cli("Post --> " + str(thread.threadMessage))

        counter = 1
        while chatGptFeedback is not True:
          try:
            # print("Post: " + thread.threadMessage)
        
            timeAlloted = 60
            ai_start_time = time.time()
        
            # Generate Sentence

            cli("Waiting for AI response")

            message = "What to reply to a "+ thread.postType +" '"+ thread.threadMessage +"' where the reply should agree to the "+ thread.postType +" and the "+ thread.postType +" is not referring to me it refers to someone else. Add a little bit praise and appreciation to PHDream. Do not provide translation. Use taglish dialect. Use simple words and make the reply short, that will make the reply written like a real human. "
            messages.append({"role": "user", "content": message},)
            chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            randomSentence = chat.choices[0].message.content
            browser.execute_script(f'document.querySelector("textarea").value = "{randomSentence}"')

            cli("AI response received")
        
            chatGptFeedback = True
          except Exception as error:
            time.sleep(10)
            print("An exception occurred ", error)
      
        counter += 1
        
        # browser.find_element(By.TAG_NAME, commentElement).send_keys(Keys.CONTROL, 'v') # paste
        browser.find_element(By.TAG_NAME, commentElement).send_keys(" ")

        # Button
        WebDriverWait(browser, waiting_time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, commentButtonElement)))
        browser.find_element(By.CSS_SELECTOR, commentButtonElement).click()
        
        cli("Response commented to the thread")
        
        time.sleep(10)
        
        ai_end_time = time.time()
        
        timeTaken = int(ai_end_time - ai_start_time)
        
        forSleep = timeAlloted - timeTaken  
        
        threadCounter += 1
        totalComments += 1
        
        if forSleep > 0:
          for i in range(forSleep):
            cli("Sleeping for " + str(forSleep - (i + 1)) + " seconds")
            time.sleep(1)
          # cli("Sleeping for " + str(forSleep) + " seconds")
          # time.sleep(forSleep)
        
        cli("Moving to the next thread")
        
        df.at[df.index[df['Facebook Name'] == profileName][0],'Comments'] = int(totalComments)
        df.to_excel('grind.xlsx', index=False)
        
        
        isThreadGood = True
      except Exception as error:
        if errorCounter > 5:
          threadCounter += 1
          isThreadGood = True
        errorCounter += 1
        print("--- ERROR ---")
  
  for i in range(5):
    cli("Moving to the next thread in "+ str(5 - (i + 1)) + " seconds")
    time.sleep(1)
    
  profCounter += 1
  browser.quit()  
    
# TIME FOR RECORDING
end_time = time.time()
duration_seconds = end_time - start_time
print("Duration in seconds:", duration_seconds)

# input("Press Enter to continue...")

