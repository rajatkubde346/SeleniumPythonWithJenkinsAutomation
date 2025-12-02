import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def _get_driver():
    """Common driver setup: headless Chrome (Jenkins friendly)."""
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver


def test_demoqa_textbox_and_checkbox():
    driver = _get_driver()

    try:
        # --- Text Box page ---
        driver.get("https://demoqa.com/text-box")

        wait = WebDriverWait(driver, 10)

        wait.until(EC.visibility_of_element_located((By.ID, "userName"))).send_keys("rajat")
        driver.find_element(By.ID, "userEmail").send_keys("rajatkubde346@gmail.com")
        driver.find_element(By.ID, "currentAddress").send_keys("Pune")
        driver.find_element(By.ID, "permanentAddress").send_keys("Pune")

        # Normal click ki jagah JS click, kyunki ads iframe click ko block kar sakte hain
        submit_btn = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        driver.execute_script("arguments[0].click();", submit_btn)

        time.sleep(2)

        # Basic assertion – output box me data aa gaya?
        output_text = driver.find_element(By.ID, "output").text.lower()
        assert "rajat" in output_text
        assert "pune" in output_text

        # --- Checkbox page ---
        driver.get("https://demoqa.com/checkbox")
        time.sleep(2)

        check1 = driver.find_element(By.ID, "item-1")
        check1.click()
        time.sleep(2)

        # First svg checkbox expand icon click
        check = driver.find_element(By.XPATH, "//*[local-name()='svg']")
        check.click()
        time.sleep(2)

        # Agar yahan tak bina error ke aa gaye -> test PASS
        assert True

    finally:
        driver.quit()


def test_parabank_register():
    driver = _get_driver()

    try:
        driver.get("https://parabank.parasoft.com/parabank/register.htm")

        wait = WebDriverWait(driver, 10)

        first = wait.until(
            EC.visibility_of_element_located((By.ID, "customer.firstName"))
        )
        first.send_keys("rajat")

        last = driver.find_element(By.ID, "customer.lastName")
        last.send_keys("kubde")

        add = driver.find_element(By.ID, "customer.address.street")
        add.send_keys("pune")

        driver.find_element(By.ID, "customer.address.city").send_keys("Pune")
        driver.find_element(By.ID, "customer.address.state").send_keys("Maharashtra")
        driver.find_element(By.ID, "customer.address.zipCode").send_keys("411045")
        driver.find_element(By.ID, "customer.ssn").send_keys("1237475")

        # username ideally unique hona chahiye
        driver.find_element(By.ID, "customer.username").send_keys("rajat1234")
        driver.find_element(By.ID, "customer.password").send_keys("1234")
        driver.find_element(By.ID, "repeatedPassword").send_keys("1234")

        register_btn = driver.find_element(
            By.CSS_SELECTOR, "input[value='Register']"
        )
        register_btn.click()

        time.sleep(3)

        driver.find_element(By.NAME, "username").send_keys("rajat1234")
        driver.find_element(By.NAME, "password").send_keys("1234")
        driver.find_element(By.TAG_NAME, "input").click()
        wait = WebDriverWait(driver, 10)





    finally:
        driver.quit()
