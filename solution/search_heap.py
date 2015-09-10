"""
    search heap file for AI Homework 1 solution

    Authors:
        Ryan Baker
        Matthew Beaulieu
        Anthony Romeo
"""
import heapq


class SearchHeap(object):
    """
        Class to handle storing and retrieving nodes in order of the eval_fn

        :param: initial - the list of items to initialize with
        :param: eval_fn - the function to determine which node to pop next
    """

    def __init__(self, initial=None, g_func=None, h_func=None, goal=None):
        self.key = lambda node: g_func(node) + h_func(node.position,
                                                      node.direction,
                                                      goal)
        if initial is not None:
            self._data = [(self.key(item), item) for item in initial]
            heapq.heapify(self._data)
        else:
            self._data = []

    def push(self, item):
        """Push an item onto the heap"""
        heapq.heappush(self._data, (self.key(item), item))

    def pop(self):
        """Pop an item from the heap"""
        return heapq.heappop(self._data)[1]

    def is_empty(self):
        """Returns True if the heap is empty"""
        return len(self._data) == 0

    def is_not_empty(self):
        """Returns True if the heap is not empty"""
        return not self.is_empty()
