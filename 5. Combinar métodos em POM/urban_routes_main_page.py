import time

from selenium.webdriver.common.by import By


# Definição da classe da página, dos localizadores e do metodo na classe
class UrbanRoutesPage:
    # Localizadores como atributos de classe
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    PERSONAL_OPTION_LOCATOR = (By.XPATH, '//div[text()="Personal"]')
    CARSHARING_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/drive.05beabd2.svg"]')
    #CARSHARING_ICON_LOCATOR = (By.XPATH, '(//img[@src="/static/media/car.8a2b1ff5.svg"])[2]')
    BOOK_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button round"]')
    CAMPING_LOCATOR = (By.XPATH, '//div[contains(text(),"Camping")]')
    AUDI_TEXT_LOCATOR = (By.XPATH, '//div[contains(text(),"Audi A3 Sedã")]')
    ADD_DRIVER_LICENSE_LOCATOR = (By.XPATH, '(//div[contains(text(),"Adicionar carteira de motorista")])[2]')
    FIRST_NAME_LOCATOR = (By.ID, 'firstName')
    LAST_NAME_LOCATOR = (By.ID, 'lastName')
    DATE_OF_BIRTH_LOCATOR = (By.ID, 'birthDate')
    NUMBER_LOCATOR = (By.ID, 'number')
    ADD_BUTTON_LOCATOR = (By.XPATH, '//form/div[2]/button[1]')
    ADD_DRIVER_LICENSE_TITLE_LOCATOR = (By.XPATH, '//div[contains(text(),"Adicionar carteira de motorista")]')
    VERIFICATION_TEXT_LOCATOR = (By.XPATH, '//div[contains(text(),"Obrigado!")]')

    def __init__(self, driver):
        self.driver = driver  # Inicializar o driver

    def choose_camping_car(self, from_text, to_text):
        # Inserir De
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)
        self.driver.find_element(*self.PERSONAL_OPTION_LOCATOR).click()
        time.sleep(1)
        self.driver.find_element(*self.CARSHARING_ICON_LOCATOR).click()
        self.driver.find_element(*self.BOOK_BUTTON_LOCATOR).click()
        time.sleep(1)
        self.driver.find_element(*self.CAMPING_LOCATOR).click()

    def get_audi_text(self):
        #Retornar o texto "Audi"
        return self.driver.find_element(*self.AUDI_TEXT_LOCATOR).text

    # Etapa para clicar em "add_driver_license"; para digitar "first_name", "last_name", "date_of_birth", "number"; e
    # para clicar em "title" e "add_button"
    def adding_driver_license(self, first_name, last_name, date_of_birth, number):
        self.driver.find_element(*self.ADD_DRIVER_LICENSE_LOCATOR).click()
        self.driver.find_element(*self.FIRST_NAME_LOCATOR).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_LOCATOR).send_keys(last_name)
        self.driver.find_element(*self.DATE_OF_BIRTH_LOCATOR).send_keys(date_of_birth)
        self.driver.find_element(*self.NUMBER_LOCATOR).send_keys(number)
        self.driver.find_element(*self.ADD_DRIVER_LICENSE_TITLE_LOCATOR).click()
        self.driver.find_element(*self.ADD_BUTTON_LOCATOR).click()

    def get_verification_text(self):
        #Retornar o texto de verificação
        return self.driver.find_element(*self.VERIFICATION_TEXT_LOCATOR).text