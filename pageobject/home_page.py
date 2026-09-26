from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self, driver):
        self.driver = driver

        # Explicit wait
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.close_popup = (By.XPATH, "//button[@class='custom-close-button']")
        self.dropdown = (By.ID, "profile-click-icon")
        self.logout = (By.XPATH, "//div[text()='Log out']")

    def close_popup_box(self):

        # Wait until popup close button is clickable
        self.wait.until(
            EC.element_to_be_clickable(self.close_popup)
        ).click()

    def click_dropdown(self):

        # Wait until profile dropdown is clickable
        self.wait.until(
            EC.element_to_be_clickable(self.dropdown)
        ).click()

    def click_logout(self):

            logout_button = self.wait.until(
                EC.element_to_be_clickable(self.logout)
            )

            logout_button.click()

            # Wait for URL to change from dashboard
            self.wait.until(
                lambda driver: "dashboard" not in driver.current_url
            )
