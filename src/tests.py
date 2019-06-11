import pytest

from datetime import timedelta

from .utils import format_bool, format_to_timedelta, \
    format_to_int, format_to_float, format_line, process_drivers
from .models import Pilot


@pytest.fixture
def pilot():
    return Pilot('01', 'RUBINHO')

@pytest.fixture
def data():
    f = open('./example.txt', "r")
    data = f.read()
    return data.split('\n')


def test_models_pilot_init(pilot):
    assert pilot.finished is False
    assert pilot.fastest_lap is None
    assert len(pilot.laps) == 0
    assert str(pilot) == pilot.code
    assert pilot.fmt_finished == 'NAO'


def test_models_pilot_add_lap(pilot):
    lap = {
        'speed': 10,
        'number': 1,
        'time': timedelta(seconds=90),
    }
    pilot.add_lap(lap)
    assert pilot.finished is False
    assert pilot.fastest_lap == lap.get('time')
    assert pilot.total_laps == 1
    assert pilot.speed == lap.get('speed')
    assert pilot.time == lap.get('time')

    lap = {
        'speed': 20,
        'number': 4,
        'time': timedelta(seconds=120),
    }
    pilot.add_lap(lap)
    assert pilot.finished is True
    assert pilot.fastest_lap == timedelta(seconds=90)
    assert pilot.total_laps == 2
    assert pilot.speed == 15
    assert pilot.time == timedelta(seconds=210)


def test_models_pilot_print_drivers(data):
    assert len(Pilot.print_drivers(process_drivers(data, Pilot))) == 10


def test_utils_pilot_process_drivers(data):
    assert len(process_drivers(data, Pilot).keys()) == 6


def test_utils_format_bool():
    assert format_bool(True) == 'SIM'
    assert format_bool(False) == 'NAO'


def test_utils_format_to_timedelta():
    value = format_to_timedelta('1:02.852')
    assert value.seconds == 62


def test_utils_format_to_int():
    assert format_to_int('1') == 1
    assert format_to_int('t') == None


def test_utils_format_to_float():
    assert format_to_float('12,2') == 12.2


def test_utils_format_line():
    line = '23:49:08.277      038 – F.MASSA                           1		1:02.852                        44,275'
    date, code, _, name, lap, time_, speed = format_line(line)

    assert code == '038'
    assert name == 'F.MASSA'
    assert lap == 1
    assert time_.seconds == 62
    assert speed == 44.275

    line = 'NOT A VALID LINE'
    assert len(format_line(line)) == 0
