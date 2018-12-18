import allure

from base.get_driver import get_driver
from page.page_login import PageLogin

# 获取driver地址
driver = get_driver()


# 统一入口类
class PageIn():
    @allure.step("实例化登录页面的对象")
    def page_get_pagelogin(self):
        return PageLogin(driver)
