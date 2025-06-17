class LoginPage:
    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url
        self.username_input = "input[name='username']"
        self.password_input = "input[name='password']"
        self.login_button = "button[type='submit']"
        self.lucide_eye_icon = "svg[css='.lucide']"
        self.checkbox_remember = "button[role='checkbox']"
        self.dropdown_menu = "button[data-slot='dropdown-menu-trigger']"
        self.radix_admin = "div.font-normal"
        self.logout_button = "text=Đăng xuất"
        self.username_error = "text=Không tìm thấy:"


    def goto(self):
        self.page.goto(self.base_url)

    def login_as(self, username, password, remember=False):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        if remember:
            self.page.click(self.checkbox_remember)
        self.page.click(self.login_button)

    def login_enter_as(self, username, password, remember=False):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        if remember:
            self.page.click(self.checkbox_remember)
        self.page.press(self.password_input, "Enter")

    def login_as_invalid(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)

    def logout(self):
        self.page.click(self.dropdown_menu)
        self.page.wait_for_selector(self.radix_admin)
        self.page.click(self.logout_button)

    def delete_textbox(self):
        self.page.fill(self.username_input, "")
        self.page.fill(self.password_input, "")

