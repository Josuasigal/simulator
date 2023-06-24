class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def search(self, key):
        if self.val == key:
            return True
        elif key < self.val:
            if self.left is None:
                return str(key) + " Tidak ditemukan"
            return self.left.search(key)
        elif key > self.val:
            if self.right is None:
                return str(key) + " Tidak ditemukan"
            return self.right.search(key)

    def insert(self, node):
        if self.val > node.val:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val)
        if self.right:
            self.right.inorder()

# Create the root node
r = Node(9)

# Insert nodes
r.insert(Node(1))
r.insert(Node(16))
r.insert(Node(14))
r.insert(Node(18))
r.insert(Node(2))
r.insert(Node(11))
r.insert(Node(7))
r.insert(Node(5))

# Search for a node
cari = int(input("Masukkan Node yang ingin dicari: "))
print(r.search(cari))

# Print the tree in sorted order
print("==========")
print("Setelah diurutkan menjadi:")
r.inorder()
