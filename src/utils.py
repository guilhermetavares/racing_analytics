import re
from datetime import timedelta


def format_to_timedelta(value):
    minutes, seconds, microseconds = list(map(int, re.compile('([0-9]+)').findall(value)))
    return timedelta(minutes=minutes, seconds=seconds, microseconds=microseconds)

def format_to_int(value):
    return int(value) if value.isdigit() else None

def format_to_float(value):
    value = re.sub(',', '.', value)
    return float(value)
