# coding = utf-8
# @Time : 2021/7/14 20:46
# @Author : pengjiangli
# @File : test_example.py
# @Software: PyCharm
# @contact: 292617625@qq.com
import pytest


@pytest.fixture
def error_fixture():
    assert 0


def test_ok():
    print("ok")


def test_fail():
    assert 0


def test_error(error_fixture):
    pass


def test_skip():
    pytest.skip("skipping this test")


def test_xfail():
    pytest.xfail("xfailing this test")


@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass