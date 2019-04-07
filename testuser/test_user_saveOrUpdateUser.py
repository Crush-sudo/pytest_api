import random
from conftest import http
import pytest
from common.commonData import CommonData
from testuser.test_user_loadUserList import Test_loadUserList
from testuser.test_user_loadUserInfo import Test_loadUserInfo
from testsys.test_sys_login import Test_login
import allure
@allure.feature("用户注册")
class Test_saveOrUpdateUser():
    @pytest.mark.zhuce
    @allure.story("注册成功")
    def test_saveOrUpdateUser(self):
        path="/user/saveOrUpdateUser"
        nickname=str(random.randint(10000000,100000000))
        mo="186"+nickname
        CommonData.mobile=mo
        data={"nickName":CommonData.name,"userName":mo,"telNo":"","email":"","address":"","roleIds":"","regionId":1,"regionLevel":1}
        re_dict=http.post(path,data)
        assert re_dict["code"]==401
        print("注册成功")

        resp_dict=Test_login().test_login_success()
        CommonData.new_userid=resp_dict["object"]["userId"]
        print("新用户登录成功")

        Test_loadUserList().tset_loadUserList()
        Test_loadUserInfo().test_loadUserInfo()
