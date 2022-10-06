from selenium.webdriver.support.select import Select


class ContactusPageObjects:
    contact_us_link_dashboard_xpath = "//a[@title='Contact Us']"
    subject_heading_selection_xpath = "//select[@id='id_contact']"
    email_address_input_xpath = "//input[@id='email']"
    order_reference_input_xpath = "//input[@id='id_order']"
    file_upload_xpath = "//input[@id='fileUpload']"
    message_text_area_xpath = "//textarea[@id='message']"
    send_button_xpath = "//button[@id='submitMessage']"

    def __init__(self, driver):
        self.driver = driver

    def click_contact_us(self):
        contact_us_link = self.driver.find_element_by_xpath(self.contact_us_link_dashboard_xpath)
        contact_us_link.click()

    def select_subject_heading(self):
        select_fr = Select(self.driver.find_element_by_xpath(self.subject_heading_selection_xpath))
        select_fr.select_by_index(2)

    def enter_email_address(self, user_email_address):
        email_address_input_field = self.driver.find_element_by_xpath(self.email_address_input_xpath)
        email_address_input_field.clear()
        email_address_input_field.send_keys(user_email_address)

    def enter_order_reference(self, user_order_reference):
        order_reference_input_field = self.driver.find_element_by_xpath(self.order_reference_input_xpath)
        order_reference_input_field.clear()
        order_reference_input_field.send_keys(user_order_reference)

    def upload_file(self):
        file_path = "../files/Resume.pdf"
        file_upload_button = self.driver.find_element_by_xpath(self.file_upload_xpath)
        file_upload_button.send_keys(file_path)
        # self.driver.find_element_by_xpath('//html/body/button').click()
