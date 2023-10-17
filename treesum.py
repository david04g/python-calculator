class Tree:
    def __init__(self, value='', left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# generate a tree from a list of items (data)
def build_tree(data, index):
    t = None
    if index < len(data):
        left = build_tree(data, index*2+1)
        right = build_tree(data, index*2+2)
        t = Tree(data[index], left, right)
    return t

# recursively traverse through all nodes in a tree and return the sum
def find_sum(tree):
    running_total = tree.value
    if tree.left == None:
        return running_total
    if tree.left != None:
        running_total+=find_sum(tree.left)
    if tree.right == None:
        return running_total
    if tree.right != None:
        running_total+=find_sum(tree.right)
    return running_total


if __name__ == '__main__':
    data = [1,2,7,4,8,6,5]
    t = build_tree(data, 0)
    # find the sum
    s = find_sum(t)
    assert s == 33