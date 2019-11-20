import queue
from state import State


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
    max_depth = 0
    while not que.empty():
        state = que.get()
        if state in explored:
            continue

        explored.add(state)
        max_depth = max(max_depth, state.depth)

        if goal_test(state.state):
            return True, state, max_depth

        childs = successor(state.state)
        for ch in childs:
            if ch not in explored:
                que.put(State(list(ch), state))

    return False, None, max_depth
