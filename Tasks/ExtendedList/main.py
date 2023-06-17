class ExtendedList(list):
    @property
    def reversed(self):
        return self[::-1]

    R = reversed

    @property
    def first(self):
        return self[0]

    @first.setter
    def first(self, value):
        self[0] = value

    F = first

    @property
    def last(self):
        return self[-1]

    @last.setter
    def last(self, value):
        self[-1] = value

    L = last

    @property
    def size(self):
        return len(self)

    @size.setter
    def size(self, new_size):
        if new_size > len(self):
            empty = [None] * (new_size - len(self))
            self.extend(empty)
        elif new_size < len(self):
            for i in range(len(self) - new_size):
                self.pop()

    S = size
