# -*- coding: utf-8 -*-

""" AVL Module

Defines AVL tree class and related functions.
"""

class AVL:
    """AVL main class."""
    def __init__(self, key, left, right, bal):
        self.key = key
        self.left = left
        self.right = right
        self.bal = bal
