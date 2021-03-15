# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021/3/15 22:33
# @Author  : https://github.com/536
from .core import API


class Wiz(API):
    def login(self, userId: str, password: str):
        """用户登录"""
        return self.session.post(
            url=self.url('{AS_URL}/as/user/login'),
            json={'userId': userId, 'password': password},
        )

    def get_userinfo_by_token(self):
        """通过有效的token，获取用户信息"""
        return self.session.post(
            url=self.url('{AS_URL}/as/user/login/token')
        )

    def logout(self):
        """注销token"""
        return self.session.get(
            url=self.url('{AS_URL}/as/user/logout')
        )

    def get_userinfo(self):
        """获取用户信息"""
        return self.session.get(
            url=self.url('{AS_URL}/as/user/info')
        )

    def keep(self):
        """延长token有效期"""
        return self.session.get(
            url=self.url('{AS_URL}/as/user/keep')
        )

    def token2temp(self):
        """通过当前token获取一个临时id

        然后通过这个id，在60秒内可以重新拿到token。该id一次有效，使用后就会失效。
        可以用于跨域页面跳转，避免泄漏token
        """
        return self.session.get(
            url=self.url('{AS_URL}/as/token/token2temp')
        )

    def get_token_by_tokenid(self, tempToken):  # NOQA
        """通过tokenid获取token"""
        return self.session.get(
            url=self.url('{AS_URL}/as/token/temp2token'),
            params={'tempToken': tempToken}
        )
