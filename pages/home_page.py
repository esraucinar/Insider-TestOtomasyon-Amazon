from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class HomePage(BasePage):
    def __init__(self, driver):
            super().__init__(driver)

    def is_on_home_page(self):
        expected_title = "Amazon.com.tr: Elektronik, bilgisayar, akıllı telefon, kitap, oyuncak, yapı market, ev, mutfak, oyun konsolları ürünleri ve daha fazlası için internet alışveriş sitesi"
        return expected_title.__eq__(self.get_title())


    def go_to_cart(self):
        cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "nav-cart")))
        cart_button.click()

        WebDriverWait(self.driver, 10).until(EC.url_contains("/gp/cart/view.html"))
        assert "cart/view.html" in self.driver.current_url, "Sepet sayfası açılmadı!"

        print(f"Alışveriş sepetine gidildi! URL: {self.driver.current_url}")
        self.take_screenshot("cart_page.png")


        cart_product_title_element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='a-truncate-cut']")))
        BasePage.cart_product_title = cart_product_title_element.text.strip()
        print(f"Sepetteki Ürün: {BasePage.cart_product_title}")


    def cart_product_delete(self):
        try:
            delete_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@value='Sil'])[1]")))
            delete_button.click()
            print("Sepetteki ürün başarıyla silindi!")
        except TimeoutException:
            self.take_screenshot("delete_product_error.png")
            print("Sepette ürün silme başarısız!")
            raise AssertionError("Sepetten ürün silinirken hata oluştu!")


    def verify_product_deleted_from_cart(self):
        try:
            confirmation = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'sc-list-item-removed-msg')]")))
            confirmation_text = confirmation.text
            assert "Alışveriş Sepetiniz konumundan kaldırıldı." in confirmation_text, "Silme mesajı doğrulanamadı!"
            self.take_screenshot("product_deleted.png")
            print("Alışveriş Sepetiniz konumundan kaldırıldı.")
        except TimeoutException:
            self.take_screenshot("product_delete_failed.png")
            raise AssertionError("Ürün silme doğrulanamadı!")


    def amazon_homepage(self):
        home_logo = self.wait.until(EC.element_to_be_clickable((By.ID, "nav-logo-sprites")))
        home_logo.click()


    def is_at_amazon_homepage(self):
        # Anasayfada olduğunun doğrulaması için URL kontrol edilir.
        return WebDriverWait(self.driver, 10).until(EC.url_to_be("https://www.amazon.com.tr/ref=nav_logo"))








