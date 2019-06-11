from datetime import timedelta


def test_models_pilot_init(pilot):

    if not pilot.finished is False:
        raise AssertionError()

    if not pilot.fastest_lap is None:
        raise AssertionError()

    if not len(pilot.laps) == 0:
        raise AssertionError()

    if not str(pilot) == pilot.code:
        raise AssertionError()

    if not pilot.fmt_finished == 'NAO':
        raise AssertionError()


def test_models_pilot_add_lap(pilot):
    lap = {
        'speed': 10,
        'number': 1,
        'time': timedelta(seconds=90),
    }
    pilot.add_lap(lap)

    if not pilot.finished is False:
        raise AssertionError()

    if not pilot.fastest_lap == lap.get('time'):
        raise AssertionError()

    if not pilot.total_laps == 1:
        raise AssertionError()

    if not pilot.speed == lap.get('speed'):
        raise AssertionError()

    if not pilot.time == lap.get('time'):
        raise AssertionError()

    lap = {
        'speed': 20,
        'number': 4,
        'time': timedelta(seconds=120),
    }
    pilot.add_lap(lap)

    if not pilot.finished is True:
        raise AssertionError()

    if not pilot.fastest_lap == timedelta(seconds=90):
        raise AssertionError()

    if not pilot.total_laps == 2:
        raise AssertionError()

    if not pilot.speed == 15:
        raise AssertionError()

    if not pilot.time == timedelta(seconds=210):
        raise AssertionError()
