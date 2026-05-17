# class LoginPage:
#     def __init__(self, page):
#         self.page = page

#         self.username_input = "#user-name"
#         self.password_input = "#password"
#         self.login_button = "#login-button"
#         self.error_message = "[data-test='error']"

#     def open_login_page(self):
#         self.page.goto("https://www.saucedemo.com")

#     def login(self, username, password):
#         self.page.fill(self.username_input, username)
#         self.page.fill(self.password_input, password)
#         self.page.click(self.login_button)

#     def get_error_message(self):
#         return self.page.locator(self.error_message).text_content()



#     '''
#     This is:
# ✅ reusable
# ✅ maintainable
# ✅ scalable

# That’s the whole point of POM.
# '''
















class LoginPage:
    def __init__(self, page):
        self.page = page

        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"

    async def open_login_page(self):
        await self.page.goto("https://www.saucedemo.com")

    async def login(self, username, password):
        await self.page.fill(self.username_input, username)
        await self.page.fill(self.password_input, password)
        await self.page.click(self.login_button)

    async def get_error_message(self):
        return await self.page.locator(self.error_message).text_content()
