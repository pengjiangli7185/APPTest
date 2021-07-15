# coding = utf-8
# @Time : 2021/7/15 16:57
# @Author : pengjiangli
# @File : Pytest03.py
# @Software: PyCharm
# @contact: 292617625@qq.com
import pytest

'''
3、使用装饰器@pytest.mark.usefixtures()修饰需要运行的用例
'''
@pytest.fixture()
def test1():
    print('\n开始执行function')

@pytest.mark.usefixtures('test1')
def test_a():
    print('---用例a执行---')

def test_d():
    print('---用例d执行---')


@pytest.mark.usefixtures('test1')
class TestCase:

    def test_b(self):
        print('---用例b执行---')

    def test_c(self):
        print('---用例c执行---')


if __name__=="__main__":
    pytest.main(["-s","Pytest03.py"])
