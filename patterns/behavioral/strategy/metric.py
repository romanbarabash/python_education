import math


class Metric(object):
    """Abstract class"""

    def distance(self, x, y):
        raise NotImplementedError("Derived classes should implement this.")


class EuclideanMetric(Metric):
    """Calculates distance from origin in R according to Pythagorean distance"""

    def distance(self, x, y):
        return math.sqrt(x * x + y * y)


class ManhattanMetric(Metric):
    """Calculates distance from origin in R according to Manhattan Metric"""

    def distance(self, x, y):
        return abs(x) + abs(y)


class Consumer(Metric):
    """We can use this class to use either of the two metrics"""

    def __init__(self, arg):
        self.metric = arg()

    def distance(self, x, y):
        return self.metric.distance(x, y)


euclid = Consumer(EuclideanMetric)
print(euclid.distance(3, 4))

manhattan = Consumer(ManhattanMetric)
print(manhattan.distance(1, -2))
