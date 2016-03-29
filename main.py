# -*- coding: utf-8 -*-
from faker import Factory
import requests
import random

fake = Factory.create()


def headers():
    return {
        'X-Forwarded-For': ip()
    }


def ip():
    return '.'.join([str(x) for x in [random.randint(1, 254),
                                      random.randint(1, 254),
                                      random.randint(1, 254),
                                      random.randint(1, 254)]])


def vote():
    username = fake.user_name()
    email = fake.email()
    real_name = Factory.create(locale='zh_CN').name()

    s = requests.session()
    s.headers.update(headers())

    register_data = {
        "userName": username,
        "email": email,
        "password": "123456",
        "password1": "123456",
        "realName": real_name,
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

    r1 = s.post(url, data=register_data)
    print(r1.status_code, r1.text)

    vote_data = {
        '_ZVING_METHOD': 'SupportOppose.voteOppose',
        '_ZVING_URL': '%2FdraftDetail',
        '_ZVING_DATA': '{"ID":"45115"}',
        '_ZVING_DATA_FORMAT': 'json',
    }
    r2 = s.post(url, data=vote_data, cookies=r1.cookies)
    print(r2.status_code, r2.text)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", help="vote how many times", default=10, type=int)
    parser.add_argument("--forever", help="vote forever", action='store_true')
    args = parser.parse_args()
    if args.forever:
        while True:
            vote()
    else:
        for i in range(args.count):
            vote()
