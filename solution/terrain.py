"""
    solution file for AI Homework 1 solution

    Authors:
        Ryan Baker
        Matthew Beaulieu
        Anthony Romeo
"""


class Terrain(object):
    """
        Class to handle interactions with the terrain.

        :param: terrain_map - 2d rectangular array of the terrain
            ex: [ [ 3, 3, 3, 3 ],
                  [ 3, 3, S, 3 ],
                  [ 3, G, 3, 3 ],
                  [ 3, 3, 3, 3 ] ]
    """
    def __init__(self, terrain_map):
        self.terrain_map = terrain_map
        self.start_position = self._find_start()
        self.goal_position = self._find_goal()

    def get_start_position(self):
        """Getter for the start node position"""
        return self.start_position

    def get_goal_position(self):
        """Getter for the goal node position"""
        return self.goal_position

    def get_cost_from_tuple(self, t):
        """Get the cost of a node from a coordinate pairing"""
        return self.get_node_cost(t[0], t[1])

    def get_node_cost(self, row, col):
        """Get the cost of a node from coordinates"""
        cost = self.terrain_map[row][col]
        return 1 if isinstance(cost, str) else cost

    def _find_start(self):
        """Find the position of the start node"""
        for i, row in enumerate(self.terrain_map):
            for j, col in enumerate(row):
                if col == 'S':
                    return (i, j)

    def _find_goal(self):
        """Find the position of the goal node"""
        for i, row in enumerate(self.terrain_map):
            for j, col in enumerate(row):
                if col == 'G':
                    return (i, j)

    def is_goal_node(self, node):
        """Return True if the given node is in the goal position"""
        return node.position == self.get_goal_position()
