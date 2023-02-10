# Program: Test for Even Cycle
# Description:
#   - The graph is undirected and connected
#   - A cycle is even if the number of nodes in the cycle is even

def check_even_cycle(node, path):
    global visited

    if node in path:
        if len(path) % 2 == 0:
            return True
        else:
            return False
    visited.append(node)

    for i in graph[node]:
        if len(path) == 0 or i != path[-1]:
            if check_even_cycle(i, path + [node]):
                return True
    return False


graph = {
    'a': ['b', 'e'],
    'b': ['a', 'c'],
    'c': ['b', 'd', 'e'],
    'd': ['c'],
    'e': ['a', 'c']
}

visited = []
if check_even_cycle('a', []):
    print("Even cycle exists")
else:
    print("Even cycle does not exist")
