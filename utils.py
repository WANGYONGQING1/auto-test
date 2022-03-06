from selenium import webdriver
from time import sleep

"""导入三方自动安装驱动库webdriver_manager"""

from webdriver_manager.chrome import ChromeDriverManager


class DriverUtil:
    """驱动方法"""

    driver = None

    def get_driver(self, url):
        "" "获取浏览器驱动"""
        if self.driver is None:
            '''自动下载驱动并生成驱动'''
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
            self.driver.get(url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
        return self.driver

    def quit_driver(self):
        """推出浏览器方法"""
        if self.driver:
            self.driver.quit()
            self.driver = None
if __name__ == '__main__':
    url='https://www.cnpython.com/qa/1443510'
    a=DriverUtil()
    a.get_driver(url)
    sleep(10)
    a.quit_driver()