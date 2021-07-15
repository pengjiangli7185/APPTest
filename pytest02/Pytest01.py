# coding = utf-8
# @Time : 2021/7/15 16:40
# @Authord : pengjiangli
# @File : Pytest01.py
# @Software: PyCharm
# @contact: 292617625@qq.com
import pytest


@pytest.fixture()
def test1():
    print('\n开始执行function')
    return 11

def test_a():
    print('---用例a执行---')


class TestCase:
    def test_b(self,test1):
        print('---用例b执行')
        print(test1)



if __name__ == '__main__':
    pytest.main(["-s","Pytest01.py"])

