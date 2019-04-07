import requests
import json
from common.commonData import CommonData
class HttpUtil:
    def __init__(self):
        self.http=requests.session()
        self.proxies = CommonData.proxies  # 设置代理
        self.headers = {}  # 设置headers
        self.headers["Content-Type"] = "application/json;charset=UTF-8"
    def post(self,path,data=None):
        json_data=json.dumps(data)
        host=CommonData.host
        url=host+path
        if CommonData.token is not None:
            self.headers["token"]=CommonData.token
        resp=self.http.post(url=url,proxies=self.proxies,
                 data=json_data,
                 headers=self.headers)
        assert  resp.status_code==200
        resp_dict = json.loads(resp.text)
        return resp_dict











# print(re.text)#响应
# print(re.headers)#请求头
# print("http-code:",re.status_code)#状态码
