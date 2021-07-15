# coding = utf-8
# @Time : 2021/7/14 19:56
# @Author : pengjiangli
# @File : pytest04.py
# @Software: PyCharm
# @contact: 292617625@qq.com
import pytest


class Test_py:
    #函数级别
    def setup(self):
        print("开始方法")

    #函数级别
    def teardown(self):
        print("结束方法")

    def test_a(self):
        print("执行方法:test_a")

    def test_b(self):
        print("执行方法test_b")



class TestB:
    # 测试类级开始
    def setup_class(self):
        print("类级开始------->setup_class")

    # 测试类级结束
    def teardown_class(self):
        print("类级结束------->teardown_class")

    def test_a(self):
        print("------->test_a")
        assert 1

    def test_b(self):
        print("------->test_b")


if __name__ == '__main__':
    pytest.main(["-s","pytest04.py"])
