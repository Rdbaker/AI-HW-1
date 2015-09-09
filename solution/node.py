"""
    node file for AI Homework 1 solution

    Authors:
        Ryan Baker
        Matthew Beaulieu
        Anthony Romeo
"""


class Node(object):
    """
        Class to handle storing state about a node in the search tree

        :param: position - a 2-tuple of the (x, y) position on the terrain map
        :param: direction - one of ['N', 'E', 'S', 'W'], corresponding to the
                            direction
    """
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        self.g = 0
        self.h = 0
        self.f = self.g + self.h
        self.closed = False

    def is_the_same(self, node):
        """Returns True if the given node is the same as this one"""
        return (self.position == node.position and
                self.direction == node.direction)
