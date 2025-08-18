from selenium import webdriver
import time
from urban_routes_main_page import UrbanRoutesPage

# Crie uma classe para ambos os testes
class TestUrbanRoutes:

    # Inicialize o driver do Chrome uma vez para a classe
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_personal_bike_option(self):
        self.driver.get('https://cnt-e4c873bc-3f3c-4791-a7dd-a0fa904f3918.containerhub.tripleten-services.com?lng=pt')
        urban_routes_page = UrbanRoutesPage(self.driver)
        time.sleep(2)
        urban_routes_page.enter_locations("East 2nd Street, 601", "1300 1St st")
        time.sleep(2)
        urban_routes_page.click_personal_option()
        urban_routes_page.click_bike_icon()
        expected_value = "Bicicleta"
        actual_value = urban_routes_page.get_bike_text()
        assert expected_value in actual_value, f'Expected: {expected_value}, Actual: {actual_value}'

    def test_duration_personal_bike_option(self):
        self.driver.get('https://cnt-e4c873bc-3f3c-4791-a7dd-a0fa904f3918.containerhub.tripleten-services.com?lng=pt')
        urban_routes_page = UrbanRoutesPage(self.driver)
        time.sleep(2)
        urban_routes_page.enter_locations("East 2nd Street, 601", "1300 1St st")
        time.sleep(2)
        urban_routes_page.click_personal_option()
        urban_routes_page.click_bike_icon()
        expected_value = "Duração"
        actual_value = urban_routes_page.get_duration_text()
        assert expected_value in actual_value, f'Expected: {expected_value}, Actual: {actual_value}'

    # Feche o navegador depois que todos os testes forem feitos
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()