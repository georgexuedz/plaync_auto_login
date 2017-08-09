#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import urlparse
import os
import sys
import time
import traceback
import datetime
import json
import re
import functools
reload(sys)
sys.setdefaultencoding('utf-8')


print datetime.datetime.now()
login_cookie = 'SCOUTER=z7h3ocirne8gdt'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "316",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": login_cookie,
    "Host": "mlogin.plaync.com",
    "Origin": "https://mlogin.plaync.com",
    "Pragma": "no-cache",
    "Referer": "https://mlogin.plaync.com/login/signin?site_id=13&return_url=http%3A//kr.plaync.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
}

form_data = {
    "game_id": "13",
    "login_name": "helloria",
    "password": "noback66",
    # "password": "ksmk0rea",
    "return_url": "http://kr.plaync.com/",
    "is_mobile": 0,
    "site_id": 0,
    "token_app_id": "206A130F-BF96-667A-4E4B-FE1A62583117",
    "app_id": "206A130F-BF96-667A-4E4B-FE1A62583117",
    "skin_code": "rockblue",
    "credential_result": "cookie",
    "hide_external_login_button": "false",
    "hide_member_info_button": "false",
}

login_url = 'https://mlogin.plaync.com/login/signin'
# r = requests.post(login_url, headers=headers, proxies=proxies, timeout=20)
r = requests.post(login_url, headers=headers, data=form_data, timeout=20, allow_redirects=False)
print 'signin response header ======================>>>>>>>>>>>>>>>\n'
print r.headers
print datetime.datetime.now()


redirect_url = r.headers['Location']
redirect_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": login_cookie + '; JSESSIONID=' + r.cookies['JSESSIONID'],
    "Host": "mlogin.plaync.com",
    "Pragma": "no-cache",
    "Referer": "https://mlogin.plaync.com/login/signin?site_id=13&return_url=http%3A//kr.plaync.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
}
r = requests.get(redirect_url, headers=redirect_headers, timeout=20)
print 'redirect crosscookie header======================>>>>>>>>>>>>>>>\n'
print r.headers
print datetime.datetime.now()

secret_param_id = urlparse.parse_qs(urlparse.urlsplit(redirect_url).query)['secret_param_id']


def crosscookie():
    url = 'https://mlogin.plaync.co.kr/login/crosscookie'
    cookie = "SCOUTER=z383i32n6dji0n"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "133",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": cookie,
        "Host": "mlogin.plaync.co.kr",
        "Origin": "https://mlogin.plaync.com",
        "Pragma": "no-cache",
        "Referer": redirect_url,
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    }

    form_data = {
        "current_domain_index": 1,
        "return_url": "http://kr.plaync.com/",
        "persistent": "false",
        "secret_param_id": secret_param_id,
    }
    r1 = requests.post(url, headers=headers, data=form_data, timeout=20)
    print 'first crosscookie header======================>>>>>>>>>>>>>>>\n'
    print r1.headers

    cookie_key_ls = ['GPLLV', 'GPSESSIONID', 'GPVLU', 'JSESSIONID']
    cookie_ls = [key + '=' + r1.cookies[key] for key in cookie_key_ls]
    cookie_ls.append(cookie)

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "133",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": ', '.join(cookie_ls),
        "Host": "mlogin.plaync.co.kr",
        "Origin": "https://mlogin.plaync.com",
        "Pragma": "no-cache",
        "Referer": "https://mlogin.plaync.co.kr/login/crosscookie",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    }

    form_data = {
        "current_domain_index": 2,
        "return_url": "http://kr.plaync.com/",
        "persistent": "false",
        "secret_param_id": secret_param_id,
    }
    r = requests.post(url, headers=headers, data=form_data, timeout=20, allow_redirects=False)
    print 'second crosscookie header======================>>>>>>>>>>>>>>>\n'
    print r.headers

    url = 'http://kr.plaync.com/'

    cookie_key_ls = ['GPLLV', 'GPSESSIONID', 'GPVLU']
    cookie_ls = [key + '=' + r1.cookies[key] for key in cookie_key_ls]
    cookie_ls.append(cookie)
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": ', '.join(cookie_ls),
        "Host": "kr.plaync.com",
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    }
    r = requests.get(url, headers=headers, timeout=20)
    print 'real page =========================>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    print r.headers
    print r.text

crosscookie()

