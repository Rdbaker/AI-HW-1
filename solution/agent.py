"""
    agent file for AI Homework 1 solution

    Authors:
        Ryan Baker
        Matthew Beaulieu
        Anthony Romeo
"""
from math import ceil


class Agent(object):
    """
        Class to handle decisions about getting to the goal.

        :param: Terrain - the terrain on which the agent is navigating
        :param: Heuristic - the difficulty level of the heuristic
    """
    def __init__(self, terrain, heuristic):
        self.terrain = terrain
        self.heuristic = heuristic
        self.directions = {'N': (0, 1),
                           'E': (1, 0),
                           'S': (0, -1),
                           'W': (-1, 0)}
        self.position = list(terrain.get_start_position())
        self.facing = 'N'
        self.score = 0
        self.last_move = None
        self.action_costs = {'forward': lambda cost: -cost,
                             'bash': lambda cost: -3,
                             'turn': lambda cost: -ceil(cost/3),
                             'demolish': lambda cost: -4}

    def update_score(self, cost_fn, cost):
        """Update the score based on the cost function and the node cost"""
        self.score += cost_fn(cost)

    def forward(self):
        """The rules to move forward"""
        # Change X value
        self.position[0] = self.directions[self.facing][0]
        # Change Y value
        self.position[1] = self.directions[self.facing][1]
        # Update the score
        self.update_score(self.action_costs['forward'],
                          self.terrain.get_node_cost(self.position[0],
                                                     self.position[1]))

