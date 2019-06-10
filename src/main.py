import sys
#
# ctn = 1
# for line in sys.stdin:
#     print(ctn, line)
#     ctn += 1
from utils import format_line
from models import Pilot


def process_stdin(data):
    pass


def process_file(filename):
    pass


def process_drivers(data):
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


if __name__ == "__main__":
    if sys.stdin:
        for line in sys.stdin:
            print(format_line(line))
