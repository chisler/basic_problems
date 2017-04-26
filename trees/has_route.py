graph = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"],
    "D": [],
}

# A -> C - yes
# A -> D - no

visited = set()


def dfs(node, end):
    if node in visited:
        return

    if node == end:
        print('There is a way!')
        return

    visited.add(node)
    for v in graph[node]:
        dfs(v, end)

dfs("A", "C")
dfs("A", "D")