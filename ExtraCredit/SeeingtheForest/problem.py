class Node:
    def __init__(self, data, color='red'):
        self.data = data
        self.color = color
        self.parent = None
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(data=None, color='black')  # Sentinel NIL node
        self.root = self.NIL

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node  # Tree was empty
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'red'
        self.insert_fixup(new_node)

    def insert_fixup(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)
        self.root.color = 'black'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def inorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node != self.NIL:
            self.inorder_traversal(node.left, result)
            result.append(node.data)
            self.inorder_traversal(node.right, result)
        return result
    

    def delete(self, data):
        # Step 1: Find the node containing the data
        node_to_delete = self.find_node(self.root, data)
        if node_to_delete == self.NIL:
            return  # Node not found

        original_color = node_to_delete.color
        if node_to_delete.left == self.NIL:
            x = node_to_delete.right
            self.rb_transplant(node_to_delete, node_to_delete.right)
        elif node_to_delete.right == self.NIL:
            x = node_to_delete.left
            self.rb_transplant(node_to_delete, node_to_delete.left)
        else:
            # Find successor (the smallest node in the right subtree)
            successor = node_to_delete.right
            while successor.left != self.NIL:
                successor = successor.left
            original_color = successor.color
            x = successor.right
            if successor.parent == node_to_delete:
                x.parent = successor
            else:
                self.rb_transplant(successor, successor.right)
                successor.right = node_to_delete.right
                successor.right.parent = successor

            self.rb_transplant(node_to_delete, successor)
            successor.left = node_to_delete.left
            successor.left.parent = successor
            successor.color = node_to_delete.color

        if original_color == 'black':
            self.delete_fixup(x)

    def rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete_fixup(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'black'

    def find_node(self, current, data):
        while current != self.NIL and current.data != data:
            if data < current.data:
                current = current.left
            else:
                current = current.right
        return current
