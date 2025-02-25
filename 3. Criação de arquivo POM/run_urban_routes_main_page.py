import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage  # Importar a classe POM


def test_personal_bike_option():
    driver = webdriver.Chrome()
    # Atualize a URL
    driver.get('https://cnt-1559d7a4-e9f5-49d2-a568-67515da435b6.containerhub.tripleten-services.com')
    urban_routes_page = UrbanRoutesPage(driver)
    urban_routes_page.enter_from_location('East 2nd Street, 601')
    urban_routes_page.enter_to_location('1300 1st St')
    urban_routes_page.click_personal_option()
    time.sleep(2)
    urban_routes_page.click_bike_icon()
    time.sleep(2)
    actual_value = urban_routes_page.get_bike_text()
    expected_value = "Bicicleta"
    assert expected_value in actual_value, f"Esperado '{expected_value}', mas obtido '{actual_value}'"
    driver.quit()
