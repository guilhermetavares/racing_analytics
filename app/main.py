import sys

from utils import process_stdin
from models import Pilot


def run_data(data):
    if data:
        process_stdin(data, Pilot)


if __name__ == "__main__":
    run_data(sys.stdin)  # pragma: no cover
