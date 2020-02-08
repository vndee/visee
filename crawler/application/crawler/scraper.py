import os
from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from application.helpers.utils import ensure_dir


class BasicWebDriver:
    def __init__(self, executable_path='', timeout=15, wait=15):
        # download_dir = os.path.join(os.getcwd(), 'download/')
        # ensure_dir(download_dir)

        selenium_options = Options()
        # selenium_options.add_argument('--headless')
        selenium_options.add_argument('--no-sandbox')
        # selenium_options.add_argument('--disable-dev-shm-usage')
        selenium_options.add_argument('--dns-prefetch-disable')
        selenium_options.headless = True
        selenium_options.add_experimental_option(
            'prefs',
            {
                # 'download.default_directory': download_dir
            }
        )

        self.driver = webdriver.Chrome(executable_path=executable_path, chrome_options=selenium_options)
        self.driver.set_page_load_timeout(timeout)
        self.wait = WebDriverWait(self.driver, wait)
        self.driver.implicitly_wait(wait)
        self.ignore_index = False

    def get_html(self, url):
        try:
            self.driver.get(url)
            time.sleep(0.5)
        except TimeoutException as toe:
            print(toe)
            self.driver.refresh()
            print(url)
        except Exception as ex:
            print(ex)

    def execute_script(self, script):
        try:
            self.driver.execute_script(script)
        except Exception as ex:
            print(ex)
