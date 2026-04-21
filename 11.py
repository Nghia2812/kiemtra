# ================= AVL TREE =================

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    # ===== Chiều cao =====
    def height(self, n):
        return n.height if n else 0

    # ===== Hệ số cân bằng =====
    def balance(self, n):
        return self.height(n.left) - self.height(n.right) if n else 0

    # ===== Xoay phải =====
    def right_rotate(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    # ===== Xoay trái =====
    def left_rotate(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    # ===== Thêm node =====
    def insert(self, root, key):
        if not root:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        # cập nhật chiều cao
        root.height = 1 + max(self.height(root.left), self.height(root.right))

        # kiểm tra cân bằng
        b = self.balance(root)

        # LL
        if b > 1 and key < root.left.key:
            return self.right_rotate(root)

        # RR
        if b < -1 and key > root.right.key:
            return self.left_rotate(root)

        # LR
        if b > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL
        if b < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # ===== Duyệt inorder =====
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print("Khoa:", root.key)
            self.inorder(root.right)


# ================= MAIN =================
if __name__ == "__main__":
    tree = AVL()
    root = None

    print("Nhap cac so (cach nhau boi dau cach, ket thuc bang -1):")

    # ===== INPUT CHUẨN (KHÔNG LỖI) =====
    try:
        arr = list(map(int, input().split()))
    except:
        print("Nhap sai dinh dang!")
        exit()

    # ===== INSERT =====
    for x in arr:
        if x == -1:
            break
        root = tree.insert(root, x)

    # ===== OUTPUT =====
    print("\nCay AVL (Inorder):")
    tree.inorder(root)