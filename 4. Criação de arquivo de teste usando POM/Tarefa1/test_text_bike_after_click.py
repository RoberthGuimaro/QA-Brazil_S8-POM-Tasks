import time
from unittest import expectedFailure

from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage # importar a classe pom

def test_personal_bike_option():
    # Abra o aplicativo Urban Routes e atualize a URL após iniciar o servidor
    driver = webdriver.Chrome()
    driver.get("https://cnt-a0b46c6d-8695-4f69-b41a-f98011b73853.containerhub.tripleten-services.com?lng=pt")

    # Crie uma instância da classe da página
    # urban_routes_page é o nome da instância criada
    urban_routes_page = UrbanRoutesPage(driver)
    time.sleep(2)  # Adiciona atraso para visibilidade

    # Use métodos POM para executar ações na pagina
    # Preencha o campo "De"
    urban_routes_page.enter_from_location('East 2nd Street, 601')

    # Preencha o campo "Para"
    urban_routes_page.enter_to_location('1300 1st St')

    # Clique no botão "Personal"
    urban_routes_page.click_personal_option()
    time.sleep(2) # Adiciona atraso para visibilidade

    # Clique no botão "Scooter"
    urban_routes_page.click_bike_icon()
    time.sleep(2)

    # Verifique se o texto "Scooter" é exibido
    actual_value = urban_routes_page.get_bike_text()
    expected_value = "Bicicleta"
    assert expected_value in actual_value, f"Expected: {expected_value}, Actual: {actual_value}"
    driver.quit()

