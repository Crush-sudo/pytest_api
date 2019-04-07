from conftest import http
import pytest
from common.commonData import CommonData
import allure
class Test_loadUserInfo():
    @allure.story("查看刚注册的用户详情")
    def test_loadUserInfo(self):
        path="/user/loadUserInfo"
        data={"id":CommonData.new_userid}
        re_dict=http.post(path,data)
        assert re_dict["code"]==200
        assert re_dict["msg"]=="操作成功"
        assert re_dict["object"]["userName"]==CommonData.mobile
        print(re_dict)