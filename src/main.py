import sys
#
# ctn = 1
# for line in sys.stdin:
#     print(ctn, line)
#     ctn += 1
from utils import process_drivers
from models import Pilot


def process_stdin(data):
    drivers = process_drivers(data, Pilot)
    print('\n'.join(Pilot.print_drivers(drivers)))


if __name__ == "__main__":
    if sys.stdin:
        process_stdin(sys.stdin)
