import openai


# time
import time

import random

# selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# TIME FOR RECORDING
start_time = time.time()

def typeOfMessage():
  typesFeeling = ["joy", "fun", "engaging", "supportive", "appreciation", "excitement", "wholesome"]
  randominium = random.randint(0, len(typesFeeling) -1)
  return typesFeeling[randominium]

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
facebook.append(Facebook("posts/760803052712859/?comment_id=760875826038915","comment"))
facebook.append(Facebook("posts/760935576032940/?comment_id=760936562699508","comment"))
facebook.append(Facebook("posts/759704576156040/?comment_id=759705089489322","comment"))
facebook.append(Facebook("posts/759704576156040?comment_id=759787379481093","comment"))
facebook.append(Facebook("posts/759704576156040?comment_id=759776516148846","comment"))
facebook.append(Facebook("posts/756628039797027/?comment_id=756721556454342","comment"))
facebook.append(Facebook("posts/756628039797027?comment_id=756683659791465","comment"))
facebook.append(Facebook("posts/756628039797027?comment_id=756796763113488","comment"))
facebook.append(Facebook("permalink/760006666125831/?comment_id=760014389458392","comment"))
facebook.append(Facebook("permalink/760006666125831/?comment_id=760019062791258","comment"))
facebook.append(Facebook("permalink/759741329485698/?comment_id=759775512815613","comment"))
facebook.append(Facebook("permalink/759741329485698/?comment_id=759819346144563","comment"))
facebook.append(Facebook("permalink/760929932700171/?comment_id=760933352699829","comment"))
facebook.append(Facebook("permalink/760929932700171/?comment_id=760932679366563","comment"))
facebook.append(Facebook("permalink/760803052712859/?comment_id=760883152704849","comment"))
facebook.append(Facebook("permalink/760803052712859/?comment_id=760902112702953","comment"))
facebook.append(Facebook("permalink/760803052712859/?comment_id=760885906037907","comment"))
facebook.append(Facebook("permalink/759741329485698/?comment_id=759988892794275","comment"))
facebook.append(Facebook("permalink/759741329485698/?comment_id=760730616053436","comment"))
facebook.append(Facebook("permalink/759741329485698/?comment_id=759839196142578","comment"))

profile = []
profile.append(Profile("Michael Castro", 11))

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

browsersProfile = [11, 25, 37, 40, 2, 24, 18, 22]
# browsersProfile = [22]


for profile in browsersProfile:
  print("Current profile: " + str(profile))
  testing = 0
  
  # WEBDRIVER CONFIGURATION
  if not testing:
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data')
    options.add_argument('--profile-directory=Profile '+ str(profile))
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
    options.add_argument('--user-agent="Mozilla/5.0 (Linux; Android 12; SM-N9750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36 EdgA/112.0.1722.46"')
    browser = webdriver.Chrome(executable_path='driver\chromedriver.exe', options= options)


  #---------------------------------------------------
  waiting_time = 20;
  
  #--------------------------
# CHAT GPT CONFIGURATION
  openai.api_key = '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'
  messages = [
      {"role": "system", "content": "You are a kind helpful assistant."},
  ]
  
  
  # STARTER
  threadCounter = 1

  for thread in facebook:
    isThreadGood = False
    while isThreadGood is False:
      try:
        print("Thread: number " + str(threadCounter))

        # Go to page
        browser.get(thread.link)
        
        commentElement = 'textarea'
        commentButtonElement = "div[aria-label='SEND']"
        
        chatGptFeedback = False
        randomSentence = ""

        # Comment
        WebDriverWait(browser, waiting_time).until(EC.presence_of_element_located((By.TAG_NAME, commentElement)))
        
        counter = 1
        while chatGptFeedback is not True:
          print('Run '+ str(counter) +' while at thread ' + str(threadCounter))
          try:
            thread.threadMessage = browser.execute_script('return document.querySelector("div[data-type=transactional] div[data-mcomponent=MContainer]").children[0].children[1].textContent') 
            print("Post: " + thread.threadMessage)
        
            timeAlloted = 60
            ai_start_time = time.time()
        
            # Generate Sentence
            print("Waiting for openAi response.")

            message = "What to reply to a "+ thread.postType +" '"+ thread.threadMessage +"' where the reply should agree to the "+ thread.postType +" and the "+ thread.postType +" is not referring to me it refers to someone else. Add a little bit praise and appreciation to PHDream. Do not provide translation. Use taglish dialect. Use simple words and make the reply short, that will make the reply written like a real human. "
            messages.append({"role": "user", "content": message},)
            chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            randomSentence = chat.choices[0].message.content
            browser.execute_script(f'document.querySelector("textarea").value = "{randomSentence}"')
            print(randomSentence)
        
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
        
        ai_end_time = time.time()
        
        timeTaken = int(ai_end_time - ai_start_time)
        
        forSleep = timeAlloted - timeTaken        
        
        if forSleep > 0:
          time.sleep(forSleep)
        
        print("Running next thread")

        threadCounter += 1
        isThreadGood = True
      except Exception as error:
        print("--- ERROR ---")
  
  time.sleep(5)
  browser.quit()  
    


  
# TIME FOR RECORDING
end_time = time.time()
duration_seconds = end_time - start_time
print("Duration in seconds:", duration_seconds)

# input("Press Enter to continue...")

