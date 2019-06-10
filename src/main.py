import sys
#
# ctn = 1
# for line in sys.stdin:
#     print(ctn, line)
#     ctn += 1
from utils import format_line
from models import Pilot


def process_stdin(data):
    drivers = process_drivers(data)
    print_drivers(drivers)


def process_file(filename):
    f = open(filename, "r")
    data = f.read()
    drivers = process_drivers(data.split('\n'))
    print_drivers(drivers)


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

    return drivers


def print_drivers(drivers):
    drivers = sorted(drivers.values(), key=lambda pilot: pilot.time)

    fastest_lap = None
    fastest_time = None

    print('\n' * 2)
    print('RESULTADO FINAL')
    print('\n')

    print('POSICAO;PILOTO_CODIGO;PILOTO;TERMINOU_A_PROVA;TEMPO_DE_PROVA;VALOCIDADE_MEDIA;VOLTA_MAIS_RAPIDA;TEMPO_PARA_O_VENCEDOR')

    for ctn, i in enumerate(drivers, 1):
        time_ = i.time

        if fastest_time is None:
            fastest_time = time_

        if fastest_lap is None or i.fastest_lap < fastest_lap[0]:
            fastest_lap = (i.fastest_lap, i.name)

        diff_champion = time_ - fastest_time
        line = [ctn, i, i.name, i.fmt_finished, i.time, i.speed, i.fastest_lap, '+{}'.format(diff_champion)]
        print(';'.join(map(str, line)))

    print('\n' * 1)
    print('TOTAL DE PROVA:', fastest_time)
    print('VOLTA MAIS RAPIDA:', fastest_lap[0], fastest_lap[1])

if __name__ == "__main__":
    if sys.stdin:
        process_stdin(sys.stdin)
