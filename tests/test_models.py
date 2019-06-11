import pytest

from datetime import timedelta

from .models import Pilot


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
