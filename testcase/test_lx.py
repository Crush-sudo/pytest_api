# from conftest import http
# import pytest
# import os
# from framework.util import Util
# from ddt import ddt,data
# excelPath=os.path.abspath(".")+"/tools/test_login.xlsx"
# sheetName="login"
# testdata=Util().read_excel(excelPath,sheetName)
# @ddt
# class Test_login():
#     @data(*testdata)
#     @pytest.mark.lx
#     def test_login_success(self,data):
#         username=data["username"]
#         password=data["password"]
#         code=int(data["code"])
#         msg=data["msg"]
#         print(username,password,code,msg)
#         login_path = "/sys/login"
#         login_data = {"userName": username, "password": password}
#         resp_dict = http.post(login_path, login_data)
#         assert resp_dict["code"] == code
#         assert resp_dict["msg"] == msg
#         print("登录成功")
#         # assert resp_dict["object"]["userId"] == userid
#
