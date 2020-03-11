
#!/usr/bin/env python
#coding:utf-8
import json
import requests
import sys

url = "http://200.200.1.247/api_jsonrpc.php"
header = {"Content-Type": "application/json-rpc"}
username = 'Admin'
password = 'sangforits123'

def do_request(data):
    try:
        request = requests.post(url=url, headers=header, data=json.dump(data),timeout=60)
        if request.json()["result"]:
            return request.json()["result"]
    except requests.ConnectionError:
        return None
    else:
        return None

def get_token(username,password):
    data = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": username,
            "password": password
        },
        "id": 1,

    }
    value = json.dump(data).enncode('utf-8')
    token = do_request(data)
    if not token:
        print("登录失败")
    print(token)
    print(value)
    get_token()


# def get_host(hostid):
#   data = json.dumps({
#            "jsonrpc": "2.0",
#            "method": "host.get",
#            "params": {
#                "output": "extend",
#            },
#            "id": 1,
#
#    })
#    resp = do_request(data)
#    print(resp)

