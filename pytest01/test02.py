# coding = utf-8
# @Time : 2021/7/12 20:32
# @Author : pengjiangli
# @File : test02.py
# @Software: PyCharm
# @contact: 292617625@qq.com
import pytest



def test_a(self):  # test开头的测试函数
    print("------->test_a")
    assert 1  # 断言成功

def test_b(self):
    print("------->test_b")
    assert 0  # 断言失败

if __name__ == '__main__':
    pytest.main(["test02.py"])
