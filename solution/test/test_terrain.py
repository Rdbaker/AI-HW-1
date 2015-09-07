"""
    test terrain file for AI Homework 1 solution

    Authors:
        Ryan Baker
        Matthew Beaulieu
        Anthony Romeo
"""
from solution.terrain import Terrain

terrain_map = [[5, 5, 5, 5], [5, 5, 5, 'S'], [5, 5, 'G', 5], [5, 5, 5, 5]]
ter = Terrain(terrain_map)


class TestTerrain:
    def test_get_start_position(self):
        assert ter.get_start_position() == (1, 3)

    def test_get_goal_position(self):
        assert ter.get_goal_position() == (2, 2)

    def test_get_cost_of_start_is_one(self):
        assert ter.get_node_cost(1, 3) == 1

    def test_get_cost_of_goal_is_one(self):
        assert ter.get_node_cost(2, 2) == 1

    def test_get_other_cost_is_five(self):
        assert ter.get_node_cost(0, 0) == 5
