"""
    主页page类
"""
import allure

import page
from base.base import Base


class PageLogin(Base):
    # 点击 我
    @allure.step("点击 我")
    def page_me_click(self):
        self.base_click(page.login_click_me)

    # 点击 已有帐号,请登录
    @allure.step("点击 已有帐号,请登录")
    def page_have_count_click(self):
        self.base_click(page.login_have_count)

    # 输入帐号
    @allure.step("输入帐号")
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    @allure.step("输入密码")
    def page_input_password(self, password):
        self.base_input(page.login_password, password)

    # 点击登录
    @allure.step("点击登录")
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 获取昵称
    @allure.step("获取昵称")
    def page_get_nikename(self):
        return self.base_get_nikename(page.login_nikename)

    # 点击设置
    @allure.step("点击设置")
    def page_click_mysetting(self):
        self.base_click(page.my_setting)

    # 拖拽 短信提醒 到地址管理
    @allure.step("拖拽 短信提醒 到 地址管理")
    def page_drag_and_drop(self):
        # 定位短信提醒
        ele1 = self.base_find_element(page.setting_send_msg)
        # 定位修改密码
        ele2 = self.base_find_element(page.setting_update_pwd)
        # 拖拽
        self.base_drag_and_drop(ele1, ele2)

    # 点击退出
    @allure.step("点击退出")
    def page_click_logout_btn(self):
        self.base_click(page.setting_click_logout_btn)

    # 点击确认退出
    @allure.step("点击确认退出")
    def page_click_logout_ok(self):
        self.base_click(page.setting_logout_ok)

    # 封装整体退出
    def page_logout(self):
        # 拖拽
        self.page_drag_and_drop()
        # 点击退出
        self.page_click_logout_btn()
        # 确认退出
        self.page_click_logout_ok()