#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,time,shutil

log_path = 'log'
if os.path.exists(log_path):
    shutil.rmtree(log_path)
os.mkdir(log_path)

login_log = os.path.join(log_path,'login.log')
appium_log = os.path.join(log_path,'appium.log')
devices_name = '192.168.56.101:5555'
package_name = 'com.tencent.mm'
lanuch_activity = 'com.tencent.mm.ui.LauncherUI'
allow = "//*[@text='允许']"
allow_en = "//*[@text='ALLOW']"
login_btn = "//*[@text='登录']"
weixin_btn = "//*[@text='用微信号/QQ号/邮箱登录']"
serach_btn = '//android.widget.TextView[@content-desc="搜索"]'
serach_id = 'com.tencent.mm:id/ht'
app_icon = 'com.tencent.mm:id/ko'
app_name = u'腾讯医典'