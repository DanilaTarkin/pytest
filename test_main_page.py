from pages.main_page import MainPage
from pages.locators import MainPageLocators
from pages.locators import ProductPageLocators
from pages.locators import CartPageLocators
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import pytest

@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    link = MainPageLocators.MAIN_PAGE_LINK
    
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес	
    page = MainPage(browser, link)

    # открываем нужную страницу
    page.open()
	# выполняем метод страницы: ищем переход на страницу логина
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = MainPageLocators.MAIN_PAGE_LINK

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес	
    page = MainPage(browser, link)
	# открываем нужную страницу
    page.open()
	# выполняем метод страницы: переходим на страницу логина
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = MainPageLocators.MAIN_PAGE_LINK

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес	
    page = MainPage(browser, link)
	# открываем нужную страницу
    page.open()
    page.go_to_basket_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.cart_should_be_empty()

def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = ProductPageLocators.PRODUCT_PAGE_LINK

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес	
    page = MainPage(browser, link)
	# открываем нужную страницу
    page.open()
    page.go_to_basket_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.cart_should_be_empty()