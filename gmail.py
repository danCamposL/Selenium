# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class TestGMail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://mail.google.com/')

    def test_prueba_entrada_a_correo(self):
        email = self.driver.find_element_by_id('Email')
        email.send_keys("danielcampos586@gmail.com")
        email.send_keys(Keys.RETURN)
        time.sleep(8)
        passwd = self.driver.find_element_by_id('Passwd')
        passwd.send_keys("*********")
        passwd.send_keys(Keys.RETURN)
        time.sleep(30)
        bandeja = self.driver.find_element_by_id(':2m').click()



if __name__=='__main__':
    unittest.main()
