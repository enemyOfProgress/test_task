import pytest
from selenium import webdriver
from .pages.base_page import BasePage
from .pages.vacancies_page import VacanciesPage
from .pages.locators import VacanciesPageLocaotrs


class TestVacanciesPage:
    # You can add to language or department, or open vacancies another values
    @pytest.mark.parametrize('language', ["English"])
    @pytest.mark.parametrize('department', ["Research & Development"])
    @pytest.mark.parametrize('op', [""])
    @pytest.mark.xfail(reason="Need to fix quantity of 'Vanacies open'")
    def test_vanacies_in_list_compare_open_vacancies(self, browser, language, department, op):
        vp = open_browser_by_url(browser=browser, page=VacanciesPage)
        if op is "":
            op = vp.get_numbers_open_vacancies()
        vp.close_cookies()
        # Scroll need, 'cause the German language was hidden due to the pop-up "Chrome is being cnotrolled..."
        vp.scroll_into_view()
        vp.click_all_departments_list()
        vp.select_department(department)
        vp.click_languages_list()
        vp.select_language(language)
        vp.click_languages_list()
        vp.compare_result(op)


def open_browser_by_url(browser, page):
    url = "https://cz.careers.veeam.com/vacancies"
    browser = page(browser, url)
    browser.open_url()
    return browser
