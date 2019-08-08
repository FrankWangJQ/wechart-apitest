

import pytest

from tests.utils import Utils


@pytest.fixture(scope="session")
def token():
    return Utils.get_token_new()