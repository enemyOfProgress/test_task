from selenium import webdriver
from .base_page import BasePage
from .locators import VacanciesPageLocaotrs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class VacanciesPage(BasePage):
    # It's not necessary, but cookies window blocks some elements
    def close_cookies(self):
        ccw = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, "cookiescript_close")))
        ccw.click()

    def click_all_departments_list(self):
        departments = self.browser.find_element(*VacanciesPageLocaotrs.DEPARTMENTS_LIST)
        departments.click()

    def select_department(self, dep):
        rd_dep = self.browser.find_elements(*VacanciesPageLocaotrs.DEPARTMENTS)
        for i in rd_dep:
            if dep in i.text:
                i.click()

    def click_languages_list(self):
        lan_list = self.browser.find_element(*VacanciesPageLocaotrs.LANGUAGE_LIST)
        lan_list.click()

    # Select language from dropdown list
    def select_language(self, lang):
        languages = self.browser.find_elements(*VacanciesPageLocaotrs.LANGUAGES)
        for i in languages:
            if i.text == lang:
                i.click()

    def get_numbers_open_vacancies(self):
        vacancies_number = self.browser.find_element(*VacanciesPageLocaotrs.VACANCIES_NUMBER)
        return vacancies_number.text

    def get_number_of_vacancies_from_lsit(self):
        vn = self.browser.find_elements(*VacanciesPageLocaotrs.VACANCIEC_LIST)
        return len(vn)

    def compare_result(self, open_vacancies):
        vacancies_in_list = self.get_number_of_vacancies_from_lsit()
        assert open_vacancies == vacancies_in_list, f"Quantity does not match: open vacancies is {open_vacancies}, " \
                                                    f"but actual vacancies in list is {vacancies_in_list}"
