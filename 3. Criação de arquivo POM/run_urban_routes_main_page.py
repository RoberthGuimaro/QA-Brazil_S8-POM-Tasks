import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage  # Importar a classe POM


def test_personal_bike_option():
    driver = webdriver.Chrome()
    # Atualize a URL
    driver.get('https://cnt-fbc38827-ee19-4cb1-bf7e-75dea924c7e1.containerhub.tripleten-services.com?lng=pt')
    urban_routes_page = UrbanRoutesPage(driver)
    wait = WebDriverWait(driver, 10)  # Define um tempo máximo de 10 segundos
    wait.until(EC.presence_of_element_located(urban_routes_page.FROM_LOCATOR))
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
