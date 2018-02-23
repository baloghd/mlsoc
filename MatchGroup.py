from abc import ABCMeta, abstractmethod
from Match import *
from typing import *

class MatchGroup(metaclass = ABCMeta):
    def __init__(self, matches: List):
        self.matches = matches

    def __len__(self):
        return len(self.matches)

    @abstractmethod
    def avg(self, total):
        return "%.4f" % round(total/len(self), 4)

    @abstractmethod
    def __getitem__(self, i):
        return self.matches[i]
    
    @abstractmethod
    def calc_totals(self):
        pass

class SoccerMatchGroup(MatchGroup):
    def __init__(self, matches):
        MatchGroup.__init__(self, matches)

    def __len__(self):
        return MatchGroup.__len__(self)

    def __getitem__(self, i):
        return MatchGroup.__getitem__(self, i)

    def avg(self, total):
        return "%.4f" % round(total/len(self), 4)

    def calc_totals(self):
        self.fthg_sum = sum([x.fthg for x in self.matches])
        self.fthg_sum_avg = self.avg(self.fthg_sum)

        self.ftag_sum = sum([x.ftag for x in self.matches])
        self.ftag_sum_avg = self.avg(self.ftag_sum)

        self.hthg_sum = sum([x.hthg for x in self.matches])
        self.hthg_sum_avg = self.avg(self.hthg_sum)

        self.htag_sum = sum([x.htag for x in self.matches])
        self.htag_sum_avg = self.avg(self.htag_sum)

    def calc_RPI(self):
        pass


class BasketBallMatchGroup(MatchGroup):
    pass

class HockeyMatchGroup(MatchGroup):
    pass

class BaseballMatchGroup(MatchGroup):
    pass

class AmericanFootballMatchGroup(MatchGroup):
    pass