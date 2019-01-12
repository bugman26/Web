from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from SampleProject.Pages.loginPage import LoginPage
from SampleProject.Pages.servicePage import ServicePage
from SampleProject.Pages.dashboardPage import DashboardPage
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/U002EMD/PycharmProjects/Web/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_login_valid(self):
        driver = self.driver
        driver.get("https://www.amaysim.com.au/")
        login = LoginPage(driver)
        login.click_login_btn()
        login.enter_username("0468340754")
        login.enter_password("theHoff34")
        login.click_login()
        service = ServicePage(driver)
        service.click_mobile_num1()
        dashboard = DashboardPage(driver)
        dashboard.verify_element_on_dashboard()
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/U002EMD/PycharmProjects/Web/SampleProject/Reports"))




