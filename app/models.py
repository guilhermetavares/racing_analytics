from functools import reduce


class Pilot(object):

    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.laps = list()
        self.finished = False
        self.fastest_lap = None

    def __repr__(self):
        return f'{self.code}'

    def __str__(self):
        return self.code

    @classmethod
    def print_drivers(self, drivers):
        stdout = list()

        drivers = sorted(drivers.values(), key=lambda pilot: pilot.time)

        fastest_lap = None
        fastest_time = None

        stdout.append('RESULTADO FINAL (*.CSV)')
        stdout.append('POSICAO;PILOTO_CODIGO;PILOTO;TERMINOU_A_PROVA;TEMPO_DE_PROVA;VALOCIDADE_MEDIA;VOLTA_MAIS_RAPIDA;TEMPO_PARA_O_VENCEDOR')

        for ctn, i in enumerate(drivers, 1):
            time_ = i.time

            if fastest_time is None:
                fastest_time = time_

            if fastest_lap is None or i.fastest_lap < fastest_lap[0]:
                fastest_lap = (i.fastest_lap, i.name)

            diff_champion = time_ - fastest_time
            line = [ctn, i, i.name, i.fmt_finished, i.time, i.speed, i.fastest_lap, '+{}'.format(diff_champion)]
            stdout.append(';'.join(map(str, line)))

        stdout.append(f'TOTAL DE PROVA: {fastest_time}')
        stdout.append('VOLTA MAIS RAPIDA: {} {}'.format(fastest_lap[0], fastest_lap[1]))
        return stdout


    def add_lap(self, data):

        if data.get('number') == 4:
            self.finished = True

        if self.fastest_lap is None or data.get('time') < self.fastest_lap:
            self.fastest_lap = data.get('time')

        self.laps.append(data)

    @classmethod
    def _sum(self, lst):
        return reduce(lambda a, b: a + b, lst)

    @classmethod
    def _average(self, lst):
        return self._sum(lst) / len(lst)

    @property
    def fmt_finished(self):
        return 'SIM' if self.finished else 'NAO'

    @property
    def total_laps(self):
        return len(self.laps)

    @property
    def speed(self):
        lst = [item.get('speed') for item in self.laps]
        return self._average(lst)

    @property
    def time(self):
        return self._sum([item.get('time') for item in self.laps])
