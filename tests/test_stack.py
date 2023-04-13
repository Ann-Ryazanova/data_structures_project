"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Node, Stack


class StackTest(unittest.TestCase):

    def test_Node_init(self):
        n = Node(5, None)
        self.assertEquals(n.data, 5)
        self.assertEquals(n.next_node, None)

    def test_stack_init(self):
        s = Stack()
        self.assertIsNone(s.next_node)
        self.assertIsNone(s.data)
        self.assertIsNone(s.top)

    def test_push(self):
        pass
