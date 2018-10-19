import copy
import random
import itertools as it
import functools as fc
from .rubylike import Rubylike

class ri(Rubylike):
    def __init__(self, arraylike):
        self.data = arraylike

    def __iter__(self):
        return iter(self.to_a())

    def to_a(self):
        array = list(self.data)
        self.data = ri(array)
        return array

    def first(self):
        a = self.to_a()
        if len(a) == 0:
            return None
        else:
            return a[0]

    def find(self, func):
        for elem in self:
            if func(elem):
                return elem

    def len(self):
        return len(self.to_a())

    def take(self, n):
        return ri(self.to_a()[:n])

    def takewhile(self, func):
        return ri(it.takewhile(func, self.data))

    def drop(self, n):
        return ri(self.to_a()[n:])

    def dropwhile(self, func):
        return ri(it.dropwhile(func, self.data))

    def map(self, func):
        return ri(map(func, self.data))

    def select(self, func):
        return ri(filter(func, self.data))

    def reject(self, func):
        return self.select(lambda x: not func(x))

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
        cp = self.to_a()
        random.shuffle(cp)
        return ri(cp)

    def sample(self, n=None):
        if n != None and n < 1:
            raise "n must be greater than 1."

        if n == None:
            return random.sample(self.to_a(), 1)[0]
        else:
            return ri(random.sample(self.to_a(), n))

    def all(self, func=None):
        if func == None:
            return all(self.to_a())
        else:
            return all(self.map(func).to_a())

    def any(self, func=None):
        if func == None:
            return any(self.to_a())
        else:
            return any(self.map(func).to_a())

    def reduce(self, func, initializer=None):
        if initializer is None:
            return fc.reduce(func, self.data)
        else:
            return fc.reduce(func, self.data, initializer)
