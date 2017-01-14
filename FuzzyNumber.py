from utils import FloatRange


class FuzzyNumber:
    def __init__(self, points):
        self.data = points

    def __add__(self, other):
        minimum = self.min() + other.min()
        maximum = self.max() + other.max()
        new_data = {}
        for z in FloatRange(minimum, maximum, 1000):
            pz = 0
            for a in self.iterator():
                b = z - a
                pz = max(pz, min(self.get_probability(a), other.get_probability(b)))
            new_data[round(z, 3)] = round(pz, 3)
        return FuzzyNumber(new_data)

    def __sub__(self, other):
        minimum = self.min() - other.max()
        maximum = self.max() - other.min()
        new_data = {}
        for z in FloatRange(minimum, maximum, 1000):
            pz = 0
            for a in self.iterator():
                b = -z + a
                pz = max(pz, min(self.get_probability(a), other.get_probability(b)))
            new_data[round(z, 3)] = round(pz, 3)
        return FuzzyNumber(new_data)

    def __mul__(self, other):
        minimum = self.min() * other.min()
        maximum = self.max() * other.max()
        new_data = {}
        for z in FloatRange(minimum, maximum, 1000):
            pz = 0
            for a in self.iterator():
                if a == 0:
                    continue
                b = z / a
                pz = max(pz, min(self.get_probability(a), other.get_probability(b)))
            new_data[round(z, 3)] = round(pz, 3)
        return FuzzyNumber(new_data)

    def __div__(self, other):
        minimum = self.min() / (other.max() if other.max() != 0 else -0.1)
        maximum = self.max() / (other.min() if other.min() > 0 else 0.1)

        new_data = {}
        for z in FloatRange(minimum, maximum, 1000):
            pz = 0
            for a in self.iterator():
                if z == 0:
                    continue
                b = float(a) / z
                pz = max(pz, min(self.get_probability(a), other.get_probability(b)))
            new_data[round(z, 3)] = round(pz, 3)
        return FuzzyNumber(new_data)

    def get_probability(self, x):
        next_pos = float('inf')
        prev = float('-inf')
        for va, pa in self.data.items():
            if va == x:
                return pa
            else:
                prev = va if x > va > prev else prev
                next_pos = va if x < va < next_pos else next_pos

        if next_pos == float('inf') or prev == float('-inf'):
            return 0

        m = (self.data[next_pos] - self.data[prev]) / float(next_pos - prev)
        return m * (x - prev) + self.data[prev]

    def min(self):
        return float(min(self.data.keys()))

    def max(self):
        return float(max(self.data.keys()))

    def iterator(self):
        maximum = float(max(self.data.keys()))
        minimum = float(min(self.data.keys()))
        step = 0.5
        while minimum - step < maximum:
            yield minimum
            minimum += step

    def __str__(self):
        return self.data.items().__str__()

    def xs(self):
        return sorted(self.data.keys())

    def ys(self):
        return [self.data[i] for i in sorted(self.data.keys())]


class TrapNumber(FuzzyNumber):
    def __init__(self, a, b, c, d):
        FuzzyNumber.__init__(self, {a: 0, b: 1, c: 1, d: 0})
