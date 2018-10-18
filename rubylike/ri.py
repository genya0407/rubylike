import copy
import random
from .rubylike import Rubylike

class ri(Rubylike):
    def __init__(self, arraylike):
        self.data = arraylike

    def __iter__(self):
        return iter(self.data)

    def first(self):
        a = self.to_a()
        if len(a) == 0:
            return None
        else:
            return a[0]

    def to_a(self):
        return list(self.data)

    def map(self, func):
        return ri(map(func, self.data))

    def filter(self, func):
        return ri(filter(func, self.data))

    def each(self, func):
        for elem in self:
            func(elem)

    def max(self):
        return self.max_by(lambda x: x)

    def min(self):
        return self.min_by(lambda x: x)

    def max_by(self, func):
        return max(self.to_a(), default=None, key=func)

    def min_by(self, func):
        return min(self.to_a(), default=None, key=func)

    def sort(self):
        return self.sort_by(lambda x: x)

    def sort_by(self, func):
        return ri(sorted(self.to_a(), key=func))

    def reverse(self):
        return ri(reversed(self.to_a()))

    def shuffle(self):
        cp = copy.copy(self.data)
        random.shuffle(cp)
        return ri(cp)

    def sample(self, n=None):
        if n != None and n < 1:
            raise "n must be greater than 1."

        if n == None:
            return random.sample(self.to_a(), 1)[0]
        else:
            return ri(random.sample(self.to_a(), n))