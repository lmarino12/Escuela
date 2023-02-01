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
    assert user.username == "asasd"

def test_prof_creation():
    user=Maestro.objects.create_user(
        username="asasd",
        f_name = "asasd",
        l_name = "asasd",
        email = "asasd",
        password = "asasd"
    )
    assert user.username == "asasd"