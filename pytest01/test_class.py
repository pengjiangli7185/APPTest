# coding = utf-8
# @Time : 2021/7/14 20:21
# @Author : pengjiangli
# @File : test_class.py
# @Software: PyCharm
# @contact: 292617625@qq.com
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")