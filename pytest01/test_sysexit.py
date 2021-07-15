# coding = utf-8
# @Time : 2021/7/14 20:17
# @Author : pengjiangli
# @File : test_sysexit.py
# @Software: PyCharm
# @contact: 292617625@qq.com
import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()