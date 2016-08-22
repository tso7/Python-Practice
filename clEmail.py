#! /usr/bin/python3
# clEmail.py - Command Line Emailer
# Usage: clEmail.py <send-to-email-address> <message>

import sys, re, time
from selenium import webdriver

# TODO: Retrieve from encrypted file instead
username = 'dummypyth@gmail.com'
password = 'spambacon'  # Not secure, I know, deal with it

def timeout(tryStatement, timer):
    timeout = time.time() + timer + 0.1
    while True:
        if time.time() > timeout:
            print('Request timed out. Check internet connection.')
            sys.exit()
        try:
            element = eval(tryStatement)
        except:
            time.sleep(2)
            continue

        return element

# Set up email regex for validation
emailRegex = re.compile(r'[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$')

# Check for valid command line arguments
if len(sys.argv) != 3:
    print('Invalid arguments. Usage: clEmail.py <send-to-email-address>\
    <message>')
    sys.exit()
elif emailRegex.match(sys.argv[1]) == None:
    print('Invalid email address format. Please check input.')
    sys.exit()

# Load chromedriver
print('Opening browser...')
browser = webdriver.Chrome()
browser.get('https://www.gmail.com')
print('Logging onto gmail...')

# Logon using credentials
emailElem = browser.find_element_by_id('Email')
emailElem.send_keys(username)
emailElem.submit()

# Wait for password screen (10 seconds)
passwordElem = timeout("browser.find_element_by_id('Passwd')", 10)
passwordElem.send_keys(password)
passwordElem.submit()

# Wait for inbox (15 seconds)
print('Logged on! Composing mail...')
composeElem = timeout("browser.find_element_by_class_name('z0')", 15)
composeElem.click()

# Wait for compose window(15 seconds)
toElem = timeout("browser.find_element_by_name('to')", 15)

# Fill in email fields and Send
toElem.send_keys(sys.argv[1])
subjectElem = browser.find_element_by_name('subjectbox')
subjectElem.send_keys('Email sent via command line Python script')
bodyElem = browser.find_element_by_css_selector("div[aria-label='Message Body']")
bodyElem.send_keys(sys.argv[2])
browser.find_element_by_xpath("//div[contains(text(),'Send')]").click()
print('Mail completed. Sending...')

# Wait for confirmation
timeout("browser.find_element_by_xpath(\"//div[@class='vh'][contains(text(),'Your message has been sent')]\")", 10)
time.sleep(2)
browser.find_element_by_xpath("//a[contains(@title, 'Google Account')]").click()
time.sleep(1)
browser.find_element_by_xpath("//a[text()='Sign out']").click()
time.sleep(2)    
browser.quit()
print('Mail sent to: ' + sys.argv[1])
