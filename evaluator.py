import math


class Evaluator:
    def __init__(self, root):
        self.root = root
        self.ans = self.eval(root)
        self.traversal = []
        self.inorder(root)

    def eval(self, node):
        if not node:
            return None
        if node.type == "NUM":
            return node.value
        elif node.type == "NEG":
            return -1 * self.eval(node.down)
        elif node.type == "SIN":
            return math.sin(self.eval(node.down))
        elif node.type == "COS":
            return math.cos(self.eval(node.down))
        elif node.type == "TAN":
            return math.tan(self.eval(node.down))
        elif node.type == "EXP":
            return self.eval(node.left) ** self.eval(node.right)
        elif node.type == "MUL":
            return self.eval(node.left) * self.eval(node.right)
        elif node.type == "DIV":
            return self.eval(node.left) / self.eval(node.right)
        elif node.type == "ADD":
            return self.eval(node.left) + self.eval(node.right)
        elif node.type == "SUB":
            return self.eval(node.left) - self.eval(node.right)

    def inorder(self, node):
        if not node:
            return
        if node.left:
            self.inorder(node.left)
        if node.down:
            self.inorder(node.down)
        if node.value:
            self.traversal.append(node.value)
        else:
            self.traversal.append(str(node.type))
        if node.right:
            self.inorder(node.right)
