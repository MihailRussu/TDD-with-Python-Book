from selenium import webdriver

# initialize the browser object
browser = webdriver.Firefox()

# open the browser with our ptoject
browser.get('http://localhost:8000')

# see if the title contains "Django" 
assert 'Django' in browser.title

# see of the page contains input element

# try to type something in that input

# try to hit "Enter" after typing and see if what was typed showed up

# try to add another item

# see if the page now has both items

# try to navigate to one item's url

# see if the navigated url contains everything

# quit the browser
browser.quit()
