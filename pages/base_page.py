from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging
from selenium.common.exceptions import TimeoutException
import os



class BasePage():
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")
    selected_product_title = None

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(driver)

    def go_to_url(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def wait_for_clickable(self, by, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by,locator)))

    def click(self, by, locator):
        self.wait_for_clickable(by,locator).click()

    def search(self, keyword):
        search_box = self.wait.until(EC.presence_of_element_located(self.SEARCH_BOX))
        search_box.send_keys(keyword)
        search_button = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        search_button.click()

    def scroll_to_element(self, by, locator):
        element = self.driver.find_element(by, locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

    def move_mouse_randomly(self):
        self.action.move_by_offset(5, 5).perform()


    def close_popups(self):
        try:
            popup = self.wait.until(EC.element_to_be_clickable((By.ID, "sp-cc-accept")))
            popup.click()
            logging.info("Çerez popup'ı başarıyla kapatıldı.")
        except TimeoutException:
            logging.info("Çerez popup'ı görünmedi, devam ediliyor.")

    def wait_until_visible(self, by, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, locator)))


    def take_screenshot(self, filename="screenshot.png"):
        os.makedirs("screenshot", exist_ok=True)
        self.driver.save_screenshot(f"screenshot/{filename}")
        print(f"Screenshot alındı: screenshot/{filename}")











