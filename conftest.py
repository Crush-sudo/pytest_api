import pytest
from util.http_util import HttpUtil
from common.commonData import CommonData
http=HttpUtil()
url=CommonData.host
login_path="/sys/login"
login_out_path="/sys/logout"
login_data={"userName": CommonData.mobile,"password": CommonData.password}
@pytest.fixture(scope="session",autouse=True)
def login():
    resp_dict=http.post(login_path,login_data)
    assert resp_dict["code"]==200
    print("登录成功")
    CommonData.token = (resp_dict["object"]["token"])
    yield
    resp_dict=http.post(login_out_path)
    assert resp_dict["code"] == 200
    print("退出登录")