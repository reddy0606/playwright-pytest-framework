class InventoryPage:

    def __init__(self, page):
        self.page = page

        self.add_to_cart_button = "#add-to-cart-sauce-labs-backpack"
        self.remove_button = "#remove-sauce-labs-backpack"
        self.cart_badge = ".shopping_cart_badge"
        self.cart_icon = ".shopping_cart_link"

    def add_item_to_cart(self):
        self.page.click(self.add_to_cart_button)

    def remove_item_from_cart(self):
        self.page.click(self.remove_button)

    def get_cart_count(self):
        return self.page.locator(self.cart_badge).text_content()

    def open_cart(self):
        self.page.click(self.cart_icon)