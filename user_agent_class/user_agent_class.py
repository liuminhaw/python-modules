"""
Program:
    User-agent data for use in web scraping
Author:
    haw
Version:
    2.1.0
"""

import sys, random
import requests
from bs4 import BeautifulSoup
from datetime import datetime


URL_COMPUTER = 'https://developers.whatismybrowser.com/useragents/explore/hardware_type_specific/computer/'
URL_PHONE = 'https://developers.whatismybrowser.com/useragents/explore/hardware_type_specific/phone/'
URL_FIREFOX = 'https://developers.whatismybrowser.com/useragents/explore/software_name/firefox/'
URL_CHROME = 'https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/'

SELECTOR = 'td.useragent a'



class UserAgent():

    def __init__(self):
        # Default user agent value
        self._filename = 'user_agents-' + datetime.now().strftime('%Y%m%d')


    def random_computer(self):
        """
        Success: Return a random user-agent
        Failed: Return an empty list
        """
        return self._load_random(URL_COMPUTER)

    def random_phone(self):
        """
        Success: Return a random user-agent
        Failed: Return an empty list
        """
        return self._load_random(URL_PHONE)

    def random_firefox(self):
        """
        Sucess: Return a random user-agent
        Failed: Return an empty list
        """
        return self._load_random(URL_FIREFOX)

    def random_chrome(self):
        """
        Success: Return a random user-agent
        Failed: Return an empty list
        """
        return self._load_random(URL_CHROME)

    def write_computer(self):
        self._filename = 'user_agents-computer-' + datetime.now().strftime('%Y%m%d')
        self._write_file(URL_COMPUTER)

    def write_phone(self):
        self._filename = 'user_agents-phone-' + datetime.now().strftime('%Y%m%d')
        self._write_file(URL_PHONE)

    def write_firefox(self):
        self._filename = 'user_agents-firefox-' + datetime.now().strftime('%Y%m%d')
        self._write_file(URL_FIREFOX)

    def write_chrome(self):
        self._filename = 'user_agents-chrome-' + datetime.now().strftime('%Y%m%d')
        self._write_file(URL_CHROME)


    def _load_random(self, url):
        """
        Randomly return an user-agent value
        or an empty list if no data is fetched
        """
        selected_list = self._scrape_for_user_agent(url)

        try:
            user_agent = random.choice(selected_list)
        except IndexError:
            return selected_list
        else:
            return user_agent.text


    def _write_file(self, url):
        """
        Save user-agent data to file
        """
        selected_list = self._scrape_for_user_agent(url)

        if len(selected_list) != 0:
            with open(self._filename, 'w') as write_file:
                for elem in selected_list:
                    write_file.write('{}\n'.format(elem.text))

            print('Write user-agent to file {} success.'.format(self._filename))
        else:
            print('No user-agent data write to file.')


    def _scrape_for_user_agent(self, url_type):
        """
        Get and return list of fetched data
        Return an empty list if request failed
        """
        # Request for web page
        try:
            req = requests.get(url_type)
            req.raise_for_status()
        except:
            return []

        # Grab information
        soup = BeautifulSoup(req.text, 'html.parser')
        selected_elem = soup.select(SELECTOR)

        return selected_elem


if __name__ == '__main__':
    test = UserAgent()

    print(test.random_computer())
    print(test.random_phone())
    print(test.random_firefox())
    print(test.random_chrome())

    test.write_computer()
    test.write_phone()
    test.write_firefox()
    test.write_chrome()
