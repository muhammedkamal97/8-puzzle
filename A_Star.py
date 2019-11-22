import heapq;
from math import sqrt

from state import State


def a_star_search(initial_state, goal_test, successor, get_distance):
    """
    Parameters:
    initial_state (State): initial state
    goal_test (tuple): goal test
    successor (function): function return list of tuples each tuple indicate successor state
    Returns:
    result (boolean): indicate the goal found or not
    goal (State): state of goal
    """


    initial_state.set_h_value(get_distance)
    heap = []
    heapq.heappush(heap, initial_state)
    explored = set()
    max_depth = 0
    while heap:
        state = heapq.heappop(heap)
        if state in explored:
            continue

        explored.add(state)
        max_depth = max(max_depth, state.depth)
        if goal_test(state.state):
            return True, state, max_depth, len(explored)

        children = successor(state.state)

        for ch in children:
            ch = State(list(ch), state)
            ch.set_g_value(state.g_value + 1)
            ch.set_h_value(get_distance)
            if ch not in explored:
                heapq.heappush(heap, ch)

    return False, None, max_depth, len(explored)
