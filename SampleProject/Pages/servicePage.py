class ServicePage():
    def __init__(self, driver):
        self.driver = driver
        self.mobile_card1_xpath = "//a[@data-automation-id='mobile-card'][1]"


    def click_mobile_num1(self):
        self.driver.find_element_by_xpath(self.mobile_card1_xpath).click()
