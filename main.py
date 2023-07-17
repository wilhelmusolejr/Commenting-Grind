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
# jamaica solona - 7

import openai

import time
from datetime import date

import random
import os

import requests

import pandas as pd

# selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#--------------------------
# FUNCTION
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
  print("Current status     : " + str(threadCounter) + " out of " + str(fbThreadDF.shape[0]))
  print("Current activity   : " + status)
  print("*************************************")
  
def sendMessageTelegram(TOKEN, chat_id, message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()
    
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
     
    return "%d:%02d:%02d" % (hour, minutes, seconds)
  
def generateRandomSentence():
  starterMessage = ["Ay true ka jan ses", "Totoo hahaha", "Sinabi mo pa dzai,", 
                    "Agreeng agree ako jan sa comment mo", "Sinabi mo pa hehe,", 
                    "Ay very true yan", "Talaga nga noh,", "Super agree po,", "Tumpak na tumpak!"]
  miniStarter = ['', "alam mo ba,", "share ko lang ha,", "pero", "basta", "tapos", "tas ano nga"]
  middleMessage = ['ang swerte talaga noh', "Nadali mo po", "sana ako din sa susunod", "ang sarap talaga feeling pag ganyan", 
                   "sobrang deseeerve talagaaaaa", "try ko nga ulit hihi, na eexcite na ako", 
                   "wow na wow", "astig talaga", "madali lang din makapag cash out", "madali lang din maglaro eh",
                   "enjoy na enjoy talaga ako", "ang daming pwedeng pag pilian!"]
  complimentMessage = ["bukod don, legit and trusted pa ang PHDream", 
                       "grabe talaga ang impact ni phdream", "the best talaga ang PHDream", 
                       "PHDream all the way!", "have a wonderful day ka phdream", 
                       "basta ph dream always winner talaga noh", 
                       "katas nanaman ng phdream ang dami ng natulungan", 
                       "solid talaga ng PhDream", "easy and fast talaga ang PHDream", "kaya bet ko talaga tong PHdream eh"
                       , "super win na super win talaga kay ph dream"]
  lastMessage = ["more blessings po", "Sana all talagaaaaa", "more income to come para satin", "best wishes po", "easy salapi naman pala dito ihhh", 
                 "keep playing nalang ako para swertihin ulit", "push your luck madam", "", "forda game talaga lagi", "enjoyin lang ang game", "lezgooooo!"]
  emojiMessage = ["🥵", ",", "🤑😍", "😎", "!", "😍", '🤩', '🌟🥵🌟', "", "", "🤑🤑", "","🥵", "✨", "✨🤑✨", "", "✨✨", ":)", "^_^", "^^", " ", "", ":*"]

  gottenMessage = ['nabigyan ako ng chance para mabili ang mga gusto ko', 'nabili ko na lahat ng mga kailangan ko', 
                   'nakabili na din ako ng dream phone ko', 'nakakapag travel na ako', "ang saya lang hihi"]

  startSms = starterMessage[random.randrange(0,len(starterMessage))]
  miniStarterSms = miniStarter[random.randrange(0,len(miniStarter))]
  middleSms = middleMessage[random.randrange(0,len(middleMessage))]
  complimentSms = complimentMessage[random.randrange(0,len(complimentMessage))]
  lastSms = lastMessage[random.randrange(0,len(lastMessage))]
  gottenMessage = gottenMessage[random.randrange(0,len(gottenMessage))]
  
  addGottenMessage = random.randint(0, 1)
  text = startSms + " " + miniStarterSms + " " + middleSms + " " + str(emojiMessage[random.randrange(0,len(emojiMessage))]) + " " + complimentSms + " " + lastSms + " " + str(emojiMessage[random.randrange(0,len(emojiMessage))]) + " "
  
  if addGottenMessage:
    text += miniStarter[random.randrange(0,len(miniStarter))] + " " + gottenMessage
  
  return text
#--------------------------

#--------------------------
# CHAT GPT CONFIGURATION
openai.api_key = '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'
messages = [{"role": "system", "content": "You are a kind helpful assistant."}]
#--------------------------
# TELEGRAM CONFIGURATION
TOKEN = "6336647733:AAFL3PhVvfu_8k9yVa03M5iEz0Cw1oePlUM"
chat_id = "1559668342"
#--------------------------


telegramCode = str(random.randint(100, 999))

today = date.today()
todayDate = today.strftime("%B %d, %Y")

dummy = False

if dummy:
  grindFileName = "grind.xlsx"
  fbThreadFileName = "dummy_facebook_thread.xlsx"
else:
  grindFileName = "grind.xlsx"
  fbThreadFileName = "facebook_thread.xlsx"
  
triesNumber = 2
textLimit = 80

waiting_time = 10

#--------------------------
# PANDAS
# read excel
df = pd.read_excel(grindFileName, index_col=None)
fbThreadDF = pd.read_excel(fbThreadFileName, index_col=None)

# getting the last date
lastDate = df.iloc[df.shape[0] - 1]['Date']
if lastDate != todayDate:
  # print("Create blank")
  df.loc[len(df)] = [" ", " ", " "]
  tgMessage = " ----- " + str(todayDate) + " ----- "
  sendMessageTelegram(TOKEN, chat_id, tgMessage)


#--------------------------
# TIME FOR RECORDING
start_time = time.time()
#--------------------------




#--------------------------
# CLASS
class Facebook:
  def __init__(self, link, postType):
    self.link = "https://m.facebook.com/groups/phdream/" + link
    self.postType = postType
    self.threadMessage = ""
    self.messageFeeling = typeOfMessage()
    
  def trimUrl(link):
    return str(link[int(link.find("posts")):len(link)])
    
    
class Profile:
  def __init__(self, fullName, browserNumber):
    self.fullName = fullName
    self.browserNumber = browserNumber
    self.grindComment = 0
#--------------------------


#--------------------------
# INITIAL

profile = []
# profile.append(Profile("Moana Alonzo", 37)) # ---- suspended
# profile.append(Profile("Olgie Alonzo", 30)) # ---- suspended
# profile.append(Profile("Christian Abador", 2)) #===
profile.append(Profile("Kenny Sofer", 24))
# profile.append(Profile("Rhiana Alonzo",18)) # ---- not suspended
# profile.append(Profile("Brendan Eich", 22))
# profile.append(Profile("James Alarte", 16))
# profile.append(Profile("Michael Castro", 11))
# profile.append(Profile("Jerome Calawing", 35))
# profile.append(Profile("Sofia Andrade", 48))
# profile.append(Profile("Jenny Apakabago", 40))
profile.append(Profile("Jamaica Solona", 7))
# profile.append(Profile("Robert Hapiz", 6))
# profile.append(Profile("Jericho Yang", 25))


profCounter = 0
for prof in profile:
  isSuspeded = False
  profCounter += 1
  profileName = prof.fullName
  totalComments = 0
  
  # check if Profile Exist
  profileExist = df[(df['Facebook Name'] == profileName) & (df['Date'] == todayDate)].size
  
  if profileExist:
    # get latest total comments in excel
    totalComments = int(df.loc[df.index[(df['Facebook Name'] == profileName) & (df['Date'] == todayDate)]]["Comments"].values[0])
  else:
    # create profile to excel
    df.loc[len(df)] = [profileName, todayDate, totalComments]
    df.to_excel(grindFileName, index=False)
  
  testing = 0
  # WEBDRIVER CONFIGURATION
  if not testing:
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data')
    options.add_argument('--profile-directory=Profile '+ str(prof.browserNumber))
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
    
    # # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--user-agent="Mozilla/5.0 (Linux; Android 12; SM-N9750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36 EdgA/112.0.1722.46"')
    browser = webdriver.Chrome(executable_path='driver\chromedriver.exe', options= options)

  #---------------------------------------------------
  
  # STARTER
  errorCounter = 0
  threadCounter = 0
  timeAllotedIndex = 0
  for index, row in fbThreadDF.iterrows():
    threadLink = row['Facebook Link']
    threadType = row['Thread Type']
    threadStatus = row['Status']
    threadErrorCount = row['ErrorCount']
    
    threadCounter += 1
    isThreadGood = False
    
    thread_start_time = time.time()
    while isThreadGood is False:
      try:
        cli("Thread opened")

        # Go to page
        browser.get(threadLink)
        
        # Elements 
        commentElement = 'textarea'
        commentButtonElement = "div[aria-label='SEND']"
        suspendedElement = "#root > div._7om2"

        # _59k _2rgt _1j-f _2rgt
        try:
          WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, suspendedElement)))
          break
        except Exception as error:
          # Comment
          cli("Waiting for precense of comment element")
          # browser.get_screenshot_as_file("screenshot.png")
          WebDriverWait(browser, waiting_time).until(EC.presence_of_element_located((By.TAG_NAME, commentElement)))
          threadOpPost = browser.execute_script('return document.querySelector("div[data-type=transactional] div[data-mcomponent=MContainer]").children[0].children[1].textContent') 
        
        timeAlloted = random.randint(35, 70)
        timeAllotedArr = [60, 30, 50, 120, 60, 50, 30, 60, 70, 20, 60]
        # Generate Sentence

        cli(str(threadOpPost[0:50]) + "..." )
            
        if len(str(threadOpPost)) > textLimit:
          threadOpPost = threadOpPost[0:textLimit]

        # try:
        #   messageAi = "What to reply to a "+ threadType +" '"+ threadOpPost +"' where the reply should agree to the "+ threadOpPost +" and the "+ threadOpPost +" is not referring to me, it refers to someone else. Add a little bit praise and appreciation to PHDream. Use taglish dialect. Use simple words and make the reply short that will make it like written by real human."
        #   messages.append({"role": "user", "content": messageAi},)
        #   chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        #   aiFeedback = chat.choices[0].message.content
        # except Exception as error:
        #   aiFeedback = generateRandomSentence()
        
        aiFeedback = generateRandomSentence()
        
            
        browser.execute_script(f'document.querySelector("textarea").value = "{aiFeedback}"')
        cli("AI response received")
        
        browser.find_element(By.TAG_NAME, commentElement).send_keys(" ")

        # Button
        WebDriverWait(browser, waiting_time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, commentButtonElement)))
        browser.find_element(By.CSS_SELECTOR, commentButtonElement).click()
        
        cli("Response commented to the thread")
        
        waiting_timer = 10
        for i in range(waiting_timer):
            cli("Submitting comment. Ending in " + str(waiting_timer - (i + 1)) + " seconds")
            time.sleep(1)
        
        # browser.get_screenshot_as_file("screenshot" + str(random.randint(1,100)) +".png")

        # ai_end_time = time.time()
        thread_end_time = time.time()
        
        # timeTaken = int(ai_end_time - ai_start_time)
        timeTaken = int(thread_end_time - thread_start_time)
        
        forSleep = timeAllotedArr[timeAllotedIndex] - timeTaken  
        
        totalComments += 1
        
        if forSleep > 0:
          for i in range(forSleep):
            # print(timeAlloted)
            # print(timeTaken)
            # print(forSleep)
            cli("Alotted time: "+ str(timeAllotedArr[timeAllotedIndex]) +" | Sleeping for " + str(forSleep - (i + 1)) + " seconds")
            time.sleep(1)
          # cli("Sleeping for " + str(forSleep) + " seconds")
          # time.sleep(forSleep)
        
        cli("Moving to the next thread")
        
        df.at[df.index[(df['Facebook Name'] == profileName) & (df['Date'] == todayDate) ][0],'Comments'] = int(totalComments)
        df.to_excel(grindFileName, index=False)

        timeAllotedIndex += 1
        if timeAllotedIndex == len(timeAllotedArr):
          timeAllotedIndex = 0
        
        isThreadGood = True
      except Exception as error:
        if errorCounter > triesNumber:
          browser.get_screenshot_as_file("screenshot"+str(random.randint(100, 999))+".png")
          isThreadGood = True
        errorCounter += 1
        print("--- ERROR ---")
    
    waiting_timer = 3
    for i in range(waiting_timer):
      cli("Moving to the next thread in "+ str(waiting_timer - (i + 1)) + " seconds")
      time.sleep(1)
    
  
  waiting_timer = 5
  for i in range(waiting_timer):
    cli("Moving to the next profile in "+ str(waiting_timer - (i + 1)) + " seconds")
    time.sleep(1)
  
  try:
    tgMessage = " | " + telegramCode + " | " + str(profileName) + " -> " + str(totalComments) + " comments"
    sendMessageTelegram(TOKEN, chat_id, tgMessage)
  except Exception as error:
    print("Error occured at sending telegram message", error)
    

  browser.quit()
    
    
# TIME FOR RECORDING
end_time = time.time()
duration_seconds = int(end_time - start_time)

os.system('cls')
print("*************************************")
print("Duration in seconds:", convert(duration_seconds))
print("Run " + str(len(profile)) + " facebook profiles")
print("*************************************")
# input("Press Enter to continue...")

