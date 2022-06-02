# -*- coding: UTF-8 -*-
from requests import options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json
from selenium.webdriver.common.action_chains import ActionChains

with open(r"C:\Users\廖峻德\Desktop\自動爬蟲\自動上課\class.json",'r',encoding='utf8') as jfies:
    jdata = json.load(jfies)
while 7==7:
    idc = input("請輸入課程名稱:")
    if idc == "歷史":
            driver = webdriver.Edge()
            driver.get(jdata[idc])
            #帳號
            driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('s11003129@school.saihs.edu.tw')
            driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span').click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/input').click()
            #密碼
            driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('A131137373')
            driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span').click()
    else:
        if  idc == "實習2" :
            driver = webdriver.Edge()
            driver.get(jdata[idc])
            time.sleep(3)
            driver.find_elements_by_class_name("pmHCK")[-1].click()
            time.sleep(2)
            driver.find_elements_by_class_name("pmHCK")[0].click()
        else:
            if idc == "體育":
                driver = webdriver.Edge()
                driver.get("https://drive.google.com/drive/folders/18ZwqgCwFPN7f0DqiDaAG8_a41x79cm_n")
                time.sleep(3)
                driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[3]/div[1]/a').click()
                time.sleep(2)
                                        #帳號
                driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('s11003129@school.saihs.edu.tw')
                driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/input').click()
                                                #密碼
                driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('A131137373')
                driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span').click()
                time.sleep(3)
                list1 = driver.find_elements_by_class_name("pmHCK")[-1]
                ActionChains(driver).double_click(list1).perform()
                time.sleep(3)
                list2 = driver.find_elements_by_class_name("pmHCK")[1]
                ActionChains(driver).double_click(list2).perform()
                time.sleep(3)
                driver.switch_to.window(driver.window_handles[1])
                driver.find_element_by_xpath('//*[@id="i5"]').click()
                driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div').send_keys('29')
                driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div').send_keys('廖峻德')
                driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]').send_keys('窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道窩不知道')
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span').click()

            else:
                if idc == "基電":
                    driver = webdriver.Edge()
                    driver.get("https://drive.google.com/drive/folders/1AimduyXqEJkF_FrND48qI76lm8vE4uZK")
                    time.sleep(3)
                    driver.find_elements_by_class_name("pmHCK")[-1].click()
                    time.sleep(2)
                    driver.find_elements_by_class_name("pmHCK")[0].click()
                else:
                    if idc == "物理":
                        option = webdriver.EdgeOptions()
                        option.add_experimental_option("prefs", { \
                        "profile.default_content_setting_values.media_stream_mic": 1,      
                        "profile.default_content_setting_values.media_stream_camera": 1,  
                        "profile.default_content_setting_values.geolocation": 1,           
                        "profile.default_content_setting_values.notifications": 1 ,      
                        })
                        driver = webdriver.Edge(options=option)
                        driver.get("https://meet.google.com/")
                                                # 點擊登陸
                        driver.find_element_by_xpath('//*[@id="drawer"]/div/div[3]/div[1]/div/span[1]/a').click()
                                                #帳號
                        driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('s11003129@school.saihs.edu.tw')
                        driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span').click()
                        time.sleep(3)
                        driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/input').click()
                                                #密碼
                        driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('A131137373')
                        driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span').click()
                        time.sleep(2)
                        driver.get("https://drive.google.com/drive/folders/18O5ecgAUFUaFTqCfvpQa0N6152wIo6hQ")
                        time.sleep(2)
                        dri1 = driver.find_elements_by_class_name("pmHCK")[4]
                        ActionChains(driver).double_click(dri1).perform()
                        time.sleep(1)
                        dri2 = driver.find_elements_by_class_name("pmHCK")[0]
                        ActionChains(driver).double_click(dri2).perform()
                        time.sleep(1)
                        dri3 = driver.find_elements_by_class_name("pmHCK")[0]
                        ActionChains(driver).double_click(dri3).perform()
                        time.sleep(1)
                        dri4 = driver.find_elements_by_class_name("pmHCK")[0]
                        ActionChains(driver).double_click(dri4).perform()
                        time.sleep(5)
                        driver.find_element_by_class_name("a-b-Xa-La-A").click()
                        driver.switch_to.window(driver.window_handles[1])
                        time.sleep(10)
                        driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[3]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div[1]').click()
                        time.sleep(1)
                        driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div[1]').click()

                        time.sleep(1)
                                            #請求進入會議室
                        driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/button/span').click()
                    else:
                        if idc == "國防":
                            driver = webdriver.Edge()
                            driver.get(jdata[idc])
                            time.sleep(2)
                            driver.find_elements_by_class_name("pmHCK")[-1].click()
                        else:
                            if idc == "化學":
                                driver = webdriver.Edge()
                                driver.get(jdata[idc])
                            else:
                                options = webdriver.EdgeOptions()
                                options.add_experimental_option("prefs", { \
                                    "profile.default_content_setting_values.media_stream_mic": 1,      
                                    "profile.default_content_setting_values.media_stream_camera": 1,  
                                    "profile.default_content_setting_values.geolocation": 1,           
                                    "profile.default_content_setting_values.notifications": 1 ,
                                    'blink-settings=imagesEnabled': 2      
                                    })

                                driver = webdriver.Edge(options=options)
                                driver.get("https://meet.google.com/")
                                    # 點擊登陸
                                driver.find_element_by_xpath('//*[@id="drawer"]/div/div[3]/div[1]/div/span[1]/a').click()
                                    #帳號
                                driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('s11003129@school.saihs.edu.tw')
                                driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span').click()
                                time.sleep(3)
                                driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/input').click()
                                    #密碼
                                driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('A131137373')
                                driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span').click()
                                time.sleep(2)
                                    #輸入會議代碼
                                driver.find_element_by_xpath('//*[@id="i4"]').send_keys(jdata[idc])
                                time.sleep(1)
                                driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[2]/div[2]/button/span').click()
                                time.sleep(5)
                                    #關閉鏡頭、麥克風
                                driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[3]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div[1]').click()
                                time.sleep(1)
                                driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div[1]').click()
                                time.sleep(1)
                                #請求進入會議室
                                driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/button/span').click()



