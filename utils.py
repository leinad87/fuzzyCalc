class FloatRange:
    def __init__(self, start, end, steps):
        self.start = start
        self.end = end
        self.gap = float(end-start)/steps

    def __iter__(self):
        return self

    def next(self):
        if self.start < self.end:
            next_value = self.start
            self.start += self.gap
            return next_value
        else:
            raise StopIteration()
