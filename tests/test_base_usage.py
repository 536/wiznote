# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021/4/11 19:52
# @Author  : https://github.com/536
import os
import unittest

from wiznote import WizNote


class TestBaseUsage(unittest.TestCase):
    def setUp(self) -> None:
        self.username = os.environ.get('WIZ_USERNAME')
        self.assertIsNotNone(self.username, 'Invalid WIZ_USERNAME!')
        self.password = os.environ.get('WIZ_PASSWORD')
        self.assertIsNotNone(self.password, 'Invalid WIZ_PASSWORD!')

    def tearDown(self) -> None:
        pass

    def test_get_userinfo(self):
        with WizNote(username=self.username, password=self.password) as wiz:
            wiz.get_userinfo()


if __name__ == '__main__':
    unittest.main()
