from selenium import webdriver
import time

#load driver
driver = webdriver.Chrome()

def isMessageExist():
    # click Load Older Threads to load all messages..one simple click is enough it will load rest automatically
    #uiMore =  driver.find_element_by_link_text('Load Older Threads')
    #uiMore.click()
    els = driver.find_elements_by_class_name("_k-")
    if els.count()>0:
        return True
    else:
        return False



#get web page
driver.get("https://www.facebook.com/login.php")

#check if opened page is facebook
assert "Log in to Facebook | Facebook" in driver.title

#enter user credentials

email = driver.find_element_by_name("email")
password = driver.find_element_by_name("pass")
loginbtn = driver.find_element_by_name("login")

"""IMPORTANT!!!! please change followings """
#enter your email or phonenumber or username
email.send_keys(“username”)
# enter your password
password.send_keys(“password”)

loginbtn.submit()
#let user see login page
time.sleep(1)

#Navigate to messages page
driver.get("https://www.facebook.com/messages")
driver.implicitly_wait(100)

“””IMPORTANT  60 minutes given for you to reveal all of your messages in older threads”””
time.sleep(60)

elements = driver.find_elements_by_css_selector("a._k_")
for el in elements:
    webdriver.ActionChains(driver).move_to_element(el).click(el).perform()
    driver.implicitly_wait(100)
    pop = driver.find_elements_by_class_name("uiPopover")
    btn = pop[1].find_element_by_css_selector("button")
    webdriver.ActionChains(driver).move_to_element(btn).click(btn).perform()

    deleteln = driver.find_element_by_link_text("Delete Conversation...")
    webdriver.ActionChains(driver).move_to_element(deleteln).click(deleteln).perform()

    deletebtn = driver.find_element_by_link_text("Delete Conversation")
    webdriver.ActionChains(driver).move_to_element(deletebtn).click(deletebtn).perform()

    time.sleep(2)


driver.close()