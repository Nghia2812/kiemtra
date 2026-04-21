# ================= TO MAU DO THI =================

def greedy_coloring(graph):
    n = len(graph)
    result = [-1] * n  # lưu màu của mỗi đỉnh

    result[0] = 0  # đỉnh đầu tiên màu 0

    for u in range(1, n):
        used = [False] * n

        # kiểm tra các đỉnh kề
        for v in graph[u]:
            if result[v] != -1:
                used[result[v]] = True

        # tìm màu nhỏ nhất chưa dùng
        color = 0
        while used[color]:
            color += 1

        result[u] = color

    return result


# ===== TEST =====
graph = [
    [1, 2],      # đỉnh 0
    [0, 2, 3],   # đỉnh 1
    [0, 1, 3],   # đỉnh 2
    [1, 2]       # đỉnh 3
]

colors = greedy_coloring(graph)

print("Ket qua to mau:")
for i in range(len(colors)):
    print(f"Dinh {i} -> Mau {colors[i]}")