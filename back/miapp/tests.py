import pytest
from pytest_fixtures import *

from django.contrib.auth.models import User


@pytest.mark.django_db
def test_my_user(create_user):
    user = create_user(username='root', password='12345', is_superuser=True)
    assert user.is_superuser
