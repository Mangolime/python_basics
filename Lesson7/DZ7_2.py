from abc import ABC, abstractmethod


class Dress(ABC):
    @abstractmethod
    def expend(self):
        pass


class Coat(Dress):
    def __init__(self, title, v):
        self.title = title
        self.v = v

    @property
    def expend(self):
        return self.v / 6.5 + 0.5


class Suit(Dress):
    def __init__(self, title, h):
        self.title = title
        self.h = h

    @property
    def expend(self):
        return 2 * self.h + 0.3


new_coat = Coat("Синее пальто", 52)
new_suit = Suit("Серый костюм", 1.7)
exp_coat = new_coat.expend
exp_suit = new_suit.expend
print(f"Расход ткани на пальто - {exp_coat:.2f} кв. м")
print(f"Расход ткани на костюм - {exp_suit:.2f} кв. м")
print(f"Общий расход ткани - {exp_coat + exp_suit:.2f} кв. м")
