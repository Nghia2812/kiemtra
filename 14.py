# ================= KNAPSACK XAP XI =================

def knapsack_greedy(weights, values, W):
    n = len(weights)

    # Tạo danh sách (index, ratio)
    items = []
    for i in range(n):
        ratio = values[i] / weights[i]
        items.append((i, ratio))

    # Sắp xếp giảm dần theo ratio
    items.sort(key=lambda x: x[1], reverse=True)

    total_weight = 0
    total_value = 0
    selected = []

    for i, ratio in items:
        if total_weight + weights[i] <= W:
            selected.append(i)
            total_weight += weights[i]
            total_value += values[i]

    return selected, total_weight, total_value


# ===== TEST =====
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5

selected, total_w, total_v = knapsack_greedy(weights, values, W)

print("Vat duoc chon:", selected)
print("Tong trong luong:", total_w)
print("Tong gia tri:", total_v)