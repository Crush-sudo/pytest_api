from conftest import http
import pytest
from common.commonData import CommonData
import allure
@pytest.mark.changepwd
@allure.feature("修改密码模块")
class Test_changePwd():
    @allure.story("修改密码成功")
    @pytest.mark.usefixtures("re_changePwd")
    def test_changePwd(self):
        changePwd_path = "/sys/changePwd"
        data = {"userId": 112,"userName": CommonData.mobile,"oldPwd": "123456","password":"802352"}
        re_dict = http.post(changePwd_path, data)
        assert re_dict["code"] == 200
        assert re_dict["msg"] == "操作成功"
        print("修改密码成功")

    @allure.story("修改密码成功")
    @pytest.mark.usefixtures("re_changePwd")
    def test_changePwd_id_null(self):
        changePwd_path = "/sys/changePwd"
        data = {"userId": "","userName": CommonData.mobile,"oldPwd": "123456","password":"802352"}
        re_dict = http.post(changePwd_path, data)
        assert re_dict["code"] == 200
        assert re_dict["msg"] == "操作成功"
        print("修改密码成功")

    @allure.story("修改密码失败")
    def test_changePwd_name_null(self):
        changePwd_path = "/sys/changePwd"
        data = {"userId": 112, "userName": "", "oldPwd": "123456", "password": "802352"}
        re_dict = http.post(changePwd_path, data)
        assert re_dict["code"] == 411
        assert re_dict["msg"] == "旧密码错误"
        print("修改密码失败")
    @pytest.fixture
    def re_changePwd(self):
        yield
        changePwd_path = "/sys/changePwd"
        data = {"userId": 112,"userName": CommonData.mobile,"oldPwd": "802352","password":"123456"}
        re_dict = http.post(changePwd_path, data)
        assert re_dict["code"] == 200
        assert re_dict["msg"] == "操作成功"
        print("恢复密码成功")

