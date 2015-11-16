# -*- coding: utf-8 -*-
from hoge import Hoge
import pytest

class TestHoge1(object):

    def pytest_funcarg__hoge(request):
        return Hoge(1)

    def test_type(self, hoge):
        assert isinstance(hoge, Hoge)

    def test_val(self, hoge):
        assert hoge.val == 1

        hoge.update('hoge')
        assert hoge.val == 'hige'

if __name__ == '__main__':
    pytest.main()
