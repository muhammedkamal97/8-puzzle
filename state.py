class State:
    def __init__(self, lists, parent=None, g_value=0, h_value=0):
        self._state = tuple(lists)
        self._parent = parent
        self._f_value = h_value + g_value
        self._g_value = g_value
        self._h_value = h_value

    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return other._state == self._state

    def __hash__(self):
        return hash(self._state)

    def __lt__(self, other):
        return self.f_value < other.f_value

    def __gt__(self, other):
        return self.f_value > other.f_value

    def __ge__(self, other):
        return self.f_value >= other.f_value

    @property
    def state(self):
        return self._state

    @property
    def parent(self):
        return self._parent

    @property
    def f_value(self):
        return self._f_value

    @property
    def g_value(self):
        return self._g_value

    @property
    def h_value(self):
        return self._h_value

    def get_coordinates(self, i):
        y = int((i-1) / 3)
        x = (i-1) % 3
        return x, y

    def set_h_value(self, get_distance):
        h_value = 0
        for i in range(0, 9):
            if self._state[i] != 0:
                h_value = h_value + get_distance(*self.get_coordinates(i), *self.get_coordinates(self._state[i]))
        self._h_value = h_value
        self._f_value = self.g_value + h_value

    def set_g_value(self, g):
        self._g_value = g
        self._f_value = self.h_value + g

