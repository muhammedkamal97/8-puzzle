from math import sqrt
import time

from state import State
from visualizer import visualize
from game.puzzle import Puzzle
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
    BFS_time = time.time()
    result, state, BFS_max_depth = breadth_first_search(init_state, goal_test, successor)
    BFS_time = time.time() - BFS_time
    print(result)
    path = list()
    path.append(state.state)
    while state.parent is not None:
        state = state.parent
        path.append(state.state)

    path.reverse()
    visualize(path, method='BFS')

    puzzle = Puzzle(path, "BFS")
    puzzle.initialization()

    # DFS
    DFS_time = time.time()
    result, state, DFS_max_depth = depth_first_search(init_state, goal_test, successor)
    DFS_time = time.time() - DFS_time
    print(result)
    path = list()
    path.append(state.state)
    while state.parent is not None:
        state = state.parent
        path.append(state.state)

    path.reverse()
    visualize(path, method='DFS')

    puzzle = Puzzle(path, "DFS")
    puzzle.initialization()

    # A* manhattan
    A_start_1_time = time.time()
    result, state, A_star_1_max_depth = a_star_search(init_state, goal_test, successor, manhatten_distance)
    A_start_1_time = time.time() - A_start_1_time
    print(result)
    path = list()
    path.append(state.state)
    while state.parent is not None:
        state = state.parent
        path.append(state.state)

    path.reverse()

    visualize(path, method='A* using Manhattan')
    puzzle = Puzzle(path, "A* using Manhattan")
    puzzle.initialization()

    # A* euclidean
    A_start_2_time = time.time()
    result, state, A_star_2_max_depth = a_star_search(init_state, goal_test, successor, euclidean_distance)
    A_start_2_time = time.time() - A_start_2_time
    print(result)
    path = list()
    path.append(state.state)
    while state.parent is not None:
        state = state.parent
        path.append(state.state)

    path.reverse()
    visualize(path, method='A* using euclidean')
    puzzle = Puzzle(path, "A* using euclidean")
    puzzle.initialization()

    print("BFS time: ", BFS_time, " BFS max depth: ", BFS_max_depth)
    print("DFS time: ", DFS_time, " DFS max depth: ", DFS_max_depth)
    print("A*(manhattan distance) time: ", A_start_1_time, " A*(manhattan distance) max depth: ", A_star_1_max_depth)
    print("A*(euclidean distance) time: ", A_start_2_time, " A*(manhattan distance) max depth: ", A_star_2_max_depth)

