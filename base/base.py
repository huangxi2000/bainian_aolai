from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self, driver):
        self.driver = driver

    # 封装 查找元素
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 封装 点击
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 封装 输入
    def base_input(self, loc, value):
        ele = self.base_find_element(loc)
        ele.clear()
        ele.send_keys(value)

    # 封装 获取昵称
    def base_get_nikename(self, loc):
        return self.base_find_element(loc).text

    # 封装 截图
    def base_get_screenshot(self):
        self.driver.get_screenshot_as_file("./image/faild.png")

    # 封装 拖拽
    def base_drag_and_drop(self, ele1, ele2):
        self.driver.drag_and_drop(ele1, ele2)

    # 获取toast
    def base_get_toast(self, msg):
        loc = By.XPATH, "//*[contains(@text, '%s')]" % msg
        return self.base_find_element(loc, timeout=3, poll=0.1).text


