import unittest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PalindromeBrowserTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        self.driver.quit()

    def test_palindrome(self):
        self.driver.get("http://localhost:30080/check?word=MADAM")
        result = json.loads(self.driver.find_element(By.TAG_NAME, "body").text)
        self.assertTrue(result["palindrome"])

    def test_not_palindrome(self):
        self.driver.get("http://localhost:30080/check?word=HELLO")
        result = json.loads(self.driver.find_element(By.TAG_NAME, "body").text)
        self.assertFalse(result["palindrome"])

    def test_case_insensitive_palindrome(self):
        self.driver.get("http://localhost:30080/check?word=RaceCar")
        result = json.loads(self.driver.find_element(By.TAG_NAME, "body").text)
        self.assertTrue(result["palindrome"])

    def test_web_form_palindrome_check(self):
        self.driver.get("http://localhost:30080/")
        word_input = self.driver.find_element(By.ID, "word")
        check_btn = self.driver.find_element(By.ID, "checkBtn")

        word_input.clear()
        word_input.send_keys("MADAM")
        check_btn.click()

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "result"))
        )
        self.assertEqual(self.driver.find_element(By.ID, "outWord").text, "MADAM")
        self.assertEqual(
            self.driver.find_element(By.ID, "outStatus").text,
            "The given string is a Palindrome"
        )

if __name__ == "__main__":
    unittest.main()
