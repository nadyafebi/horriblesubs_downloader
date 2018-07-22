import os, sys, re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

HORRIBLE = 'https://horriblesubs.info/shows/'

# Selenium Settings
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--log-level=3")
chrome_driver = os.getcwd() + "\\chromedriver.exe"

def getTorrent(name, episodes, resolution=1080):
    # Open up browser
    sys.stdout.write('Opening browser...')
    sys.stdout.flush()
    browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    browser.get(makeLink(name))

    # Return if page not found
    if browser.title == 'Page not found – HorribleSubs':
        browser.quit()
        return "ERROR: Page not found!"

    # Click 'Show More' button until it ends.
    show_more = browser.find_element_by_xpath("//div[@class='show-more']")
    while show_more.text != "The End":
        show_more.click()

    # Get the torrent link
    links = []
    for episode in episodes:
        tag = makeTag(episode, resolution)
        try:
            q = "//div[@id='{}']//a[@title='Torrent Link']".format(tag)
            episode_container = browser.find_element_by_xpath(q)
            links.append(episode_container.get_attribute("href"))
        except:
            browser.quit()
            return "ERROR: Cannot find episode!"

    # Quit browser and return link
    browser.quit()
    return links

def makeLink(name):
    # Remove symbols
    name = re.sub(r'[^\w\s]', '', name)
    # Replace spaces with dash
    name = '-'.join(name.split())
    # Return HorribleSubs link
    return HORRIBLE + name

def makeTag(episode, resolution):
    if episode < 10:
        episode = '0' + str(episode)
    return '{}-{}p'.format(episode, resolution)
