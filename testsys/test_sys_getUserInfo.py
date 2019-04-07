from conftest import http
from common.commonData import CommonData
import allure,pytest
@pytest.mark.getUserInfo
@allure.feature("查看用户信息模块")
class Test_getUserInfo():
    @allure.story("查看用户信息成功")
    def test_getUserInfo(self):
        getuserinfo_path = "/sys/getUserInfo"
        data={"token":CommonData.token}
        re_dict = http.post(getuserinfo_path,data)
        assert re_dict["code"]==200
        assert re_dict["msg"] == "操作成功"
        assert re_dict["object"]["userName"] == CommonData.mobile
        print("查看用户信息")

    @allure.story("查看用户信息成功")
    def test_getUserInfo_fail(self):
        getuserinfo_path = "/sys/getUserInfo"
        re_dict = http.post(getuserinfo_path)
        assert re_dict["code"]==200
        assert re_dict["msg"] == "操作成功"
        assert re_dict["object"]["userName"] == CommonData.mobile
        print("查看用户信息")
