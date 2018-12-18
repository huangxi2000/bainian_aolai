import os
import sys
sys.path.append(os.getcwd())
import allure

import pytest
from base.read_yaml import ReadYaml
from page.page_in import PageIn


# 获取yaml数据
def get_data():
    arrs = ReadYaml("data_login.yaml").read_yaml()
    list1 = []
    for data in arrs.values():
        list1.append((data.get("username"), data.get("password"), data.get("expect_result"), data.get("expect_toast")))
    return list1


    # 调试用
    # return [(18610453007, 123456, "itheima")]


# 登录
class TestLogin():
    # 实例化统一入口类
    def setup_class(self):
        self.login = PageIn().page_get_pagelogin()
        # 点击 我
        self.login.page_me_click()
        # 点击 去登录
        self.login.page_have_count_click()

    # 关闭驱动
    def teardown_class(self):
        self.login.driver.quit()

    # 正向登录 test_login
    @pytest.mark.parametrize("username, password, expect_result, expect_toast", get_data())
    @allure.step("开始执行登录测试")
    def test_login(self, username, password, expect_result, expect_toast):
        login = self.login
        if expect_result:
            try:
                # 输入帐号
                login.page_input_username(username)
                # 输入密码
                login.page_input_password(password)
                # 点击登录
                login.page_click_login_btn()
                # 获取昵称 + 断言
                assert expect_result in login.page_get_nikename()
                # 断言成功 退出
                # 点击个人 设置
                login.page_click_mysetting()
                # 退出
                login.page_logout()
                # 点击 我
                login.page_me_click()
                # 点击 去登录
                login.page_have_count_click()
            # 断言失败则
            except AssertionError:
                # 截图
                login.base_get_screenshot()
                # 打开图片 写入报告
                with open("./image/faild.png", "rb") as f:
                    allure.attach("失败原因: ", f.read(), allure.attach_type.PNG)
        # 逆向登录 test_login
        else:
            try:
                # 输入帐号
                login.page_input_username(username)
                # 输入密码
                login.page_input_password(password)
                # 点击登录
                login.page_click_login_btn()
                # 获取昵称 + 断言
                # assert expect_toast in login.base_get_toast(expect_toast)
                # 调试断言 失败,写入报告
                assert "登录密码错误1" in login.base_get_toast(expect_toast)
            except:
                # 截图
                login.base_get_screenshot()
                # 打开图片 写入报告
                with open("./image/faild.png", "rb") as f:
                    allure.attach("失败原因: ", f.read(), allure.attach_type.PNG)
