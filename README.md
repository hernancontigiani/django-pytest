# django-pytest

# 1 - Install pytest-django
Include in requirements.txt
```
pytest-django==4.5.2
```

# 2 - Create a django project and app
```sh 
django-admin startproject back
python manage.py startapp miapp
```

# 3 - Config pytest
Create a file pytest.ini inside the proyect folder (back)
```
[pytest]
DJANGO_SETTINGS_MODULE = back.settings
python_files = tests.py test_*.py *_tests.py
```

# 4 - Pytest Fixtures
- In this example, we are going to create a script where we are going to place all functions helpers (fixtures) for our tests.
- For now, we create "pytest_fixtures" file with this content:
```python
import pytest

@pytest.fixture
def create_user(db, django_user_model):
    def make_user(**kwargs):
        return django_user_model.objects.create_user(**kwargs)
    return make_user
```

Create user will be used any time we need to login with credentials in our API tests.

# Test
For this example, inside or app folder (miapp) we include in "tests.py":
```python
import pytest
from pytest_fixtures import *

from django.contrib.auth.models import User


@pytest.mark.django_db
def test_my_user(create_user):
    user = create_user(username='root', password='12345', is_superuser=True)
    assert user.is_superuser
```


Launch test inside the project folder (back):
```sh
pytest
```

# Reference
- https://djangostars.com/blog/django-pytest-testing/
- https://pytest-django.readthedocs.io/en/latest/database.html