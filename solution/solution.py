"""
    solution file for AI Homework 1 solution

    Authors:
        Ryan Baker
        Matthew Beaulieu
        Anthony Romeo
"""
from heuristic import H_MAP as h_map
from agent import Agent


def solve(terrain_map, heuristic):
    agent = Agent(terrain_map, h_map[heuristic])
    return agent.a_star_search()
