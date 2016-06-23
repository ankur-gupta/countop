class Integer(int):
    counts = {'add': 0, 'sub': 0, 'lt': 0, 'gt': 0}

    @staticmethod
    def reset_counts():
        for key in Integer.counts.keys():
            Integer.counts[key] = 0

    @staticmethod
    def additions():
        return Integer.counts['add']

    def __init__(self, value):
        self.value = int(value)

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.value)

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            self.__class__.counts['add'] += 1
            return self.__class__(self.value + other.value)
        elif isinstance(other, int):
            self.__class__.counts['add'] += 1
            return self.__class__(self.value + other)
        else:
            raise TypeError('unsupported operand type(s) for +: '
                            '{} and {}'.format(self.__class__, type(other)))

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            self.__class__.counts['sub'] += 1
            return self.__class__(self.value - other.value)
        elif isinstance(other, int):
            self.__class__.counts['sub'] += 1
            return self.__class__(self.value - other)
        else:
            raise TypeError('unsupported operand type(s) for -: '
                            '{} and {}'.format(self.__class__, type(other)))

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.__class__.counts['add'] += 1
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.__class__.counts['add'] += 1
            self.value += other
            return self
        else:
            raise TypeError('unsupported operand type(s) for +: '
                            '{} and {}'.format(self.__class__, type(other)))

    def __isub__(self, other):
        if isinstance(other, self.__class__):
            self.__class__.counts['sub'] += 1
            self.value -= other.value
            return self
        elif isinstance(other, int):
            self.__class__.counts['sub'] += 1
            self.value -= other
            return self
        else:
            raise TypeError('unsupported operand type(s) for -: '
                            '{} and {}'.format(self.__class__, type(other)))

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            self.__class__.counts['lt'] += 1
            return self.value < other.value
        elif isinstance(other, (int, float)):
            self.__class__.counts['lt'] += 1
            return self.value < other
        else:
            raise TypeError('unsupported operand type(s) for <: '
                            '{} and {}'.format(self.__class__, type(other)))

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            self.__class__.counts['gt'] += 1
            return self.value > other.value
        elif isinstance(other, (int, float)):
            self.__class__.counts['gt'] += 1
            return self.value > other
        else:
            raise TypeError('unsupported operand type(s) for >: '
                            '{} and {}'.format(self.__class__, type(other)))


