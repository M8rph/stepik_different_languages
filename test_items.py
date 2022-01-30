import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_language(browser):
    browser.get(link)
    time.sleep(5)
    assert browser.find_elements_by_class_name("btn-add-to-basket"), "Button not found"
