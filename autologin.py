from selenium import webdriver
from selenium.webdriver.common.by import By
from getpass import getpass

# username = input("Your Email")
# password = getpass("Your Password")
driver = webdriver.Safari()
driver.get("https://webmail1.hostinger.in/?_task=mail&_mbox=INBOX")

username_textbox = driver.find_element(By.ID, "rcmloginuser")
username_textbox.send_keys("ayush.kssk@devwings.in")

password_textbox = driver.find_element(By.ID, "rcmloginpwd")
password_textbox.send_keys("Devwings*0987")

login_button = driver.find_element(By.ID, "rcmloginsubmit")
login_button.click()