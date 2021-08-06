#!/usr/bin/python
# -*- coding: utf-8 -*-


import queue


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def get_element(self):
        """return node.element"""
        return self.val

    def dict_form(self):
        """return node as dict form"""
        dict_set = {
            "element": self.val,
            "left": self.left,
            "right": self.right,
        }
        return dict_set

    def __str__(self):
        """when print a node , print it's element"""
        return str(self.val)


class CreateTree:
    def __init__(self):
        self.root = None

    def recursion(self, node, new_node):
        if node.left is None:
            node.left = new_node
            return

        if node.right is None:
            node.right = new_node
            return

        self.recursion(node.left, new_node)
        self.recursion(node.right, new_node)

    # def construct(self, li=None):
    #         if not li:
    #             return None
    #         tl = []
    #         for i in li:
    #             if i is None:
    #                 tl.append(None)
    #             else:
    #                 tl.append(TreeNode(i))
    #         for idx in range(len(li) / 2):
    #             if idx * 2 + 1 < len(tl) and tl[idx * 2 + 1]:
    #                 tl[idx].left = tl[idx * 2 + 1]
    #
    #             if idx * 2 + 2 < len(tl) and tl[idx * 2 + 2]:
    #                 tl[idx].right = tl[idx * 2 + 2]
    #         self.root = tl[0]

    def create_tree(self, list_):
        self.root = TreeNode(list_[0])
        for elem in list_[1:]:
            new_node = TreeNode(elem)
            # self.add_node(elem)
            self.recursion(self.root, new_node)


class PrintTree:
    def pre_order(self, root):
        if root is None:
            return
        print(root.val)
        self.pre_order(root.left)
        self.pre_order(root.right)

    def middle_order(self, root):
        if root is None:
            return
        self.middle_order(root.left)
        print(root.val)
        self.middle_order(root.right)

    def post_order(self, root):
        if root is None:
            return
        self.post_order(root.left)
        self.pre_order(root.right)
        print(root.val)

    @staticmethod
    def level_order(root):
        bak_list = [root]

        while bak_list:
            tmp = []
            for node in bak_list:
                print(node.val)

                if node.left is not None:
                    tmp.append(node.left)

                if node.right is not None:
                    tmp.append(node.right)

            bak_list = tmp


if __name__ == '__main__':
    obj = CreateTree()
    obj.create_tree([1, 2, 3, 4, 5])