# ================= TSP XAP XI =================

import sys

# ===== TIM MST (PRIM) =====
def prim(graph):
    n = len(graph)
    selected = [False] * n
    parent = [-1] * n
    key = [sys.maxsize] * n

    key[0] = 0

    for _ in range(n):
        u = -1
        min_val = sys.maxsize

        for i in range(n):
            if not selected[i] and key[i] < min_val:
                min_val = key[i]
                u = i

        selected[u] = True

        for v in range(n):
            if graph[u][v] != 0 and not selected[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    return parent


# ===== TAO DANH SACH KE TU MST =====
def build_tree(parent):
    tree = {}
    for i in range(len(parent)):
        tree[i] = []

    for i in range(1, len(parent)):
        tree[parent[i]].append(i)
        tree[i].append(parent[i])

    return tree


# ===== DFS =====
def dfs(tree, start, visited, path):
    visited[start] = True
    path.append(start)

    for v in tree[start]:
        if not visited[v]:
            dfs(tree, v, visited, path)


# ===== TSP XAP XI =====
def tsp_approx(graph):
    parent = prim(graph)
    tree = build_tree(parent)

    visited = [False] * len(graph)
    path = []

    dfs(tree, 0, visited, path)

    path.append(0)  # quay ve diem dau

    return path


# ===== TEST =====
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path = tsp_approx(graph)

print("Duong di xap xi:")
print(" -> ".join(map(str, path)))