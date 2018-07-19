import re
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

HORRIBLE = 'https://horriblesubs.info/shows/'

# Selenium Settings
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--log-level=3")
chrome_driver = os.getcwd() + "\\chromedriver.exe"

def getTorrent(name, episode, resolution=1080):
    # Get HorribleSubs link and tag
    link = makeLink(name)
    tag = makeTag(episode, resolution)

    # Open up browser
    browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    browser.get(link)

    # Click 'Show More' button until it ends.
    show_more = browser.find_element_by_xpath("//div[@class='show-more']")
    while show_more.text != "The End":
        show_more.click()

    # Get the torrent link
    q = "//div[@id='{}']//a[@title='Torrent Link']".format(tag)
    episode_container = browser.find_element_by_xpath(q)
    torrent_link = episode_container.get_attribute("href")

    # Quit browser and return link
    browser.quit()
    return torrent_link

def makeLink(name):
    # Remove symbols
    name = re.sub(r'[^\w\s]', '', name)
    # Replace spaces with dash
    name = '-'.join(name.split())
    # Return HorribleSubs link
    return HORRIBLE + name

def makeTag(episode, resolution):
    if int(episode) < 10:
        episode = '0' + episode
    return '{}-{}p'.format(episode, resolution)
