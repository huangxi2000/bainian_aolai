from selenium.webdriver.common.by import By
"""
    登录配置数据
"""

# 主页 我
login_click_me = By.ID, "com.yunmall.lc:id/tab_me"
# 已有帐号,去登录
login_have_count = By.ID, "com.yunmall.lc:id/textView1"
# 帐号输入框
login_username = By.ID, "com.yunmall.lc:id/logon_account_textview"
# 密码输入框
login_password = By.ID, "com.yunmall.lc:id/logon_password_textview"
# 登录按钮
login_btn = By.ID, "com.yunmall.lc:id/logon_button"
# 昵称
login_nikename = By.ID, "com.yunmall.lc:id/tv_user_nikename"
# 个人页面设置
my_setting = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
# 设置 短信提醒
setting_send_msg = By.ID, "com.yunmall.lc:id/setting_sms_notify"
# 设置 修改密码
setting_update_pwd = By.ID, "com.yunmall.lc:id/setting_modify_pwd"
# 设置 退出
setting_click_logout_btn = By.ID, "com.yunmall.lc:id/setting_logout"
# 确认 退出
setting_logout_ok = By.ID, "com.yunmall.lc:id/ymdialog_right_button"