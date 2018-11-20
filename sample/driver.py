#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time,os,sys,subprocess,json
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from fastAutoTest.utils.logger import Log
from config import *
log = Log()
log.setLevel(Log.INFO)
logger = log.getLogger()


class AppiumDriver(object):
    driver = None
    def  __init__(self):
        self.device = devices_name
        self.url = "127.0.0.1"
        self.port = "4725"
        self.package_name = package_name
        self.lanuch_activity = lanuch_activity

    def init_capability(self):
        '''
        启动配置文件
        :return:
        '''
        desired_caps = {
            "platformName": "Android",
            "appPackage": self.package_name,
            "platformVersion ": "7.0",
            "appActivity": self.lanuch_activity,
            "autoLaunch": "true",
            "unicodeKeyboard": "true", # 使用appium的输入法，支持中文并隐藏键盘
            "resetKeyboard": "true", # 重置键盘
            "newCommandTimeout": 120, # 设置driver超时时间
            #"automationName": "uiautomator2"
            "noReset": True

        }
        desired_caps["deviceName"] = self.device
        desired_caps.update()
        AppiumDriver.driver = webdriver.Remote('http://{}:{}/wd/hub'.format(self.url ,self.port), desired_caps)
        return AppiumDriver.driver


    def kill_appium(self):
        '''
        结束appium进程
        :return:
        '''
        if os.popen('lsof -i:{}'.format(self.port)).read() == '':
            logger.info('appium pid is null')
        else:
            pid = os.popen('lsof -i:{}'.format(self.port)).readlines()[1].split()[1]
            os.system('kill -9 {}'.format(pid))
            logger.info('kill appium')


    def start_appium(self):
        '''
        启动appium服务
        :return:
        '''
        self.kill_appium()
        args = 'appium --log {} --session-override --udid {} -a  {} -p {}'.\
            format(appium_log,self.device ,self.url,self.port)
        logger.info('appium启动命令:{}'.format(args))
        appium = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, bufsize=1,close_fds=True)
        while True:
            appium_line = appium.stdout.readline().strip().decode()
            time.sleep(1)
            logger.info("启动appium中...")
            if 'Welcome to Appium' in appium_line or 'Error: listen' in appium_line:
                logger.info("appium启动成功")
                break
        return self.init_capability()


    def reset_keyboard(self ,device):
        '''
        重置键盘
        :return:
        '''
        try:
            cmd = "adb -s {} shell ime list -s | grep -v 'appium'".format(device)
            cmdline = subprocess.Popen(cmd ,shell=True, stdout=subprocess.PIPE)
            Keyboard = cmdline.stdout.readlines()[0].replace("\r\n" ,"")
            resetcmd = "adb -s {} shell ime set {}".format(device ,Keyboard)
            subprocess.call(resetcmd ,shell=True)
            logger.info("重置输入法完成")
        except Exception as e:
            logger.info("重置输入法异常!{}".format(e))


    def is_element_exist(self,driver, *loc):
        try:
            WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(loc))
            self.driver.find_element(*loc)
            return True
        except Exception as e:
            logger.warning(str(e))
            return False



