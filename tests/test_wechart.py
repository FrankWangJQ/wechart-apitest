from unittest import TestCase

from tests.utils import Utils


class TestWeixin(TestCase):
    def test_get_token(self):
        print(Utils.get_token())
        assert Utils.get_token() !=""
