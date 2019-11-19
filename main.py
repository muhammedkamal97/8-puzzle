from math import sqrt

from state import State
from BFS import breadth_first_search
from DFS import depth_first_search
from A_Star import a_star_search

def successor(state):
    new_states = []
    zero_index = state.index(0)
    # Left
    if (zero_index % 3) - 1 >= 0:
        lst = list(state)
        lst[zero_index], lst[zero_index-1] = lst[zero_index-1], lst[zero_index]
        new_states.append(tuple(lst))
    # Right
    if (zero_index % 3) + 1 < 3:
        lst = list(state)
        lst[zero_index], lst[zero_index + 1] = lst[zero_index + 1], lst[zero_index]
        new_states.append(tuple(lst))
    # Up
    if (zero_index//3) > 0:
        lst = list(state)
        lst[zero_index], lst[zero_index - 3] = lst[zero_index - 3], lst[zero_index]
        new_states.append(tuple(lst))
    # Down
    if (zero_index//3) < 2:
        lst = list(state)
        lst[zero_index], lst[zero_index + 3] = lst[zero_index + 3], lst[zero_index]
        new_states.append(tuple(lst))
    return new_states

def goal_test(state):
    for i in range(len(state)):
        if i != state[i]:
            return False
    return True




def euclidean_distance(x1, y1, x2, y2):
    return sqrt(pow((x1-x2), 2) + pow((y1-y2), 2))

def manhatten_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


if __name__ == "__main__":

    initial_state = [1, 2, 5, 3, 4, 0, 6, 7, 8]
    init_state = State(initial_state)

    # BFS
    result, state = breadth_first_search(init_state, goal_test, successor)
    print(result)
    path = list()
    path.append(state.state)
    while state.parent is not None:
        state = state.parent
        path.append(state.state)

    path.reverse()
    print(path)

    # DFS
    result, state = depth_first_search(init_state, goal_test, successor)
    print(result)
    path = list()
    path.append(state.state)
    while state.parent is not None:
        state = state.parent
        path.append(state.state)

    path.reverse()
    print(path)

    # A* manhatten
    result, state = a_star_search(init_state, goal_test, successor, manhatten_distance)
    print(result)
    path = list()
    path.append(state.state)
    while state.parent is not None:
        state = state.parent
        path.append(state.state)

    path.reverse()
    print(path)


    # A* eucildean
    result, state = a_star_search(init_state, goal_test, successor, euclidean_distance)
    print(result)
    path = list()
    path.append(state.state)
    while state.parent is not None:
        state = state.parent
        path.append(state.state)

    path.reverse()
    print(path)
