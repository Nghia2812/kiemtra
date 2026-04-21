import os

class Node:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, word, meaning):
        # 1. Thực hiện chèn BST thông thường
        if not root:
            return Node(word, meaning)
        if word < root.word:
            root.left = self.insert(root.left, word, meaning)
        elif word > root.word:
            root.right = self.insert(root.right, word, meaning)
        else:
            root.meaning = meaning # Cập nhật nghĩa nếu từ đã tồn tại
            return root

        # 2. Cập nhật chiều cao
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Kiểm tra cân bằng và thực hiện các phép quay
        balance = self.get_balance(root)

        # Case LL
        if balance > 1 and word < root.left.word:
            return self.right_rotate(root)
        # Case RR
        if balance < -1 and word > root.right.word:
            return self.left_rotate(root)
        # Case LR
        if balance > 1 and word > root.left.word:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Case RL
        if balance < -1 and word < root.right.word:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, root, word):
        if not root:
            return root

        if word < root.word:
            root.left = self.delete(root.left, word)
        elif word > root.word:
            root.right = self.delete(root.right, word)
        else:
            if not root.left or not root.right:
                temp = root.left if root.left else root.right
                root = temp
            else:
                temp = self.min_value_node(root.right)
                root.word = temp.word
                root.meaning = temp.meaning
                root.right = self.delete(root.right, temp.word)

        if not root:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def search(self, root, word):
        curr = root
        while curr:
            if word == curr.word:
                return curr
            curr = curr.left if word < curr.word else curr.right
        return None

    def export_all(self, root, file):
        if root:
            self.export_all(root.left, file)
            file.write(f"{root.word},{root.meaning}\n")
            self.export_all(root.right, file)

# --- Chuông trình chính ---
def main():
    tree = AVLTree()
    root = None
    
    while True:
        print("\n===== TU DIEN ANH-VIET (AVL PYTHON) =====")
        print("1. Them tu moi")
        print("2. Tim nghia cua tu (Xuat file ketqua.txt)")
        print("3. Xoa mot tu")
        print("4. Xuat toan bo tu dien (tudien_xuat.txt)")
        print("0. Thoat")
        
        choice = input("Chon chuc nang: ")

        if choice == '1':
            data = input("Nhap 'Tu,Nghia': ")
            if ',' in data:
                w, m = map(str.strip, data.split(',', 1))
                root = tree.insert(root, w, m)
                print(f"Da them: {w}")
            else:
                print("Dinh dang sai! Vui long nhap theo dang: Tu,Nghia")

        elif choice == '2':
            w = input("Nhap tu can tim: ").strip()
            node = tree.search(root, w)
            if node:
                print(f"Tim thay: {node.word} -> {node.meaning}")
                with open("ketqua.txt", "a", encoding="utf-8") as f:
                    f.write(f"{node.word},{node.meaning}\n")
            else:
                print("Khong tim thay!")

        elif choice == '3':
            w = input("Nhap tu can xoa: ").strip()
            root = tree.delete(root, w)
            print(f"Da xoa (neu co) tu: {w}")

        elif choice == '4':
            with open("tudien_xuat.txt", "w", encoding="utf-8") as f:
                tree.export_all(root, f)
            print("Da xuat toan bo ra file tudien_xuat.txt")

        elif choice == '0':
            break
        else:
            print("Lua chon khong hop le!")

if __name__ == "__main__":
    main()