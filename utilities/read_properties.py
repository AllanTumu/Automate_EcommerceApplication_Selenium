import configparser

config = configparser.RawConfigParser()
config.read("../Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('Common required information', 'baseURL')
        return url

    @staticmethod
    def get_page_title():
        page_title = config.get('Common required information', 'page_title')
        return page_title
