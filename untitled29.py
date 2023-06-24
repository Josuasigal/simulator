class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
        
    def search(self,key):
        if self.val < key:
            if self.right is None:
                return str(key)+" Tidak ditemukan"
            return self.right.search(key)
        elif self.val > key:
            if self.left is None:
                return str(key)+" Tidak ditemukan"
            return self.left.search(key)
        else:
            print(str(self.val) + ' Ditemukan')
            return True
        
def insert(root,node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
        
print("==============================")
print("------BINARY SEARCH TREE------")
print("==============================")

r = Node(9)
insert(r,Node(1))
insert(r,Node(16))
insert(r,Node(14))
insert(r,Node(18))
insert(r,Node(2))
insert(r,Node(11))
insert(r,Node(7))
insert(r,Node(5))

cari=int(input("Masukan Node yang ingin dicari: "))
print(r.search(cari))
print("===========================")
print("Setelah diturutkan menjadi...")
inorder(r)
