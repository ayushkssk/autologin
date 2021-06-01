from selenium import webdriver
from getpass import getpass

# username = input("Your Email")
# password = getpass("Your Password")
driver = webdriver.Chrome("C:\\webdriver\\chromedriver.exe")
# driver.get("https://www.facebook.com/")
driver.get("https://webmail1.hostinger.in/?_task=mail&_mbox=INBOX")
# username_textbox = driver.find_element_by_id("email")
username_textbox = driver.find_element_by_id("rcmloginuser")
# username_textbox.send_keys(username)
username_textbox.send_keys("ayush.kssk@devwings.in")

password_textbox = driver.find_element_by_id("rcmloginpwd")
#password_textbox.send_keys(password)
password_textbox.send_keys("Devwings*0987")

login_button = driver.find_element_by_id("rcmloginsubmit")
login_button.submit()