from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class DriverAPI:

    def __init__(self, driver):
        self.driver = driver

    def get_link(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def click_on(self, element_method, method_used=By.CSS_SELECTOR, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((method_used, element_method)))
        element.click()
        return element

    def send_data(self, element_method, data, method_used=By.CSS_SELECTOR, timeout=10):
        element = self.find(element_method, method_used, timeout)
        element.send_keys(data)
        return element

    def find(self, element_method, method_used=By.CSS_SELECTOR, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((method_used, element_method)))

            return element
        except:
            return None

    def switch_iframe(self, iframe_id):
        self.driver.switch_to.frame(iframe_id)

    def switch_default_content(self):
        self.driver.switch_to.default_content()

    def get_text(self, element_method, method_used=By.CSS_SELECTOR, timeout=10):
        content = self.find(element_method, method_used, timeout)
        return content.text

    def is_present_on_page(self, element_method, method_used=By.CSS_SELECTOR, timeout=10):
        try:
            self.find(element_method, method_used, timeout)
            return True
        except:
            return False

    def get_current_url(self):
        return self.driver.current_url

    def quit(self):
        self.driver.quit()

    def find_list_element(self, element_method, method_used=By.CSS_SELECTOR, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((method_used, element_method)))
            elements = self.driver.find_elements(by=By.CSS_SELECTOR, value=element_method)
            return elements
        except:
            return None

    def relocate_to_url(self, url, element_method, method_used=By.CSS_SELECTOR, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located((method_used, element_method)))
        self.driver.get(url)

    def take_screenshot(self, scenario_name, step_name):
        file_name = f"{scenario_name}_{step_name}_{round(time.time() * 1000)}.png"
        screenshot_directory = "/Users/admin/PycharmProjects/Python-Exercises/behaveproject/screenshot"
                                #"../behaveproject/screenshot"
        destination_file = screenshot_directory + file_name

        try:
            self.driver.save_screenshot(destination_file)
            print("Screenshot saved to directory --> :: " + destination_file)
        except NotADirectoryError:
            print("Failed to save screenshot")
