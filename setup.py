# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021/3/16 1:51
# @Author  : https://github.com/536
from setuptools import setup

setup(
    name='wiznote',
    version='1.1.3',
    description='Wiz Open API In Python.',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='https://github.com/536',
    url='https://github.com/536/wiz',
    packages=['wiz'],
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        'requests',
    ],
    zip_safe=False,
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
    ],
    project_urls={
        'Documentation': 'https://www.wiz.cn/wapp/pages/book/bb8f0f10-48ca-11ea-b27a-ef51fb9d4bb4',
        'Source': 'https://github.com/536/wiz',
    },
)
