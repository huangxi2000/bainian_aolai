import os
import yaml


# 读取yaml方法
class ReadYaml():
    # 实例化获取文件路径
    def __init__(self, filename):
        self.filename = os.getcwd() + os.sep + "data" + os.sep + filename

    # 读取yaml文件
    def read_yaml(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            return yaml.load(file)

    # 调试yaml文件
    def read_yaml_1(self):
        with open("../data/data_login.yaml", "r", encoding="utf-8") as file:
            return yaml.load(file)


# 调试查看数据
# if __name__ == '__main__':
#     arrs = ReadYaml("").read_yaml_1()
#     list1 = []
#     for data in arrs.values():
#         list1.append((data.get("username"), data.get("password"), data.get("expect_result"), data.get("expect_toast")))
#     print(list1)
