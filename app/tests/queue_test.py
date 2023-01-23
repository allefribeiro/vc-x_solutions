import unittest

from app.structures.queue import Queue, DequeueException


class QueueTestCase(unittest.TestCase):
    def test_enqueue_one(self):
        queue = Queue(1)
        assert len(queue) == 1
        assert repr(queue) == '1'

    def test_is_empty(self):
        queue = Queue()
        assert queue.is_empty() is True

        queue.enqueue(1)
        assert queue.is_empty() is False

        queue.dequeue()
        assert queue.is_empty() is True

    def test_size(self):
        queue = Queue()
        assert len(queue) == 0

        queue.enqueue(1)
        assert len(queue) == 1

        queue.dequeue()
        assert len(queue) == 0

    def test_enqueue(self):
        queue = Queue()

        tests = [1, '0', Queue, lambda x: x, {}, [], None]

        for test in tests:
            queue.enqueue(test)

        assert len(tests) == len(queue)

    def test_dequeue_with_initial_queue(self):
        tests = [1, None, [], Queue, 'foo', lambda y: y, {}]
        queue = Queue(tests)

        assert len(queue) == len(tests)

        for _ in tests:
            queue.dequeue()

        assert queue.is_empty() is True

    def test_dequeue(self):
        queue = Queue()

        with self.assertRaises(DequeueException):
            queue.dequeue()

        one = 1
        two = 2

        queue.enqueue(one)
        queue.enqueue(two)

        assert len(queue) == 2

        assert queue.dequeue() == one
        assert queue.dequeue() == two

        assert len(queue) == 0

    def test_queue_as_string(self):
        queue = Queue()

        assert str(queue) == ''

        queue.enqueue(3)
        queue.enqueue(1)
        queue.enqueue(2)

        assert str(queue) == '3 -> 1 -> 2'
