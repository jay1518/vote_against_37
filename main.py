# -*- coding: utf-8 -*-
from __future__ import print_function
from faker import Factory
import requests
import json

fake = Factory.create(locale='zh_CN')


def headers():
    return {
        'X-Forwarded-For': fake.ipv4(),
        'User-Agent': fake.user_agent()
    }


def vote(timeout=3):
    username = fake.user_name()
    email = fake.email()
    real_name = fake.name()

    s = requests.session()
    s.headers.update(headers())
    print(headers())

    register_data = {
        "userName": username,
        "email": email,
        "password": "123456",
        "password1": "123456",
        "realName": real_name,
        "province": u"北京市",
        "job": u"IT|互联网|通信",
        "mobile": "",
        "address": "",
    }

    register_data = {
        '_ZVING_METHOD': 'Register.doRegister',
        '_ZVING_URL': '%2Fregister',
        '_ZVING_DATA': json.dumps(register_data),
        '_ZVING_DATA_FORMAT': 'json',
    }

    url = "http://zqyj.chinalaw.gov.cn/ajax/invoke"

    r1 = s.post(url, data=register_data, timeout=timeout)
    print(r1.status_code, r1.text)

    vote_data = {
        '_ZVING_METHOD': 'SupportOppose.voteOppose',
        '_ZVING_URL': '%2FdraftDetail',
        '_ZVING_DATA': '{"ID":"45115"}',
        '_ZVING_DATA_FORMAT': 'json',
    }
    r2 = s.post(url, data=vote_data, cookies=r1.cookies, timeout=timeout)
    print(r2.status_code, r2.text)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", help="vote how many times", default=10, type=int)
    parser.add_argument("--timeout", help="request timeout, in seconds", default=3.0, type=float)
    parser.add_argument("--forever", help="vote forever", action='store_true')
    args = parser.parse_args()
    if args.forever:
        while True:
            try:
                vote(timeout=args.timeout)
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(e)
    else:
        for i in range(args.count):
            try:
                vote(timeout=args.timeout)
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(e)
