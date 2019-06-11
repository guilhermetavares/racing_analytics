import pytest

from datetime import timedelta
from .utils import format_bool, format_to_timedelta, \
    format_to_int, format_to_float, format_line, process_drivers, \
    process_stdin
from .models import Pilot


def test_models_pilot_print_drivers(data):
    assert len(Pilot.print_drivers(process_drivers(data, Pilot))) == 10


def test_utils_process_stdin(capsys, data):
    process_stdin(data, Pilot)
    captured = capsys.readouterr()
    assert 'RESULTADO FINAL' in captured.out


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
