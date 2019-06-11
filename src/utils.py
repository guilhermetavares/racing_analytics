import re
from datetime import timedelta


def process_stdin(data, Pilot):
    drivers = process_drivers(data, Pilot)
    print('\n'.join(Pilot.print_drivers(drivers)))


def process_drivers(data, Pilot):
    drivers = dict()

    for line in data:
        item = format_line(line)

        if len(item) == 0:
            continue

        date, code, _, name, lap, time_, speed = item
        driver = drivers.get(code, None)

        if driver is None:
            driver = Pilot(code=code, name=name)
            drivers.update({code: driver})

        driver.add_lap({
            'speed': speed,
            'number': lap,
            'time': time_,
        })

    return drivers


def format_bool(value):
    return 'SIM' if value else 'NAO'


def format_to_timedelta(value):
    minutes, seconds, microseconds = list(map(int, re.compile('([0-9]+)').findall(value)))
    return timedelta(minutes=minutes, seconds=seconds, microseconds=microseconds)


def format_to_int(value):
    return int(value) if value.isdigit() else None


def format_to_float(value):
    value = re.sub(',', '.', value)
    return float(value)


def format_line(line):
    res = re.sub('[ ]', ' ', line).split()

    try:
        date, code, _, name, lap, time_, speed = res

        lap = format_to_int(lap)
        speed = format_to_float(speed)
        time_ = format_to_timedelta(time_)

        return [date, code, _, name, lap, time_, speed]

    except ValueError:
        return []
