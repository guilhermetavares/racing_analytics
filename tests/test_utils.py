from .utils import format_bool, format_to_timedelta, \
    format_to_int, format_to_float, format_line, process_drivers, \
    process_stdin
from .models import Pilot


def test_models_pilot_print_drivers(data):
    if not len(Pilot.print_drivers(process_drivers(data, Pilot))) == 10:
        raise AssertionError()


def test_utils_process_stdin(capsys, data):
    process_stdin(data, Pilot)
    captured = capsys.readouterr()
    if not 'RESULTADO FINAL' in captured.out:
        raise AssertionError()


def test_utils_pilot_process_drivers(data):
    if not len(process_drivers(data, Pilot).keys()) == 6:
        raise AssertionError()


def test_utils_format_bool():
    if not format_bool(True) == 'SIM':
        raise AssertionError()

    if not format_bool(False) == 'NAO':
        raise AssertionError()


def test_utils_format_to_timedelta():
    value = format_to_timedelta('1:02.852')
    if not value.seconds == 62:
        raise AssertionError()


def test_utils_format_to_int():
    if not format_to_int('1') == 1:
        raise AssertionError()

    if not format_to_int('t') == None:
        raise AssertionError()


def test_utils_format_to_float():
    if not format_to_float('12,2') == 12.2:
        raise AssertionError()


def test_utils_format_line():
    line = '23:49:08.277      038 – F.MASSA                           1		1:02.852                        44,275'
    _, code, _, name, lap, time_, speed = format_line(line)

    if not code == '038':
        raise AssertionError()

    if not name == 'F.MASSA':
        raise AssertionError()

    if not lap == 1:
        raise AssertionError()

    if not time_.seconds == 62:
        raise AssertionError()

    if not speed == 44.275:
        raise AssertionError()

    line = 'NOT A VALID LINE'
    if not len(format_line(line)) == 0:
        raise AssertionError()
