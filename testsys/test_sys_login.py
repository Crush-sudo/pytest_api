from common.commonData import CommonData
from conftest import http
import allure,pytest
@pytest.mark.login
@allure.feature("登录模块")
class Test_login():
    @allure.story("成功登录")
    def test_login_success(self):
        login_path = "/sys/login"
        login_data = {"userName": CommonData.mobile, "password": "123456"}
        resp_dict = http.post(login_path, login_data)
        assert resp_dict["code"] == 200
        assert resp_dict["msg"] == "操作成功"
        return resp_dict

    @allure.story("登录失败")
    def test_login_fail(self):
        login_path = "/sys/login"
        login_data = {"userName": "18613141314", "password": "111222"}
        resp_dict = http.post(login_path, login_data)
        assert resp_dict["code"] == 410
        assert resp_dict["msg"] == "用户名或密码错误"

    @allure.story("登录失败")
    def test_login_username_not(self):
        login_path = "/sys/login"
        login_data = {"userName": "18615649632", "password": "123456"}
        resp_dict = http.post(login_path, login_data)
        assert resp_dict["code"] == 301
        assert resp_dict["msg"] == "用户不存在"

    @allure.story("登录失败")
    def test_login_username_long(self):
        login_path = "/sys/login"
        login_data = {"userName": "186131413141314", "password": "123456"}
        resp_dict = http.post(login_path, login_data)
        assert resp_dict["code"] == 301
        assert resp_dict["msg"] == "用户不存在"

    @allure.story("登录失败")
    def test_login_username_null(self):
        login_path = "/sys/login"
        login_data = {"userName": "", "password": "123456"}
        resp_dict = http.post(login_path, login_data)
        assert resp_dict["code"] == 301
        assert resp_dict["msg"] == "用户不存在"

    @allure.story("登录失败")
    def test_login_psd_null(self):
        login_path = "/sys/login"
        login_data = {"userName": "18613141314", "password": ""}
        resp_dict = http.post(login_path, login_data)
        assert resp_dict["code"] == 410
        assert resp_dict["msg"] == "用户名或密码错误"

    @allure.story("登录失败")
    def test_login_onlyname(self):
        login_path = "/sys/login"
        login_data = {"userName": "18613141314"}
        resp_dict = http.post(login_path, login_data)
        assert resp_dict["code"] == 500
        assert resp_dict["msg"] == "内部服务器异常，请联系研发人员"

    @allure.story("登录失败")
    def test_login_onlypsd(self):
        login_path = "/sys/login"
        login_data = {"password": "123456"}
        resp_dict = http.post(login_path, login_data)
        assert resp_dict["code"] == 301
        assert resp_dict["msg"] == "用户不存在"


#密码错误
#用户名不存在
#用户名15位
#用户名为空
#密码为空
#参数不存在