import pytest
from .models import Pilot


@pytest.fixture
def pilot():
    return Pilot('01', 'RUBINHO')


@pytest.fixture
def data():
    f = open('example.txt', "r")
    data = f.read()
    return data.split('\n')
