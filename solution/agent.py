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
from terrain import Terrain
from utils import backtrace


class Agent(object):
    """
        Class to handle decisions about getting to the goal.

        :param: Terrain - the terrain on which the agent is navigating
        :param: Heuristic - the difficulty level of the heuristic
    """
    def __init__(self, terrain, heuristic):
        self.terrain = Terrain(terrain)
        self.directions = {'N': (0, -1),
                           'E': (1, 0),
                           'S': (0, 1),
                           'W': (-1, 0)}
        self.start_node = Node(self.terrain.get_start_position(), 'N', 0)
        # Push our start position onto the heap
        self.search_heap = SearchHeap(initial=[self.start_node],
                                      g_func=lambda node: node.g,
                                      h_func=heuristic,
                                      goal=self.terrain.get_goal_position())
        self.visited = []
        self.position = list(self.terrain.get_start_position())
        self.facing = 'N'
        self.action_costs = {'forward': lambda cost: -cost,
                             'bash': lambda cost: -3,
                             'turn': lambda cost: -ceil(float(cost)/float(3)),
                             'demolish': lambda cost: -4}
        print "goal position:"
        print self.terrain.get_goal_position()

    def a_star_search(self):
        """
        A* search for the goal
        inspired by:
            https://github.com/qiao/PathFinding.js/blob/master/src/finders/AStarFinder.js#L54
        """
        while self.search_heap.is_not_empty():
            node = self.search_heap.pop()
            # add the node to self.visited to show we visited it
            self.visited.append(node)
            if self.terrain.is_goal_node(node):
                # TODO: make it return the path to the goal
                # as a sequence of nodes
                print "Score of the path:"
                print node.g + 100
                print "Number of actions required to reach the goal:"
                print node.depth
                print "Number of nodes expanded:"
                print len(self.visited)
                print "Actions taken from start:"
                backtrace(node)
                break

            for action, neighbor in self.get_search_neighbors(node).iteritems():
                last_time_visited = self.has_been_visited_already(neighbor)
                if last_time_visited is None and self.terrain.node_inside_terrain(neighbor):
                    neighbor.g = self.assign_g_cost(neighbor, node, self.terrain, action)
                    self.search_heap.push(neighbor)

    def get_search_neighbors(self, node):
        """Returns a list of node leaves from the given node."""
        # These things create nodes
        turn_left = Node(position=node.position,
                         direction=self.turn_left(node),
                         depth=node.depth + 1,
                         action='turn left',
                         parent=node)
        turn_right = Node(position=node.position,
                          direction=self.turn_right(node),
                          depth=node.depth + 1,
                          action='turn right',
                          parent=node)
        move_forward = Node(position=self.forward(node),
                            direction=node.direction,
                            depth=node.depth + 1,
                            action='move forward',
                            parent=node)
        bash_and_forward = Node(position=self.bash_and_forward(node),
                                direction=node.direction,
                                depth=node.depth + 1,
                                action='bash and move forward',
                                parent=node)
        # return the nodes
        return {'turn_left': turn_left,
                'turn_right': turn_right,
                'move_forward': move_forward,
                'bash_and_forward': bash_and_forward}

    def assign_g_cost(self, node, parent, terrain, action):
        if 'turn' in action:
            # Update the g costs of the nodes
            return(parent.g +
                   self.action_costs['turn'](
                           self.terrain.get_cost_from_tuple(
                               node.position)))
        elif action == 'move_forward':
            return parent.g + self.action_costs['forward'](
                                    self.terrain.get_cost_from_tuple(
                                        node.position))
        else:
            return parent.g + self.action_costs['bash'](0) + self.action_costs['forward'](
                                        self.terrain.get_cost_from_tuple(
                                            node.position))

    def forward(self, node):
        """The rules to move forward"""
        new_pos = (node.position[0] + self.directions[node.direction][0],
                   node.position[1] + self.directions[node.direction][1])
        # TODO: Update the score
        return new_pos

    def bash_and_forward(self, node):
        """The rules to bash and move forward"""
        return self.forward(Node(position=self.forward(node),
                                 direction=node.direction,
                                 depth=node.depth + 1))

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
