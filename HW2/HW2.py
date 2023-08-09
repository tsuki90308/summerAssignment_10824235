class Node:

    def __init__(self, data):
        self.left = None  #左节点
        self.right = None #右节点
        self.data = data  #值

    def insert(self, data):
    # 将新值与父节点进行比较
        if self.data:  # 非空
            if data < self.data:            #新值较小，放左边
                if self.left is None:       #若空，则新建插入节点
                    self.left = Node(data)
                else:                       #否则，递归往下查找
                    self.left.insert(data)
            elif data > self.data:          #新值较大，放右边
                if self.right is None:      #若空，则新建插入节点
                    self.right = Node(data)
                else:                       #否则，递归往下查找
                    self.right.insert(data)
        else:
            self.data = data                

    # 打印这棵树，中序遍历
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Inorder
# Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

# Preorder
# Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

# Postorder
# Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res




root1 = Node(10) #创建节点
print("創建根:")
root1.PrintTree()


# 使用insert方法添加节点
root2 = Node(12)
root2.insert(6)
root2.insert(14)
root2.insert(3)
print("插入到樹中:")
root2.PrintTree()


root3 = Node(27)
root3.insert(14)
root3.insert(35)
root3.insert(10)
root3.insert(19)
root3.insert(31)
root3.insert(42)
print("順序遍歷:")
print(root3.inorderTraversal(root3))


root4 = Node(27)
root4.insert(14)
root4.insert(35)
root4.insert(10)
root4.insert(19)
root4.insert(31)
root4.insert(42)
print("預購遍歷:")
print(root4.PreorderTraversal(root4))

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print("後序遍歷:")
print(root.PostorderTraversal(root))