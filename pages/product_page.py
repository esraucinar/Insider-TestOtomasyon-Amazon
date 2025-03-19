from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.home_page import HomePage




class ProductPage(BasePage):
        PRODUCT_PAGE_PRODUCTS_VIEW_ITEM = (By.XPATH,"(//div[@data-component-type='s-search-result' and not(contains(@class, 'AdHolder'))])[{index}]//a[contains(@href, '/dp/')]")
        SECOND_PAGE_LINK = (By.XPATH, "//a[contains(@aria-label, '2 sayfasına git')]")
        PRODUCT_TITLE = (By.XPATH, "//span[@id='productTitle']")

        def __init__(self, driver):
            super().__init__(driver)

        def go_to_product_item(self, index):
            product_xpath = (By.XPATH,f"(//div[@data-component-type='s-search-result'][not(.//span[contains(text(), 'Sponsorlu')])])[{index}]//a")
            title_xpath = (By.XPATH, "//span[@id='productTitle']")

            product_element = self.wait.until(EC.presence_of_element_located(product_xpath))
            product_url = product_element.get_attribute("href")

            self.click(*product_xpath)
            print(f"{index}. ürüne tıklandı.")

            self.wait.until(EC.presence_of_element_located(title_xpath))

            product_title_element = self.driver.find_element(*title_xpath)
            BasePage.selected_product_title = product_title_element.text.strip()
            print(f"Ürün Sayfasında Bulunan Başlık: {BasePage.selected_product_title}")


            current_url = self.driver.current_url
            print(f"Açılan Sayfanın URL'si: {current_url}")


            assert product_url in current_url, f"Yanlış ürün açıldı! Beklenen: {product_url}, Açılan: {current_url}"

        def verify_product_in_cart(self):
            homepage = HomePage(self.driver)
            homepage.go_to_cart()

            print(f" Kaydedilen ürün başlığı = {BasePage.selected_product_title}")
            print(f" Sepetteki ürün başlığı = {BasePage.cart_product_title}")

            cart_product_title_element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='a-truncate-cut']")))
            BasePage.cart_product_title = cart_product_title_element.text.strip()
            print(f"Sepetteki Ürün: {BasePage.cart_product_title}")


            if not BasePage.selected_product_title or not BasePage.cart_product_title:
                raise AssertionError("Ürün başlığı kaydedilmediği için doğrulama yapılamadı!")


            assert BasePage.selected_product_title in BasePage.cart_product_title, (
                f"Yanlış ürün sepete eklendi! Beklenen: {BasePage.selected_product_title}, Sepette: {BasePage.cart_product_title}"
            )
            print("Sepete eklenen ürün doğru!")


        def go_to_second_page(self):
            self.scroll_to_element(*self.SECOND_PAGE_LINK)
            time.sleep(3)

            self.click(*self.SECOND_PAGE_LINK)
            print("2. sayfaya tıklandı.")

            time.sleep(3)

            print(f"Sayfa yönlendirildi: {self.driver.current_url}")

            bottom_element = (By.XPATH, "(//div[@data-component-type='s-search-result'])[6]")
            self.scroll_to_element(*bottom_element)
            time.sleep(2)

            self.take_screenshot("after_click_second_page.png")
            print("2. sayfa açıldı ve aşağı kaydırıldı.")


        def verify_product_page(self):
            current_url = self.driver.current_url
            assert "/dp/" in current_url, f"Ürün sayfasında değil! Mevcut URL: {current_url}"

            try:

                product_title = self.wait.until(EC.presence_of_element_located((By.ID, "productTitle")))
                assert product_title.is_displayed(), "Ürün başlığı bulunamadı!"
                print(f"Ürün sayfasındasın! Ürün Başlığı: {product_title.text}")
                self.take_screenshot("product_page_verified.png")

            except Exception as e:
                print(f"Ürün sayfası doğrulama başarısız! Hata: {e}")
                self.take_screenshot("error_not_on_product_page.png")
                raise AssertionError("Ürün sayfası doğrulama başarısız!")

        def add_product_to_cart(self):
            try:
                add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button")))
                add_to_cart_button.click()
                print("'Sepete Ekle' butonuna tıklandı.")

            except TimeoutException:
                print("'Sepete Ekle' butonu yok, alternatif yöntem denenecek...")

                try:
                    buying_options_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='buybox-see-all-buying-choices']/span/a")))
                    buying_options_button.click()
                    print("'Satın Alma Seçeneklerini Gör' butonuna tıklandı.")


                    alternative_add_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@name='submit.addToCart'])[1]")))

                    self.driver.execute_script("arguments[0].scrollIntoView(true);", alternative_add_button)
                    time.sleep(1)
                    alternative_add_button.click()
                    print("Alternatif sepete ekleme butonuna tıklandı.")

                except TimeoutException:
                    print("Alternatif yöntem de başarısız oldu.")
                    self.take_screenshot("error_alternative_method.png")
                    raise AssertionError("Alternatif yöntemle sepete ekleme başarısız!")


            self.take_screenshot("add_to_cart_success.png")
            print("Ürün sepete başarıyla eklendi!")






















