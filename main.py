from BFS import breadth_first_search, State


def successor(state):
    new_states = []
    zero_index = state.index(0)
    if (zero_index % 3) - 1 >= 0:
        lst = list(state)
        lst[zero_index], lst[zero_index-1] = lst[zero_index-1], lst[zero_index]
        new_states.append(tuple(lst))
    if (zero_index % 3) + 1 < 3:
        lst = list(state)
        lst[zero_index], lst[zero_index + 1] = lst[zero_index + 1], lst[zero_index]
        new_states.append(tuple(lst))
    if (zero_index//3) > 0:
        lst = list(state)
        lst[zero_index], lst[zero_index - 3] = lst[zero_index - 3], lst[zero_index]
        new_states.append(tuple(lst))
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


if __name__ == "__main__":
    initial_state = [1, 2, 5, 3, 4, 0, 6, 7, 8]
    init_state = State(initial_state)
    result, state = breadth_first_search(init_state, goal_test, successor)
    print(result)
    path = list()
    path.append(state.state)
    while state.parent is not None:
        state = state.parent
        path.append(state.state)

    path.reverse()
    print(path)