import pytest


@pytest.mark.fixture(scope="session")
def user_cred(request):
    return request.param

