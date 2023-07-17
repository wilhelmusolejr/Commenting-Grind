from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import threading
import time

def start(index):
  option = webdriver.ChromeOptions()
  # option.add_argument('--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data')
  profile_path = f"--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\Profile {index}"
  option.add_argument(profile_path)
  
  print(f"Thread: {index}\
    Profile path: {profile_path}")
  
  # service = Service('driver\chromedriver.exe')
  driver = webdriver.Chrome(executable_path='driver\chromedriver.exe', options=option)
  
  driver.get("https://youtube.com")
  time.sleep(5)
  driver.quit()
  
  
def worker(index):
  option = webdriver.ChromeOptions()
  option.add_argument('--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data')
  profile_path = f"--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\Profile {index}"
  option.add_argument(profile_path)
  
  print(f"Thread: {index}\
    Profile path: {profile_path}")
  
  # service = Service('driver\chromedriver.exe')
  driver = webdriver.Chrome(executable_path='driver\chromedriver.exe', options=option)
  
  driver.get("https://facebook.com")
  time.sleep(5)
  driver.quit()
  
def main():
  profiles = []
  
  # for i in range(2):
  profiles += [threading.Thread(target=start, args=[11])]
  profiles += [threading.Thread(target=worker, args=[6])]
    
  for i in profiles:
    i.start()
    
  for i in profiles:
    i.join()
    
if __name__ == '__main__':
  main()