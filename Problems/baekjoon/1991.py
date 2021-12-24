import sys


class Node:
    def __init__(self, val: str, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return self.val


N = int(sys.stdin.readline())

dic = dict()
offset = 65
for i in range(N):
    ch = chr(i + offset)
    dic.update({ch: Node(val=ch)})
dic.update({'.': None})

for i in range(N):
    node, left, right = sys.stdin.readline().split()
    node = dic[node]
    left = dic[left]
    right = dic[right]

    node.left = left
    node.right = right

def preorder(node: Node):
    print(node, end='')
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)

preorder(dic['A'])
print('')

def inorder(node: Node):
    if node.left:
        inorder(node.left)
    print(node, end='')
    if node.right:
        inorder(node.right)

inorder(dic['A'])
print('')

def postorder(node: Node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node, end='')

postorder(dic['A'])
