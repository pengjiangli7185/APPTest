# coding = utf-8
# @Time : 2021/7/12 20:41
# @Author : pengjiangli
# @File : test03.py
# @Software: PyCharm
# @contact: 292617625@qq.com
import pytest


class PyTest_03:

    def setup(self):
        print("------->setup_method")

    def teardown(self):
        print("------->teardown_method")

    def test_a(self):
        print("------->test_a")
        assert 1

    def test_b(self):
        print("------->test_b")


if __name__ == '__main__':
    pytest.main(["-s" , "test03.py"])