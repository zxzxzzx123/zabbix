#!/usr/bin/env python
# coding:utf8
import requests
import json

headers = {'Content-Type': 'application/json-rpc'}
server_ip = '200.200.1.247'

url = 'http://%s/zabbix/api_jsonrpc.php' % server_ip


# 获取token
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

#从api获取主机信息
def getHosts(token_num):
    data = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": ["hostid", "host"],
            "selectInterfaces": ["interfaceid", "ip"]
        },
        "id": 2,
        "auth": token_num,
        }
    request = requests.post(url=url, headers=headers, data=json.dumps(data))
    dict = json.loads(request.content.decode('utf-8'))
    #print(dict['result'])
    return dict['result']

#整理信息，输出想要的信息，组合成字典
def getProc(data):
    dict = {}
    list =data
    for i in data:
        host = i['host']
        inter = i['interfaces']
        for j in inter:
            ip = j['ip']
            dict[host]=ip
    return  dict

#排序ip列表
def  getData(dict):
    data = dict
    ip_list = []
    for key in data.keys():    #Python 字典(Dictionary) keys() 函数以列表返回一个字典所有的键。
        ip = data[key]
        ip_list.append(ip)
    ip_list = list(set(ip_list)) #list() 方法用于将元组转换为列表。
    ip_list.sort()  #sort() 函数用于对原列表进行排序
    return ip_list

#整理输出ip
def getGroup(ip_list):
    ip_group = {}
    ips = ip_list
    f = open("out1.txt","w")
    for i in ips:
        f.write(i + '\n')
    f.close()

if __name__ == "__main__":
    username = 'Admin'
    passwd = 'sangforits123'
    token_number = getToken(username,passwd)
   # print(token_number)
    data = getHosts(token_number)
    hosts = getProc(data)
   # print(hosts)
ip_list = getData(hosts)
getGroup(ip_list)

