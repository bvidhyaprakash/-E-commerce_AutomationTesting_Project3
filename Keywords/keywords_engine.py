import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class KeywordEngine:
    def __init__(self, driver, yaml_file):
        self.driver = driver
        self.yaml_file = yaml_file

    def parse_locator(self, locator):
        strategy, value = locator.split(":", 1)
        strategies = {
            "id": By.ID,
            "name": By.NAME,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR,
            "class": By.CLASS_NAME,
        }
        return strategies[strategy], value

    def find_element(self, by, loc, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, loc)))

    def run_steps(self):
        with open(self.yaml_file, "r") as f:
            steps = yaml.safe_load(f)["steps"]

        for step in steps:
            action = step["action"]
            locator = step.get("locator")
            value = step.get("value")

            if locator:
                by, loc = self.parse_locator(locator)

            print(f"[STEP] {action.upper()} — locator={locator} value={value}")

            if action == "open_url":
                self.driver.get(value)

            elif action == "enter_text":
                elem = self.find_element(by, loc)
                elem.clear()
                elem.send_keys(value)

            elif action == "click":
                elem = self.find_element(by, loc)
                elem.click()

            elif action == "assert_text":
                elems = self.driver.find_elements(by, loc)
                texts = [el.text for el in elems]
                if isinstance(value, list):
                    for v in value:
                        assert v in texts, f"Expected '{v}' in {texts}"
                else:
                    assert value in texts, f"Expected '{value}' in {texts}"
            else:
                raise ValueError(f"Unknown action '{action}'")
