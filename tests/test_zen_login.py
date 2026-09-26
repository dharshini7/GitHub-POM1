# Page Object Model - is a design pattern where we create separate python classes for each webpage u r testing
# and also keep all the locators and actions inside that class.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobject.login_page import LoginPage
from pageobject.home_page import HomePage

from selenium import webdriver

from pageobject.login_page import LoginPage
from pageobject.home_page import HomePage

def test_valid_login():

    # Open Chrome
    driver = webdriver.Chrome()


    # Open ZenClass login page
    driver.get("https://v2.zenclass.in/login")

    # Create LoginPage object
    login_page = LoginPage(driver)

    # Login with valid credentials
    login_page.login(
        "dharshiniravi777@gmail.com",
        "Prems@10"
    )

    # Create HomePage object
    home_page = HomePage(driver)

    # First close the blue popup
    home_page.close_popup_box()

    # Click profile dropdown
    home_page.click_dropdown()

    # Click Logout
    home_page.click_logout()
    print("URL after logout:",driver.current_url)
    print("TITLE after logout:",driver.title)

    # Verify that we returned to Login page
    assert "login" in driver.current_url

    # Close browser
    driver.quit()

    # ---------------------------------------------------------
    # NEGATIVE SCENARIO 1
    # Invalid username + valid password
    # ---------------------------------------------------------

def test_invalid_user():
        # Open Chrome
        driver = webdriver.Chrome()

        # Open ZenClass login page
        driver.get("https://v2.zenclass.in/login")

        # Create LoginPage object
        login_page = LoginPage(driver)

        # Enter invalid username + valid password
        login_page.login(
            "wrongemail@gmail.com",
            "Prems@10"
        )

        # Invalid login should NOT go to dashboard
        assert "dashboard" not in driver.current_url

        print("Invalid username test passed")

        # Close browser
        driver.quit()

        # ---------------------------------------------------------
        # NEGATIVE SCENARIO 2
        # Valid username + invalid password
        # ---------------------------------------------------------

def test_invalid_password():
            # Open Chrome
            driver = webdriver.Chrome()

            # Open ZenClass login page
            driver.get("https://v2.zenclass.in/login")

            # Create LoginPage object
            login_page = LoginPage(driver)

            # Enter valid username + invalid password
            login_page.login(
                "dharshiniravi777@gmail.com",
                "WrongPassword123"
            )

            # Invalid login should NOT go to dashboard
            assert "dashboard" not in driver.current_url

            print("Invalid password test passed")

            # Close browser
            driver.quit()

# ---------------------------------------------------------
# NEGATIVE SCENARIO 3
# Invalid username + invalid password
# ---------------------------------------------------------

def test_invalid_both():

    # Open Chrome
    driver = webdriver.Chrome()

    # Open ZenClass login page
    driver.get("https://v2.zenclass.in/login")

    # Create LoginPage object
    login_page = LoginPage(driver)

    # Enter invalid username + invalid password
    login_page.login(
        "wrongemail@gmail.com",
        "WrongPassword123"
    )

    # Invalid login should NOT go to dashboard
    assert "dashboard" not in driver.current_url

    print("Invalid username and password test passed")

    # Close browser
    driver.quit()

# ---------------------------------------------------------
# NEGATIVE SCENARIO 4
# Empty username + valid password
# ---------------------------------------------------------

def test_empty_username():

    # Open Chrome
    driver = webdriver.Chrome()

    # Open ZenClass login page
    driver.get("https://v2.zenclass.in/login")

    # Create LoginPage object
    login_page = LoginPage(driver)

    # Keep username empty
    # Enter valid password
    login_page.login(
        "",
        "Prems@10"
    )

    # Login should NOT go to dashboard
    assert "dashboard" not in driver.current_url

    print("Empty username test passed")

    # Close browser
    driver.quit()

# ---------------------------------------------------------
# NEGATIVE SCENARIO 5
# Valid username + empty password
# ---------------------------------------------------------

def test_empty_password():

    # Open Chrome
    driver = webdriver.Chrome()

    # Open ZenClass login page
    driver.get("https://v2.zenclass.in/login")

    # Create LoginPage object
    login_page = LoginPage(driver)

    # Enter valid username
    # Keep password empty
    login_page.login(
        "dharshiniravi777@gmail.com",
        ""
    )

    # Login should NOT go to dashboard
    assert "dashboard" not in driver.current_url

    print("Empty password test passed")

    # Close browser
    driver.quit()

# ---------------------------------------------------------
# NEGATIVE SCENARIO 5
# Valid username + empty password
# ---------------------------------------------------------

def test_both_empty():

    # Open Chrome
    driver = webdriver.Chrome()

    # Open ZenClass login page
    driver.get("https://v2.zenclass.in/login")

    # Create LoginPage object
    login_page = LoginPage(driver)

    # Enter valid username
    # Keep password empty
    login_page.login(
        "",
        ""
    )

    # Login should NOT go to dashboard
    assert "dashboard" not in driver.current_url

    print("empty username and password test passed")

    # Close browser
    driver.quit()

    # ---------------------------------------------------------
    # LOGOUT SCENARIO 1
    # Valid login → Logout → Login page
    # ---------------------------------------------------------

def test_logout():
        # Open Chrome
        driver = webdriver.Chrome()

        # Open ZenClass login page
        driver.get("https://v2.zenclass.in/login")

        # Create LoginPage object
        login_page = LoginPage(driver)

        # Login with valid credentials
        login_page.login(
            "dharshiniravi777@gmail.com",
            "Prems@10"
        )

        # Create HomePage object
        home_page = HomePage(driver)

        # Close blue popup
        home_page.close_popup_box()

        # Open profile dropdown
        home_page.click_dropdown()

        # Click Logout
        home_page.click_logout()

        # Verify that we returned to login page
        assert "login" in driver.current_url

        print("Logout test passed")

        # Close browser
        driver.quit()

        # ---------------------------------------------------------
        # LOGOUT SCENARIO 2
        # After logout → try to access dashboard
        # ---------------------------------------------------------

def test_dashboard_after_logout():
            # Open Chrome
            driver = webdriver.Chrome()

            # Open login page
            driver.get("https://v2.zenclass.in/login")

            # Create LoginPage object
            login_page = LoginPage(driver)

            # Login
            login_page.login(
                "dharshiniravi777@gmail.com",
                "Prems@10"
            )

            # Create HomePage object
            home_page = HomePage(driver)

            # Close popup
            home_page.close_popup_box()

            # Open profile dropdown
            home_page.click_dropdown()

            # Logout
            home_page.click_logout()

            # Try to access dashboard again
            driver.get("https://v2.zenclass.in/dashboard")

            # User should NOT remain on dashboard
            assert "dashboard" not in driver.current_url

            print("Dashboard is protected after logout")

            # Close browser
            driver.quit()

# ---------------------------------------------------------
# LOGOUT SCENARIO 3
# Login → Do NOT open dropdown → Logout should not be visible
# ---------------------------------------------------------

def test_logout_without_dropdown():

    # Open Chrome
    driver = webdriver.Chrome()

    # Open ZenClass login page
    driver.get("https://v2.zenclass.in/login")

    # Create LoginPage object
    login_page = LoginPage(driver)

    # Login with valid credentials
    login_page.login(
        "dharshiniravi777@gmail.com",
        "Prems@10"
    )

    # Create HomePage object
    home_page = HomePage(driver)

    # Close blue popup
    home_page.close_popup_box()

    # IMPORTANT:
    # We are NOT clicking the profile dropdown.

    # Check whether Logout is visible
    logout_elements = driver.find_elements(
        *home_page.logout
    )

    # Logout should not be visible before opening dropdown
    assert len(logout_elements) == 0

    print("Logout is not available before opening dropdown")

    # Close browser
    driver.quit()







