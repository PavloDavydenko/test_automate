from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://demoblaze.com/index.html')

    def click_galaxy_x6(self):
        galaxy_x6 = self.driver.find_element(By.LINK_TEXT, 'Samsung galaxy s6')
        galaxy_x6.click()

    def click_monitor(self):
        monitor_link = self.driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
        monitor_link.click()

    def check_products_count(self, count):
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.find_elements(By.CSS_SELECTOR, '.card')) == count
        )
        monitors = self.driver.find_elements(By.CSS_SELECTOR, '.card')
        assert len(monitors) == count
