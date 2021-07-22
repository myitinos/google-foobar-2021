class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = self.right = None

    def _str(self, level=0):
        ret = "  "*level+repr(self.value)+"\n"
        if self.left:
            ret += self.left._str(level+1)
            ret += self.right._str(level+1)
        return ret

    def seek(self, value):
        if self.left and self.right:
            if self.left.value == value or self.right.value == value:
                return self.value
            return self.left.seek(value) or self.right.seek(value)
        return None


class Tree:
    def __init__(self, height):
        nums = list(range(1, 2 ** height))
        self.root = Tree.postorder(height, nums)

    @staticmethod
    def postorder(height, nums):
        if height == 1:
            return Node(nums.pop())
        node = Node(nums.pop())
        node.right = Tree.postorder(height-1, nums)
        node.left = Tree.postorder(height-1, nums)
        return node

    def seek(self, val):
        if val >= self.root.value:
            return -1
        return self.root.seek(val)


def solution(h, q):
    tree = Tree(h)
    return [tree.seek(p) for p in q]


if __name__ == '__main__':
    print(solution(5, [19, 14, 28]))
