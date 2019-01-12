class DashboardPage():
    def __init__(self, driver):
        self.driver = driver
        self.update_your_email_add_link_text = "Update your email address"
        self.recharge_voucher_link_text = "Recharge voucher"
        self.add_data_link_text = "Add Data"

    def verify_element_on_dashboard(self):
        self.driver.find_element_by_link_text(self.update_your_email_add_link_text).is_displayed()
        self.driver.find_element_by_link_text(self.recharge_voucher_link_text).is_displayed()
        self.driver.find_element_by_link_text(self.add_data_link_text).is_displayed()