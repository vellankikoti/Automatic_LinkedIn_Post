from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

baseUrl = "https://in.linkedin.com/"

#Maximize Window
driver.maximize_window()

driver.get(baseUrl)

#Waiting Time
driver.implicitly_wait(3)

#SignIn Page
loginLink = driver.find_element(By.XPATH,"/html/body/nav/a[3]")
loginLink.click()

#EMail / Username Field
emailField = driver.find_element(By.ID,"username")
emailField.send_keys("your username")

#Password Field
passwordField = driver.find_element(By.ID,"password")
passwordField.send_keys("yourpassword")

#SignIn Button
signinButton = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/main[1]/div[1]/form[1]/div[3]/button[1]")
signinButton.click()

time.sleep(5)

# Writing New Post
# Start Post Button
startPost = driver.find_element(By.XPATH,"//button[@class='share-box__open share-box__trigger p4 hoverable-link-text t-16 t-black--light t-bold']")
startPost.click()

time.sleep(3)

#Text Box
textBox = driver.find_element(By.CLASS_NAME,"mentions-texteditor__content")
textBox.send_keys("This is the Test Post from Selenium Script    ",  Keys.ENTER)
textBox.send_keys(Keys.ENTER)
#Sending Hash Tags
textBox.send_keys("#Selenium    #Automation    #Testing    #Python    #Scripting    #LinkedIn    #Post    #Koti_Vellanki")

time.sleep(2)

# Post Button
postButton = driver.find_element(By.XPATH,"//span[text()='Post']")
postButton.click()

# Waiting 10 seconds to see post
time.sleep(10)

#User Tab
userButton = driver.find_element(By.XPATH,"/html[1]/body[1]/header[1]/div[1]/nav[1]/ul[1]/li[6]/div[1]/div[1]/button[1]")
userButton.click()

time.sleep(2)
#SignOut
signoutButton = driver.find_element(By.XPATH,"/html[1]/body[1]/header[1]/div[1]/nav[1]/ul[1]/li[6]/div[1]/div[1]/ul[1]/li[5]/ul[1]/li[1]/a[1]")
signoutButton.click()

time.sleep(2)

# Closing Window
driver.close()