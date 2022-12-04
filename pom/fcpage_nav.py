from base.seleniumbase import SeleniumBase

class facebookPageNav(SeleniumBase):
    def __int__(self, driver):
        super().__init__(driver)
        self.driver = driver
