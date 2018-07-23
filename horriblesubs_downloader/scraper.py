import os, re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

HORRIBLE = 'https://horriblesubs.info/shows/'

# Selenium Settings
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--log-level=3")
chrome_driver = os.getcwd() + "\\chromedriver.exe"

class Scraper(object):
    def __init__(self, anime_info):
        self.name = anime_info['name']
        self.episodes = anime_info['episodes']
        self.resolution = anime_info['resolution']
        self.browser = None

    def openBrowser(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
        self.browser.get(makeLink(self.name))

    def getTorrent(self):
        # Check if page is not found
        if self.browser.title == 'Page not found - HorribleSubs':
            self.browser.quit()
            return 'ERROR: Page not found!'

        # Click 'Show More' button until it ends.
        show_more = self.browser.find_element_by_xpath("//div[@class='show-more']")
        while show_more.text != "The End":
            show_more.click()

        # Get the torrent link
        links = []
        for episode in self.episodes:
            tag = makeTag(episode, self.resolution)
            try:
                q = "//div[@id='{}']//a[@title='Torrent Link']".format(tag)
                episode_container = self.browser.find_element_by_xpath(q)
                links.append(episode_container.get_attribute("href"))
            except:
                self.browser.quit()
                return "ERROR: Cannot find episode!"

        # Quit browser and return link
        self.browser.quit()
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
