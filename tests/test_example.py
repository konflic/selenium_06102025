def test_main_title(browser):
    browser.get(f"http://{browser.base_url}:8081/")
    assert browser.title == "PrestaShop"


def test_contacts_title(browser):
    browser.get(f"http://{browser.base_url}:8081/contact-us")
    assert browser.title == "Contact us"
