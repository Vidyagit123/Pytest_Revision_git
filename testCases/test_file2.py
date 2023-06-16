import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

class Test_py2:

    def test_sum_5(self):
        a=4
        b=5
        sum=a+b
        print("sum="+str(sum))
        if sum==9:
            assert True
        else:
            assert False

    @pytest.mark.group2
    def test_credence_007(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("headless")
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "opencall").click()
        l = len(driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p/a"))
        time.sleep(2)
        list=[]
        for i in range(1,l+1):
            Mobno=driver.find_element(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p/a["+str(i)+"]").text
            # print("MobileNumber-->" + str(r)+"-->" + str(MobileNumber))
            list.append(Mobno)
        print(list)
        if "+91 9091929355" in list:
            print("Mobile number is present")
            print(list.index("+91 9091929355"))
            assert True
        else:
            print("Mobile number is not present")
            assert False
        driver.quit()
