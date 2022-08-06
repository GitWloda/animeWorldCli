#for animation
import time
import itertools
import threading
from termcolor import colored

#for video
import sys
import os

#for driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def exitSite():
    for i in range(driver_len - 1, 0, -1):
        driver.switch_to.window(driver.window_handles[i]) #will close the last tab first.
        driver.close()
        #print("Closed Tab No. ", i)
        driver.switch_to.window(driver.window_handles[0]) # Switching the driver focus to First tab.

print("Anime World "+colored("I","green")+"T"+colored("A","red")+" CLI... START")

#here is the animation
def animate(loadText):
    i=0
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        if i < 8:
            sys.stdout.write(colored("\r"+loadText + c, "green"))
        if i >= 8 and i < 16:
            sys.stdout.write(colored("\r"+loadText + c, "white"))
        if i >= 16 and i < 24:
            sys.stdout.write(colored("\r"+loadText + c, "red"))
        if i >= 24:
            i=0
        i+=1
        sys.stdout.flush()
        time.sleep(0.2)
    print(" ")
    print("COMPLETE")

t = threading.Thread(target=animate, args=("SEARCHING FOR: "+sys.argv[1]+"... ",))
done = False
t.start()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('window-size=1920x1080')
prefs = {"profile.managed_default_content_settings.images" : 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)
#driver.set_window_size(1920, 1080, driver.window_handles[0])
link = sys.argv[1].replace(" ", "+")
driver.get('https://www.animeworld.tv/search?keyword='+link)

#driver_len = len(driver.window_handles) #fetching the Number of Opened tabs
#print("Length of Driver = ", driver_len)
#if driver_len > 1: # Will execute if more than 1 tabs found.
#    for i in range(driver_len - 1, 0, -1):
#        driver.switch_to.window(driver.window_handles[i]) #will close the last tab first.
#        driver.close()
#        print("Closed Tab No. ", i)
#    driver.switch_to.window(driver.window_handles[0]) # Switching the driver focus to First tab.
#else:
#    print("Found only Single tab.")

element = driver.find_element(By.ID, "sidebar")

driver.execute_script("""
var element = arguments[0];
element.parentNode.removeChild(element);
""", element)

AName = driver.find_elements(By.CLASS_NAME, "name")
done = True
time.sleep(0.2)
if len(sys.argv) > 2:
    name = sys.argv[2]
else:
    i = 0
    for x in AName:
        print(str(i).ljust(4)+"-> "+x.get_attribute("href")[31:])
        i += 1
    name = int(input("select anime: "))
x=AName[int(name)].get_attribute("href")
t = threading.Thread(target=animate, args=("OPENING ANIME: "+x[31:]+"... ",))
done = False
t.start()
driver.get(x)

#video = driver.find_element(By.ID, "player-cover").click()
#driver_len = len(driver.window_handles) #fetching the Number of Opened tabs
#print("Length of Driver = ", driver_len)
#if driver_len > 1: # Will execute if more than 1 tabs found.
#    exitSite()
#else:
#    print("Found only Single tab.")

#video = driver.find_element(By.ID, "player").click()
#driver_len = len(driver.window_handles) #fetching the Number of Opened tabs
#print("Length of Driver = ", driver_len)
#if driver_len > 1: # Will execute if more than 1 tabs found.
#    exitSite()
#else:
#    print("Found only Single tab.")
done = True
time.sleep(0.2)
if len(sys.argv) > 3:
    Aep = sys.argv[3]
else:
    Aep = int(input("num. EP"))

t = threading.Thread(target=animate, args=("OPENING EP: "+str(Aep)+"... ",))
done = False
t.start()

try:
    driver.find_element(By.XPATH, "//*[@id=\"animeId\"]/div[2]/div[3]/div/span[1]")
except:
    driver.find_element(By.XPATH, "//*[@id=\"animeId\"]/div[2]/div[3]/ul/li["+str(Aep)+"]/a").click()
    driver_len = len(driver.window_handles) #fetching the Number of Opened tabs
    #print("Length of Driver = ", driver_len)
    exitSite()
else:
    group = 1
    groupNow = 0
    while int(Aep) > int(groupNow):
        groupNow = driver.find_element(By.XPATH, "//*[@id=\"animeId\"]/div[2]/div[3]/div/span["+str(group)+"]").text
        group += 1
        ch = '-'
        # Remove all characters before the character '-' from string
        listOfWords = groupNow.split(ch, 1)
        if len(listOfWords) > 0: 
            groupNow = listOfWords[1]
            groupNow = groupNow[1:]
        else:
            print(groupNow)
    group -= 1
    #print(group)
    driver.find_element(By.XPATH, "//*[@id=\"animeId\"]/div[2]/div[3]/div/span["+str(group)+"]").click()
    driver_len = len(driver.window_handles) #fetching the Number of Opened tabs
    #print("Length of Driver = ", driver_len)
    exitSite()
    i = 1
    AepNow = 1
    while int(Aep) > int(AepNow):
        AepNow = driver.find_element(By.XPATH, "//*[@id=\"animeId\"]/div[2]/div[3]/ul["+str(group)+"]/li["+str(i)+"]/a").text
        if int(Aep) == int(AepNow):
            driver.find_element(By.XPATH, "//*[@id=\"animeId\"]/div[2]/div[3]/ul["+str(group)+"]/li["+str(i)+"]/a").click()
        else:
            i += 1

#if driver.find_element(By.XPATH, "//*[@id=\"animeId\"]/div[2]/div[3]/div"):
#    rangeEP = int(Aep/50)
#    rangeEP = int(rangeEP+1)
#    print(rangeEP)
#    driver.find_element(By.XPATH, "//*[@id=\"animeId\"]/div[2]/div[3]/div/span["+str(rangeEP)+"]").click()
#    driver_len = len(driver.window_handles) #fetching the Number of Opened tabs
#    print("Length of Driver = ", driver_len)
#    if driver_len > 1: # Will execute if more than 1 tabs found.
#        for i in range(driver_len - 1, 0, -1):
#            driver.switch_to.window(driver.window_handles[i]) #will close the last tab first.
#            driver.close()
#            print("Closed Tab No. ", i)
#            driver.switch_to.window(driver.window_handles[0]) # Switching the driver focus to First tab.
#    else:
#        print("Found only Single tab.")
#        driver_len = len(driver.window_handles) #fetching the Number of Opened tabs
#        print("Length of Driver = ", driver_len)
#        if driver_len > 1: # Will execute if more than 1 tabs found.
#            for i in range(driver_len - 1, 0, -1):
#                driver.switch_to.window(driver.window_handles[i]) #will close the last tab first.
#                driver.close()
#                print("Closed Tab No. ", i)
#                driver.switch_to.window(driver.window_handles[0]) # Switching the driver focus to First tab.
#        else:
#            print("Found only Single tab.")

#i = 0
#x = 0
#y = 0
#j = 0
#while x == 0:
#    if driver.find_element(By.XPATH, "//*[@id=\"animeId\"]/div[2]/div[3]/div/span[0]"):
#        i += 1
#        while y == 0:
#            if driver.find_element(By.XPATH, "//*[@id=\"animeId\"]/div[2]/div[3]/ul[3]/li["+str(j)+"]"):
#                j += 1
#                x = 1
#                y = 1
#print(driver.find_element(By.XPATH, "//*[@id=\"animeId\"]/div[2]/div[3]/ul[3]/li[1]"))

#AepClick = str(Aep)[-2:]
#print(AepClick)
#if int(AepClick) > 50:
#    AepClick = int(AepClick)-50
#    print(AepClick)
#driver.find_element(By.XPATH, "//*[@id=\"animeId\"]/div[2]/div[3]/ul[5]/li["+str(AepClick)+"]/a").click()
WLink = driver.find_element(By.ID, "downloadLink").get_attribute("href")
driver.get(WLink)
WLink = driver.find_element(By.XPATH, "/html/body/div[2]/a").get_attribute("href")
#print(WLink)
done = True
os.system("mpv " + WLink)


#driver.quit()
