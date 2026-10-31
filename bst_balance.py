import random, math, sys
sys.setrecursionlimit(10000)

class Node:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key); return
        cur = self.root
        while True:
            if key < cur.key:
                if cur.left: cur = cur.left
                else: cur.left = Node(key); return
            elif key > cur.key:
                if cur.right: cur = cur.right
                else: cur.right = Node(key); return
            else:
                return  # dublikat yoxdur

    def search(self, key):
        cur, steps = self.root, 0
        while cur:
            steps += 1
            if key == cur.key: return True, steps
            cur = cur.left if key < cur.key else cur.right
        return False, steps

    def inorder(self, n="root"):
        n = self.root if n == "root" else n
        return self.inorder(n.left) + [n.key] + self.inorder(n.right) if n else []

    def height(self, n="root"):
        n = self.root if n == "root" else n
        return 0 if not n else 1 + max(self.height(n.left), self.height(n.right))

    def balanced(self, n="root"):
        """Hər node üçün |h(sol) - h(sağ)| <= 1 olub-olmadığını yoxlayır"""
        n = self.root if n == "root" else n
        if not n: return True
        return (abs(self.height(n.left) - self.height(n.right)) <= 1
                and self.balanced(n.left) and self.balanced(n.right))

    def rebalance(self):
        """Sıralı siyahıdan yeni balanslı ağac qurur: O(n)"""
        keys = self.inorder()
        def build(lo, hi):
            if lo > hi: return None
            mid = (lo + hi) // 2
            n = Node(keys[mid])
            n.left, n.right = build(lo, mid - 1), build(mid + 1, hi)
            return n
        self.root = build(0, len(keys) - 1)

def build(keys):
    t = BST()
    for k in keys: t.insert(k)
    return t

if __name__ == "__main__":
    n = 1000
    data = list(range(n))
    shuffled = data[:]; random.shuffle(shuffled)

    sorted_t, random_t = build(data), build(shuffled)
    print(f"n = {n}, ideal hündürlük ≈ {math.ceil(math.log2(n + 1))}\n")
    for name, t in [("Sıralı daxiletmə", sorted_t), ("Təsadüfi daxiletmə", random_t)]:
        print(f"{name:20} hündürlük={t.height():4}  "
              f"axtarış(son açar)={t.search(data[-1])[1]:4} addım  balanslı={t.balanced()}")

    sorted_t.rebalance()
    print(f"\nRebalance-dan sonra (sıralı ağac): hündürlük={sorted_t.height()}, "
          f"axtarış={sorted_t.search(data[-1])[1]} addım, balanslı={sorted_t.balanced()}")
