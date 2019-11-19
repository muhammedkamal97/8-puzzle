
def visualize(path, **kwargs):
    method = kwargs.get('method', None)
    time = kwargs.get('time', None)
    cost = kwargs.get('cost', None)
    depth = kwargs.get('depth', None)

    if method:
        print(f'This is the path for: {method}\n')
        print("----------\n")
    for state in path:
        print(f'{state[0]} | {state[1]} | {state[2]}\n')
        print(f'{state[3]} | {state[4]} | {state[5]}\n')
        print(f'{state[6]} | {state[7]} | {state[8]}\n')
        print("----------\n")

    if time:
        print(f'Elapsed time: {time}\n')
    if cost:
        print(f'Total path cost: {cost}\n')
    if depth:
        print(f'Path depth: {depth}\n')

    print("=============================\n")

