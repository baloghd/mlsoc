from abc import ABCMeta, abstractmethod
import datetime
from typing import *

MatchResult = Tuple[int, int]

class Match(metaclass = ABCMeta):
    """
    Az abstract base class az összes *sportnév*Match child classnak
    """ 
    def __init__(self, date, home, away, comptype = "league"):
        self.date = date
        self.home = home
        self.away = away
        self.comptype = comptype

    def __str__(self):
        return str(self.__dict__)

    def comparison(results: MatchResult) -> str:
        if results[0] > results[1]:
            return "H"
        elif results[0] < results[1]:
            return "A"
        else:
            return "D"

    def result_over(n: int, results: MatchResult) -> bool:
        return True if sum(results) > n else False

    @abstractmethod
    def add_results(self, fthg: int, ftag: int):
        self.fthg = fthg
        self.ftag = ftag
        
    @abstractmethod
    def create_binary_tags(self):
        pass

    @abstractmethod
    def create_result_tags(self):
        pass

    @abstractmethod
    def create_tags(self):
        self.create_result_tags()
        self.create_binary_tags()
        

class SoccerMatch(Match):
    def __init__(self, date, home, away, comptype):
        Match.__init__(self, date, home, away, comptype)
        
    def add_results(self, hthg: int, htag: int, fthg: int, ftag: int):
        self.hthg = hthg
        self.htag = htag
        self.fthg = fthg
        self.ftag = ftag

        self.ftr_tuple = (self.fthg, self.ftag)
        self.htr_tuple = (self.hthg, self.htag)
      
    def create_binary_tags(self):
        self.tags = {'btts': "Y" if (self.fthg > 0) and (self.ftag > 0) else "N",
                     'ft over 1.5': "Y" if Match.result_over(1.5, self.ftr_tuple) else "N",
                     'ft over 2.5': "Y" if Match.result_over(2.5, self.ftr_tuple) else "N",
                     'ft over 3.5': "Y" if Match.result_over(3.5, self.ftr_tuple) else "N",
                     'ht over 1.5': "Y" if Match.result_over(1.5, self.htr_tuple) else "N", 
                     'ht over 2.5': "Y" if Match.result_over(2.5, self.htr_tuple) else "N",
                     'ht over 3.5': "Y" if Match.result_over(3.5, self.htr_tuple) else "N"}
    
    def create_result_tags(self):
        """for_what nem implementálva"""
        self.ftr = Match.comparison(self.ftr_tuple)
        self.htr = Match.comparison(self.htr_tuple)

    def create_tags(self):
        Match.create_tags(self)

class BasketballMatch(Match):
    def __init__(self, date, home, away, comptype):
        Match.__init__(self, date, home, away, comptype)

    def add_results(self, q1hg, q1ag, h1hg, h1ag, fthg, ftag):
        pass

class HockeyMatch(Match):
    def __init__(self, date, home, away, comptype):
        Match.__init__(self, date, home, away, comptype)

class BaseballMatch(Match):
    def __init__(self, date, home, away, comptype):
        Match.__init__(self, date, home, away, comptype)

class AmericanFootballMatch(Match):
    def __init__(self, date, home, away, comptype):
        Match.__init__(self, date, home, away, comptype)