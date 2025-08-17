from operator import contains

from selenium.webdriver.common.by import By


# Definição da classe da página, dos localizadores e do método na classe
class UrbanRoutesPage:
    # Localizadores como atributos de classe
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    PERSONAL_OPTION_LOCATOR = (By.XPATH, '//div[text()="Personal"]')
    CARSHARING_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/drive.05beabd2.svg"]')
#   CARSHARING_ICON_LOCATOR = (By.XPATH, '(//img[@src="/static/media/car.8a2b1ff5.svg"])[2]')
    BOOK_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button round"]')
    CAMPING_LOCATOR = (By.XPATH, '//img[@src="/static/media/camping.075c6361.svg"]')
    ADD_DRIVER_LICENSE_LOCATOR = (By.XPATH, '//div[@class="np-text"]')
    FIRST_NAME_LOCATOR = (By.ID, 'firstName')
    LAST_NAME_LOCATOR = (By.ID, 'lastName')
    DATE_OF_BIRTH_LOCATOR = (By.ID, 'birthDate')
    NUMBER_LOCATOR = (By.ID, 'number')
    ADD_A_DRIVER_LICENCE_TITLE_LOCATOR = (By.XPATH, '//div[contains(text(),"Adicionar carteira de motorista")]')
    ADD_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button full" and contains(text(), "Adicionar")]')
    VERIFICATION_TEXT_LOCATOR = (By.XPATH, '//div[@class="head" and contains(text(), "Obrigado")]')

    def __init__(self, driver):
        self.driver = driver  # Inicializar o driver

    def enter_from_location(self, from_text):
        # Inserir De
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        # Inserir Para
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def click_personal_option(self):
        # Clicar Personal
        self.driver.find_element(*self.PERSONAL_OPTION_LOCATOR).click()

    def click_carsharing_icon(self):
        # Clique no ícone Carsharing
        self.driver.find_element(*self.CARSHARING_ICON_LOCATOR).click()

    def click_book_button(self):
        # Clique no botão Reservar
        self.driver.find_element(*self.BOOK_BUTTON_LOCATOR).click()

    def click_camping(self):
        # Clique em Camping
        self.driver.find_element(*self.CAMPING_LOCATOR).click()

    def click_add_driver_license(self):
        # Clicar em Adicionar carteira de motorista
        self.driver.find_element(*self.ADD_DRIVER_LICENSE_LOCATOR).click()

    def enter_first_name(self, first_name):
        # Digitar Nome
        self.driver.find_element(*self.FIRST_NAME_LOCATOR).send_keys(first_name)

    def enter_last_name(self, last_name):
        # Digitar Sobrenome
        self.driver.find_element(*self.LAST_NAME_LOCATOR).send_keys(last_name)

    def enter_date_of_birth(self, date_of_birth):
        # Inserir Data de nascimento
        self.driver.find_element(*self.DATE_OF_BIRTH_LOCATOR).send_keys(date_of_birth)

    def enter_number(self, number):
        # Digitar Número
        self.driver.find_element(*self.NUMBER_LOCATOR).send_keys(number)

    def click_title(self):
        # Clicar Adicionar um título de carteira de motorista
        self.driver.find_element(*self.ADD_A_DRIVER_LICENCE_TITLE_LOCATOR).click()

    def click_add_button(self):
        # Clicar no botão Adicionar
        self.driver.find_element(*self.ADD_BUTTON_LOCATOR).click()

    def get_verification_text(self):
        # Retornar o texto de verificação
        return self.driver.find_element(*self.VERIFICATION_TEXT_LOCATOR).text