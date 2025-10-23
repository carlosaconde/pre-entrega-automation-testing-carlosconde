from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_cart(login_in_driver):
    try:
        driver = login_in_driver

       

       
        driver.find_element(By.XPATH,"//button[contains(@data-test,'add-to-cart')]").click()

        
        badge = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge")))
        
        assert badge.text == "1", "El carrito no muestra el numero correcto de productos"
    
        driver.find_element(By.ID, "shopping_cart_container").click()
        assert "/cart.html" in driver.current_url, "no se redirige al carrito"
        
        product_in_cart = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME,"cart_item")))
    
    except Exception as e:
        print(f"Error en test_cart: {e}")
        raise
    finally:
        driver.quit()