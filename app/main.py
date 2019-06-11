import sys

from utils import process_stdin
from models import Pilot


if __name__ == "__main__":
    if sys.stdin:
        process_stdin(sys.stdin, Pilot)
