"""
    agent file for AI Homework 1 solution

    Authors:
        Ryan Baker
        Matthew Beaulieu
        Anthony Romeo
"""
from math import ceil
from node import Node
from search_heap import SearchHeap


class Agent(object):
    """
        Class to handle decisions about getting to the goal.

        :param: Terrain - the terrain on which the agent is navigating
        :param: Heuristic - the difficulty level of the heuristic
    """
    def __init__(self, terrain, heuristic):
        self.terrain = terrain
        self.directions = {'N': (0, 1),
                           'E': (1, 0),
                           'S': (0, -1),
                           'W': (-1, 0)}
        self.start_node = Node(terrain.get_start_position(), 'N')
        # Push our start position onto the heap
        self.search_heap = SearchHeap(initial=[self.start_node],
                                      eval_fn=heuristic)
        self.visited = []
        self.position = list(terrain.get_start_position())
        self.facing = 'N'
        self.score = 0
        self.last_move = None
        self.action_costs = {'forward': lambda cost: -cost,
                             'bash': lambda cost: -3,
                             'turn': lambda cost: -ceil(cost/3),
                             'demolish': lambda cost: -4}

    def a_star_search(self, h):
        """A* search for the goal"""
        # TODO
        while self.search_heap.is_not_empty():
            node = self.search_heap.pop()
            # add the node to self.visited to show we visited it
            self.visited.append(node)

            if self.terrain.is_goal_node(node):
                # TODO: make it return the path to the goal
                # as a sequence of nodes
                return node.f

            for neighbor in self.get_search_neighbors(node):
                last_time_visited = self.has_been_visited_already(neighbor)
                if last_time_visited is None:
                    self.search_heap.push(neighbor)

    def get_search_neighbors(self, node):
        """Returns a list of node leaves from the given node."""
        turn_left = Node(position=node.position,
                         direction=self.turn_left(node))
        turn_right = Node(position=node.position,
                          direction=self.turn_right(node))
        move_forward = Node(position=self.forward(node),
                            direction=node.direction)
        bash_and_forward = Node(position=self.bash_and_forward(node),
                                direction=node.direction)
        # Update the g costs of the nodes
        turn_left.g = (node.g +
                       self.action_costs['turn'](
                           self.terrain.get_cost_from_tuple(
                               node.position)))
        turn_right.g = turn_left.g
        move_forward.g = node.g + self.action_costs['forward'](
                                    self.terrain.get_cost_from_tuple(
                                        move_forward.position))
        bash_and_forward.g = move_forward.g + self.action_costs['bash'](0)
        # return the nodes
        return [turn_left, turn_right, move_forward, bash_and_forward]

    def update_score(self, cost_fn, cost):
        """Update the score based on the cost function and the node cost"""
        self.score += cost_fn(cost)

    def forward(self, node):
        """The rules to move forward"""
        new_pos = (node.position[0] + self.directions[node.direction][0],
                   node.position[1] + self.directions[node.direction][1])
        # TODO: Update the score
        return new_pos

    def bash_and_forward(self, node):
        """The rules to bash and move forward"""
        return self.forward(self.forward(node))

    def turn_right(self, node):
        """The rules to turn right"""
        dirs = ['N', 'E', 'S', 'W']
        return dirs[(dirs.index(node.direction)+1) % len(dirs)]

    def turn_left(self, node):
        """The rules to turn left"""
        dirs = ['N', 'E', 'S', 'W']
        return dirs[(dirs.index(node.direction)-1) % len(dirs)]

    def has_been_visited_already(self, node):
        """
            Returns None or a Node

            This function will return None if the node has not been
            previously visited OR if the given node is less expensive
            to reach than the previous time we visited that position+direction
            pairing

            :param: Node - the node to check against for having already visited
                           that position + direction pairing
        """
        for visited in self.visited:
            # compare the two nodes
            if visited.is_the_same(node):
                if node.g > visited.g:
                    return visited
        return None
