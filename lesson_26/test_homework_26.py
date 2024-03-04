import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from lesson_26_pt2 import *

TRACKING_ID = 59001082084790


def test_search_by_tracking_id():
    driver = get_url('https://tracking.novaposhta.ua/#/uk/')
    search_input_xpath = '//*[@id="en"]'
    input_element = expected_field(driver, search_input_xpath)
    input_element.send_keys(TRACKING_ID)
    search_btn_xpath = '//*[@id="np-number-input-desktop-btn-search-en"]'
    search_btn = expected_field(driver, search_btn_xpath)
    search_btn.click()

    info_button_xpath = '//*[@id="chat"]/div[2]/button'
    info_button_element = expected_field(driver, info_button_xpath)
    info_button_element.click()

    status_class_name = 'header__status-text'
    status_element = find_element_by_class_name(driver, status_class_name)
    assert status_element.text == 'Отримана'
    driver.quit()


def test_search_with_invalid_tracking_id():
    driver = get_url('https://tracking.novaposhta.ua/#/uk/')
    search_input_xpath = '//*[@id="en"]'
    input_element = expected_field(driver, search_input_xpath)
    input_element.send_keys('12345678912')
    search_btn_xpath = '//*[@id="np-number-input-desktop-btn-search-en"]'
    search_btn = expected_field(driver, search_btn_xpath)
    search_btn.click()

    status_class_name = 'header__status-text'
    status_element = find_element_by_class_name(driver, status_class_name)
    assert status_element.text == 'Видалено'
    driver.quit()
