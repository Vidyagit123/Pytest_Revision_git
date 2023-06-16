import pytest

from selenium.webdriver.chrome import webdriver
from selenium import webdriver

class Test_py:
    @pytest.mark.group1

    def test_sum_1(self):
        a=4
        b=5
        sum=a+b
        print("sum="+str(sum))
        if sum==9:
            assert True
        else:
            assert False

    @pytest.mark.group1
    def test_mul_2(self):
        a = 4
        b = 5
        mul = a * b
        print("mul="+str(mul))
        if mul==20:
            assert True
        else:
            assert False

    @pytest.mark.group2
    def test_credence_3(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://credence.in/")
        print(driver.title)
        if driver.title=="Credence":
            print("U r at credence site")
            assert True
        else:
            print("U r at wrong site")
            assert False
        driver.quit()

    def test_sum_4(self):
        a = 4
        b = 5
        sum = a + b
        print("sum=" + str(sum))
        if sum == 9:
            assert True
        else:
            assert False


# To run test cases paralle--->  -n
# to generate html report----->  pytest --html=Reports/report1.html -n=2
