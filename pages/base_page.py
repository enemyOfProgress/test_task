class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        browser.maximize_window()
        self.url = url

    def open_url(self):
        self.browser.get(self.url)

    # Need to scroll dropdown list for click last elements in language
    def scroll_into_view(self):
        self.browser.execute_script("window.scrollBy(0, 50);")
