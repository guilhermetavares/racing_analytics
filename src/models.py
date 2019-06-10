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

    def add_lap(self, data):

        if data.get('number') == 4:
            self.finished = True

        if self.fastest_lap is None or data.get('time') < self.fastest_lap:
            self.fastest_lap = data.get('time')

        self.laps.append(data)

    def _sum(self, lst):
        return reduce(lambda a, b: a + b, lst)

    def _average(self, lst):
        return self._sum(lst) / len(lst)

    @property
    def fmt_finished(self):
        return 'SIM' if self.finished else 'NAO'

    @property
    def speed(self):
        lst = [item.get('speed') for item in self.laps]
        return self._average(lst)

    @property
    def time(self):
        return self._sum([item.get('time') for item in self.laps])
