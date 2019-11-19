import queue


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


def breadth_first_search(initial_state, goal_test, successor):
    """
    Parameters:
    initial_state (State): initial state
    goal_test (tuple): goal test
    successor (function): function return list of tuples each tuple indicate successor state
    Returns:
    result (boolean): indicate the goal found or not
    goal (State): state of goal
    """
    que = queue.Queue()
    que.put(initial_state)
    explored = set()
    while not que.empty():
        state = que.get()
        if state in explored:
            continue

        explored.add(state)

        if goal_test(state.state):
            return True, state

        childs = successor(state.state)
        for ch in childs:
            if ch not in explored:
                que.put(State(list(ch), state))

    return False, None
