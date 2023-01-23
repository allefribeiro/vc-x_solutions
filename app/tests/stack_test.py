import unittest

from app.structures.stack import Stack, PopException


class StackTestCase(unittest.TestCase):

    def test_is_empty(self):
        stack = Stack()
        assert stack.is_empty() is True

        stack.push(1)
        assert stack.is_empty() is False

        stack.pop()
        assert stack.is_empty() is True

    def test_size(self):
        stack = Stack()
        assert len(stack) == 0

        stack.push(1)
        assert len(stack) == 1

        stack.pop()
        assert len(stack) == 0

    def test_push_one(self):
        stack = Stack(lambda z: z)
        assert len(stack) == 1

    def test_push_items(self):
        stack = Stack()

        tests = [1, '0', Stack, lambda x: x, {}, [], None]

        for test in tests:
            stack.push(test)

        assert len(tests) == len(stack)

    def test_pop_items_with_initial_stack(self):
        tests = [1, '0', Stack, lambda x: x, {}, [], None]

        stack = Stack(tests)

        assert len(stack) == len(tests)

        for _ in tests:
            stack.pop()

        assert stack.is_empty() is True

    def test_pop_items(self):
        stack = Stack()

        with self.assertRaises(PopException):
            stack.pop()

        one = 1
        two = 2

        stack.push(one)
        stack.push(two)

        assert len(stack) == 2

        assert stack.pop() == two
        assert stack.pop() == one

        assert len(stack) == 0

    def test_stack_as_string(self):
        stack = Stack()

        assert str(stack) == ''

        stack.push(3)
        stack.push(1)
        stack.push(2)

        assert repr(stack) == '2 -> 1 -> 3'

    def test_pop_all(self):
        tests = [1, '0', Stack, lambda x: x, {}, [], None]
        stack = Stack(tests)

        assert len(stack) == len(tests)

        stack.pop_all()

        assert stack.is_empty() is True
