from selenium.webdriver.common.by import By


class LoginLocators():
    # Login page object
    click_login_icon = (By.XPATH, "//img[@src='/Resources/images/login.png']")
    click_login_button = (By.XPATH, "//a[@id='loginLink']")
    textbox_username_xpath = (By.XPATH, "//input[@id='Email']")
    textbox_password1_xpath = (By.XPATH, "(//input[@type=\"text\"])[2]")
    textbox_password2_xpath = (By.XPATH, "//input[@id=\"Password\"]")
    button_login_xpath = (By.XPATH, "//input[@value='লগইন করুন']")


class LogoutLocator():
    # home page object
    button_logout_xpath = (By.XPATH, "//img[@src='/Resources/images/login.png']")
    logout_link_xpath = (By.XPATH, "//a[@id='logOut']")


class TopNavBarLocator():
    click_homepage = (By.XPATH, "//a[contains(text(),'হোম')]")
    click_subjectPage = (By.XPATH, "//a[@href='/Category/All']")
    click_writer = (By.XPATH, '/html[1]/body[1]/div[2]/section[1]/section[1]/section[1]/section[2]/ul[1]/li[3]/a[1]')
    click_allbooks = (By.XPATH, "//ul[@class='top-nav']//a[contains(text(),'সব বই')]")
    send_searchopt = (By.XPATH, "//input[@id='search-text']")
    click_searchopt = (By.XPATH, "//button[@id='topSearch']")
    click_book = (By.XPATH, "//span[@class='title']//a[contains(text(),'ব্লাড পেইন্টিং')]")
    click_addtocart = (By.XPATH, "//a[contains(text(),'+ কার্ট-এ যোগ করুন')]")
    click_cart = (By.XPATH, "//span[@id='cart-count']")
    click_deletecart = (By.XPATH, "//i[@class='icon-trash']")


class BottomNavBarLocator():
    click_facebookicon = (By.XPATH, "//a[@id='social_facebook']")
    click_twittericon = (By.XPATH, "//a[@id='social_twitter']")
    click_youtubeicon = (By.XPATH, "//a[@id='social_youtube']")
    click_playstoreicon = (By.XPATH, "//img[@alt='play']")
    click_appstoreicon = (By.XPATH, "//img[@alt='appstore']")
    click_helpbutton = (By.XPATH, "//a[contains(text(),'সাহায্য')]")
