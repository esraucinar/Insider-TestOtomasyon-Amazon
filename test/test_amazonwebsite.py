from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.home_page import HomePage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage


class TestAmazonWebSite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.amazon.com.tr/")
        self.driver.maximize_window()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))

    # 1. Step: Go to https://www.amazon.com.tr/
    def test_add_to_cart(self):
        home_page = HomePage(self.driver)
        home_page.go_to_url("https://www.amazon.com.tr/")
        home_page.close_popups()
        sleep(3)
    # 2. Step: Verify that you are on the home page.
        self.assertTrue(home_page.is_on_home_page(),"This is not homepage!")
        home_page.take_screenshot("homepage.png")

    # 3. Step: Type 'Samsung' in the search field at the top of the screen and perform search.
        category_page = CategoryPage(self.driver)
        product_name = "Samsung"
        category_page.search_product(product_name)
        WebDriverWait(self.driver, 5).until(EC.title_contains(product_name))
        self.assertIn(product_name.lower(), category_page.get_title().lower(), "No results found.")


    # 4. Step: Verify that there are results for Samsung on the page that appears.
        self.assertTrue(category_page.is_on_category_page(), "This is not category page!")
        category_page.take_screenshot("category_page.png")
        sleep(3)


    # 5. Step: Click on the 2nd page from the search results and verify that the 2nd page is currently displayed on the page that opens.
        product_page = ProductPage(self.driver)
        product_page.go_to_second_page()
        product_page.take_screenshot("product_page.png")

    # 6. Step: Go to the 3rd Product page from the top
        product_page = ProductPage(self.driver)
        product_page.go_to_product_item(3)


    # 7. Step: Verify that you are on the product page

        product_page =ProductPage(self.driver)
        product_page.verify_product_page()
        sleep(3)

    # 8. Step: Add to product to the cart
    # 9. Step: Verify that the product has been added to the cart
        product_page = ProductPage(self.driver)
        product_page.add_product_to_cart()
        sleep(3)

    # 10. Step: Go to the cart page
        home_page = HomePage(self.driver)
        home_page.go_to_cart()
        sleep(3)

    # 11. Step: Verify that you are on the cart page and that the correct product has been added to the cart
        product_page.verify_product_in_cart()

    #12. Step: Delete the product from the cart and verify that it has been deleted
        home_page = HomePage(self.driver)
        home_page.cart_product_delete()
        home_page.verify_product_deleted_from_cart()

    #13. Step: Return to the home page and verify that is on the home page
        home_page.amazon_homepage()
        assert home_page.is_at_amazon_homepage(), "Ana sayfaya dönülemedi!"
        print("Ana sayfaya başarıyla dönüldü ve doğrulandı.")
        sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
