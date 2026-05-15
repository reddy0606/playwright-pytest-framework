class CheckoutPage:

    def __init__(self, page):
        self.page = page

        self.checkout_button = "#checkout"
        self.first_name = "#first-name"
        self.last_name = "#last-name"
        self.postal_code = "#postal-code"
        self.continue_button = "#continue"
        self.finish_button = "#finish"
        self.success_message = ".complete-header"

    def start_checkout(self):
        self.page.click(self.checkout_button)

    def fill_checkout_information(self, first, last, postal):

        self.page.fill(self.first_name, first)
        self.page.fill(self.last_name, last)
        self.page.fill(self.postal_code, postal)

    def continue_checkout(self):
        self.page.click(self.continue_button)

    def finish_checkout(self):
        self.page.click(self.finish_button)

    def get_success_message(self):
        return self.page.locator(self.success_message).text_content()