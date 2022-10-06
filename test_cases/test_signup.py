from page_objects.signup import SignUp
from utilities.read_properties import ReadConfig
import time


class Test_001_signup:
    baseUrl = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    first_name = ReadConfig.get_first_name()
    last_name = ReadConfig.get_last_name()
    password = ReadConfig.get_password()
    address_first_name = ReadConfig.get_address_first_name()
    address_last_name = ReadConfig.get_address_last_name()
    company = ReadConfig.get_company()
    address = ReadConfig.get_address()
    city = ReadConfig.get_city()
    postal_code = ReadConfig.get_postal_code()
    mobile_phone = ReadConfig.get_mobile()
    address_reference = ReadConfig.get_address_reference()
    day_DOB = ReadConfig.get_day_DOB()
    month_DOB = ReadConfig.get_month_DOB()
    year_DOB = ReadConfig.get_year_DOB()
    state = ReadConfig.get_state()

    def test_signup(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.su = SignUp(self.driver)
        self.su.clickSigninDashboard()
        time.sleep(2)
        self.su.setUserEmail(self.email)
        self.su.clickCreateAccount()
        time.sleep(5)
        self.su.setFirstName(self.first_name)
        self.su.setLastName(self.last_name)
        self.su.setDOBDay(self.day_DOB)
        self.su.setDOBMonth(self.month_DOB)
        self.su.setDOBYear(self.year_DOB)
        self.su.setAddressFirstName(self.address_first_name)
        self.su.setAddressLastName(self.address_last_name)
        self.su.setCompany(self.company)
        self.su.setAddress(self.address)
        self.su.setCity(self.city)
        self.su.setPostalCode(self.postal_code)
        self.su.setMobilePhone(self.mobile_phone)
        self.su.setAddressReference(self.address_reference)
        self.su.setPassword(self.password)
        self.su.setState(self.state)
        self.su.clickRegister()













