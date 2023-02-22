from selenium.webdriver.common.by import By

class VacanciesPageLocaotrs:
    VACANCIES_NUMBER = (By.XPATH, "/html/body/div[1]/div/div[1]/div/h3/span")
    VACANCIEC_LIST = (By.CLASS_NAME, "card.card-sm.card-no-hover")

    DEPARTMENTS_LIST = (By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div[1]/div/div[2]/div/div/button")
    DEPARTMENTS = (By.CLASS_NAME, "dropdown-item")
    LAST_DEPARTMENT = (By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div[1]/div/div[2]/div/div/div/a[9]")

    LANGUAGE_LIST = (By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div[1]/div/div[3]/div/div/button")
    LANGUAGES = (By.CLASS_NAME, "custom-control.custom-checkbox")

    CLOSE_COOKIE = (By.ID, "cookiescript_close")
