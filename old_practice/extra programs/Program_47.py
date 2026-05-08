# Define a class with a generator which can iterate the numbers, which are divisible by
# 7, between a given range 0 and n.
# Date : 09/03/2026
# Author : Nikhil


class DivisibleBySeven:
    def __init__(self,n):
        self.n = n

def generate_divisible_by_seven(self):

    for num in range(self.n + 1):
        if num%7 == 0:
            yield num


class DivisibleBySeven:
    def __init__(self,n):
        self.n = n

    def generate_divisible_by_seven(self):
        for num in range(self.n + 1):
            if num%7 == 0:
                yield num