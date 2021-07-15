# coding = utf-8
# @Time : 2021/7/15 16:50
# @Author : pengjiangli
# @File : Pytest02.py
# @Software: PyCharm
# @contact: 292617625@qq.com
import pytest

'''
2、fixture自动使用autouse=True 当用例很多的时候，每次都传这个参数，会很麻烦。fixture里面有个参数autouse，默认是False没开启的，可以设置为True开启自动使用fixture功能，这样用例就不用每次都去传参了 autouse设置为True，自动调用fixture功能

'''
@pytest.fixture(autouse=True)
def test1():
    print('\n开始执行function')

def test_a():
    print('---用例a执行---')

class TestCase:
    def test_b(self):
        print('---用例b执行')

if __name__=="__main__":
    pytest.main(["-s","Pytest02.py"])