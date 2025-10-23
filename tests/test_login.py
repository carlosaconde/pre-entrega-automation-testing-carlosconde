from selenium.webdriver.common.by import By
from selenium import webdriver


def test_login_val(login_in_driver):

    try:
        driver = login_in_driver
        assert "/inventory.html" in driver.current_url, "no se redirige al inventario"

    except Exception as e:
        print(f"Error en test login: {e}")  
        raise
    finally:
        driver.quit()  