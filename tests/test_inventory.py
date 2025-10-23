from selenium.webdriver.common.by import By
from selenium import webdriver

def test_inventory(login_in_driver):
    try:
        driver = login_in_driver

        assert driver.title == "Swag Labs"

        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No hay productos visibles en la pagina"
        productName= products[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        productPrice= products[0].find_element(By.CLASS_NAME, "inventory_item_price").text
        print(f"Primer producto visible: {productName},precio: {productPrice}")
    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise
    finally:
        driver.quit()