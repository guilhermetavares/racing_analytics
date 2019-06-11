from datetime import timedelta


def test_models_pilot_init(pilot):

    if not pilot.finished is False:
        raise AssertionError()  # pragma: no cover

    if not pilot.fastest_lap is None:
        raise AssertionError()  # pragma: no cover

    if not len(pilot.laps) == 0:
        raise AssertionError()  # pragma: no cover

    if not str(pilot) == pilot.code:
        raise AssertionError()  # pragma: no cover

    if not pilot.fmt_finished == 'NAO':
        raise AssertionError()  # pragma: no cover


def test_models_pilot_add_lap(pilot):
    lap = {
        'speed': 10,
        'number': 1,
        'time': timedelta(seconds=90),
    }
    pilot.add_lap(lap)

    if not pilot.finished is False:
        raise AssertionError()  # pragma: no cover

    if not pilot.fastest_lap == lap.get('time'):
        raise AssertionError()  # pragma: no cover

    if not pilot.total_laps == 1:
        raise AssertionError()  # pragma: no cover

    if not pilot.speed == lap.get('speed'):
        raise AssertionError()  # pragma: no cover

    if not pilot.time == lap.get('time'):
        raise AssertionError()  # pragma: no cover

    lap = {
        'speed': 20,
        'number': 4,
        'time': timedelta(seconds=120),
    }
    pilot.add_lap(lap)

    if not pilot.finished is True:
        raise AssertionError()  # pragma: no cover

    if not pilot.fastest_lap == timedelta(seconds=90):
        raise AssertionError()  # pragma: no cover

    if not pilot.total_laps == 2:
        raise AssertionError()  # pragma: no cover

    if not pilot.speed == 15:
        raise AssertionError()  # pragma: no cover

    if not pilot.time == timedelta(seconds=210):
        raise AssertionError()  # pragma: no cover
