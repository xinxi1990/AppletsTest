#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018/07/20
@author: xinxi
测试点:页面基类
"""

import unittest
from config import *
from fastAutoTest.utils.logger import Log
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from fastAutoTest.core.h5.h5Engine import H5Driver
from driver import AppiumDriver
log = Log()
log.setLevel(Log.INFO)
logger = log.getLogger()



class Base(unittest.TestCase):



    def setUp(self):
        '''
        初始化操作,每个方法执行一次
        :return:
        '''

        self.appium_driver = AppiumDriver()
        self.driver = self.appium_driver.start_appium()
        self.driver.implicitly_wait(15)
        logger.info("启动app中.....")


    # def test_lanuch(self):
    #     '''
    #     登录测试
    #     :return:
    #     '''
    #     time.sleep(5)
    #     flag = True
    #     while flag:
    #         if self.driver.find_elements(By.XPATH, allow):
    #             self.driver.find_element(By.XPATH, allow).click()
    #             logger.info('点击授权')
    #         elif self.driver.find_elements(By.XPATH, allow_en):
    #             self.driver.find_element(By.XPATH, allow_en).click()
    #             logger.info('点击授权')
    #         else:
    #             flag = False
    #             break
    #     self.driver.find_element(By.XPATH, login_btn).click()
    #     logger.info('点击登录')
    #     self.driver.find_element(By.XPATH, weixin_btn).click()
    #     logger.info('点击使用微信登录')


    def test_app(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, serach_btn).click()
        logger.info('点击搜索')
        self.driver.find_element_by_id(serach_id).send_keys(app_name)
        logger.info('搜索得到')
        self.driver.find_element_by_id(app_icon).click()
        logger.info('点击小程序')

        time.sleep(5)

        h5Driver = H5Driver()
        h5Driver.initDriver()
        h5Driver.clickElementByXpath('/html/body/div/div[2]/div[2]/div[1]/a')
        h5Driver.clickFirstElementByText('白内障')
        h5Driver.returnLastPage()
        h5Driver.returnLastPage()
        print(h5Driver.getElementTextByXpath('/html/body/div[1]/div/div[3]/p'))
        h5Driver.close()






if __name__ == '__main__':
    unittest.main()