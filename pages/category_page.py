from pages.base_page import BasePage


class CategoryPage(BasePage):
    def __init__(self, driver):
            super().__init__(driver)

    def search_product(self, product_name):
        self.search(product_name)

    def is_on_category_page(self):
        expected_title = "Amazon.com.tr : Samsung"
        return expected_title.__eq__(self.get_title())
