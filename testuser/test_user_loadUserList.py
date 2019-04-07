from conftest import http
import pytest
from common.commonData import CommonData
import allure
class Test_loadUserList():
    @allure.story("检查列表中的第一个正确")
    def tset_loadUserList(self):
        path="/user/loadUserList"
        data={"pageCurrent":1,"pageSize":10,"nickName":"","userName":"","regionId":1}
        re_dict=http.post(path,data)
        assert re_dict["code"]==200
        assert re_dict["object"]["list"][0]["id"]==CommonData.new_userid
        assert re_dict["object"]["list"][0]["userName"] == CommonData.mobile
        print("检查列表中的第一个正确")