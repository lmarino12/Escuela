import pytest
from autenticacion.models import *


def test_user_creation():
    user=Alumno.objects.create_user(
        username="asasd",
        f_name = "asasd",
        l_name = "asasd",
        email = "asasd",
        password = "asasd"
    )
    assert user.id == 1