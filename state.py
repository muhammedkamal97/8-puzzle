class State:
    def __init__(self, lists, parent=None):
        self._state = tuple(lists)
        self._parent = parent

    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return other.state == self.state

    def __hash__(self):
        return hash(self.state)

    @property
    def state(self):
        return self._state

    @property
    def parent(self):
        return self._parent
