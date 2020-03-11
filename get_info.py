#!/usr/bin/env python
# coding:utf8
import requests
import json
#from get_ip import getToken
headers = {'Content-Type': 'application/json-rpc'}
server_ip = '200.200.1.247'

url = 'http://%s/zabbix/api_jsonrpc.php' % server_ip
#登录地址 返回token
def getToken(username, passwd):
    data = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": username,
            "password": passwd
        },
        "id": 0

    }
    request = requests.post(url=url, headers=headers, data=json.dumps(data))
    dict = json.loads(request.text)
    return dict['result']
#获取信息
def get_info(tokenNumber):
    data = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": [
                "hostid",
                "host"
            ],
            "selectInterfaces": [
                "interfaceid",
                "ip"
            ]
        },
        "id": 2,
        "auth": tokenNumber,
    }
    request = requests.post(url=url,headers=headers, data=json.dumps(data))
#json.dumps	将 Python 对象编码成 JSON 字符串
#json.loads	将已编码的 JSON 字符串解码为 Python 对象
    #dict = json.loads(request.text)
    dict = json.loads(request.content.decode('utf-8'))
   # return dict['interfaces']
    return dict['result']
if __name__ == "__main__":
    username = 'Admin'
    passwd = 'sangforits123'
    #获取
    token_num = getToken(username, passwd)
    interface_result = get_info(token_num)
    for i in interface_result.key():

        ip.append(interface_result["key"])
        print("ip")

