# Basic TreeNode class for BST
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_tree(self.root, value)

    def _search_tree(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_tree(node.left, value)
        else:
            return self._search_tree(node.right, value)

    def delete(self, value):
        self.root = self._delete_node(self.root, value)

    def _delete_node(self, node, value):
        if not node:
            return node

        if value < node.value:
            node.left = self._delete_node(node.left, value)
        elif value > node.value:
            node.right = self._delete_node(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            successor = self._min_value_node(node.right)
            node.value = successor.value
            node.right = self._delete_node(node.right, successor.value)

        return node

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def inorder_traversal(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if not node:
            return []
        return self._inorder(node.left) + [node.value] + self._inorder(node.right)


class RedBlackTree:
    RED = True
    BLACK = False

    class Node:
        def __init__(self, value, color=True):
            self.value = value
            self.color = color
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)
        self.root.color = self.BLACK

    def _insert(self, node, value):
        if node is None:
            return self.Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)

        if self._is_red_color(node.right) and not self._is_red_color(node.left):
            node = self._r_rotate(node)
        if self._is_red_color(node.left) and self._is_red_color(node.left.left):
            node = self._l_rotate(node)
        if self._is_red_color(node.left) and self._is_red_color(node.right):
            self._change_colors(node)

        return node

    def _is_red_color(self, node):
        return node is not None and node.color == self.RED

    def _l_rotate(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = self.RED
        return x

    def _r_rotate(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = self.RED
        return x

    def _change_colors(self, node):
        node.color = not node.color
        node.left.color = not node.left.color
        node.right.color = not node.right.color

    def search(self, value):
        return self._search_tree(self.root, value)

    def _search_tree(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_tree(node.left, value)
        else:
            return self._search_tree(node.right, value)


class AVLTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if not node:
            return self.Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        return self._rebalance(node, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if not node:
            return node

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._rebalance(node)

    def _rebalance(self, node, value=None):
        balance = self._get_balance(node)

        if balance > 1:
            if self._get_balance(node.left) >= 0:
                return self._r_rotate(node)
            else:
                node.left = self._l_rotate(node.left)
                return self._r_rotate(node)

        if balance < -1:
            if self._get_balance(node.right) <= 0:
                return self._l_rotate(node)
            else:
                node.right = self._r_rotate(node.right)
                return self._l_rotate(node)

        return node

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right)

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def _l_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _r_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x

    def search(self, value):
        return self._search_tree(self.root, value)

    def _search_tree(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_tree(node.left, value)
        else:
            return self._search_tree(node.right, value)


# Sample Test Cases
if __name__ == "__main__":
    print("--- Binary Search Tree ---")
    bst = BinarySearchTree()
    for v in [5, 3, 7, 2, 4, 6, 8]:
        bst.insert(v)
    print("Inorder before delete:", bst.inorder_traversal())
    bst.delete(3)
    print("After deleting 3:", bst.inorder_traversal())

    print("--- AVL Tree ---")
    avl = AVLTree()
    for v in [5, 3, 7, 2, 4, 6, 8]:
        avl.insert(v)
    avl.delete(3)
    print("Search 5:", avl.search(5))
    print("Search 10:", avl.search(10))

    print("--- Red-Black Tree ---")
    rbt = RedBlackTree()
    for v in [5, 3, 7, 2, 4, 6, 8]:
        rbt.insert(v)
    print("Search 5:", rbt.search(5))
    print("Search 10:", rbt.search(10))
