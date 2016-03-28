# coding: utf-8
import requests
from random import shuffle
from faker import Factory

fake = Factory.create()

username = list(filter(str.isalpha, fake.name()))
username = ''.join(username)
email = fake.email()
realname = Factory.create(locale='zh_CN').name()

register_data = {
    "userName": username,
    "email": email,
    "password": "123456",
    "password1": "123456",
    "realName": realname,
    "province": "北京市",
    "job": "IT|互联网|通信",
    "mobile": "",
    "address": "",
}

register_data = {
    '_ZVING_METHOD': 'Register.doRegister',
    '_ZVING_URL': '%2Fregister',
    '_ZVING_DATA': str(register_data),
    '_ZVING_DATA_FORMAT': 'json',
}

url = "http://zqyj.chinalaw.gov.cn/ajax/invoke"

r1 = requests.post(url, data=register_data)
print(r1.status_code, r1.text)

vote_data = {
    '_ZVING_METHOD': 'SupportOppose.voteOppose',
    '_ZVING_URL': '%2FdraftDetail',
    '_ZVING_DATA': '{"ID":"45114"}',
    '_ZVING_DATA_FORMAT': 'json',
}
r2 = requests.post(url, data=vote_data, cookies=r1.cookies)
print(r2.status_code, r2.text)
