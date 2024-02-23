from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver


def firefox():
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    return driver


def chrome():
    options = ChromeOptions()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options)
    return driver


if __name__ == "__main__":
    import pathlib
    # driver = firefox()
    driver = chrome()
    driver.get("http://google.com")
    screen_path = pathlib.Path(__file__).parent / "screenshot.png"
    driver.save_screenshot(f'{screen_path}')
    driver.close()
