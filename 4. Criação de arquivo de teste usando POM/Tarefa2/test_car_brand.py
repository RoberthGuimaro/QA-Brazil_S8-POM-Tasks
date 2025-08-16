import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage  # Importar a classe POM
import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage

def test_carsharing_personal_camping_option():
    driver = webdriver.Chrome()
    # Abra o aplicativo e atualize a URL após iniciar o servidor
    driver.get('https://cnt-55e7d79b-436e-464b-a42a-d4dbd0f69a11.containerhub.tripleten-services.com?lng=pt')

    # Crie uma instância da classe de página
    urban_routes_page = UrbanRoutesPage(driver)
    time.sleep(3)

    # Etapa 1: Insira o endereço "De"
    urban_routes_page.enter_from_location("East 2nd Street, 601")

    # Etapa 2: Insira o endereço "Para"
    urban_routes_page.enter_to_location("1300, 1st St")

    # Etapa 3: Escolha "Personal"
    urban_routes_page.click_personal_option()
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 4: Clique em "Carsharing"
    urban_routes_page.click_carsharing_icon()
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 5: Clique em "Reservar"
    urban_routes_page.click_book_button()
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 6: Escolha "Camping"
    urban_routes_page.click_camping()
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 7: Verifique se o texto exibe "Audi A3 Sedã"
    actual_value = urban_routes_page.get_audi_text()
    expected_value = "Audi"
    assert expected_value in actual_value, f"Expected: {expected_value}, Actual: {actual_value}"
    driver.quit()
