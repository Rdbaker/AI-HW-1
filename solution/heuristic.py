"""
    solution file for AI Homework 1 solution

    Authors:
        Ryan Baker
        Matthew Beaulieu
        Anthony Romeo
"""

# Heuristic has a value of 0

UP = 1
DOWN = 2
RIGHT = 4
LEFT = 5
NOTHING = 3

def extract_coords(coord):
    return coord[0], coord[1]


def heuristic1(node_coords, node_dir, goal_coords):
    return 0


def heuristic2(node_coords, node_dir, goal):
    startrow, startcol = extract_coords(node_coords)
    goalrow, goalcol = extract_coords(goal)
    difrow = abs(startrow - goalrow)
    difcol = abs(startcol - goalcol)

    return min(difrow, difcol)


def heuristic3(node_coords, node_dir, goal):
    startrow, startcol = extract_coords(node_coords)
    goalrow, goalcol = extract_coords(goal)
    difrow = abs(startrow - goalrow)
    difcol = abs(startcol - goalcol)

    return max(difrow, difcol)


def heuristic4(node_coords, node_dir, goal):
    startrow, startcol = extract_coords(node_coords)
    goalrow, goalcol = extract_coords(goal)
    difrow = abs(startrow - goalrow)
    difcol = abs(startcol - goalcol)

    return difrow + difcol


def heuristic5(node_coords, node_dir, goal):
    startrow, startcol = extract_coords(node_coords)
    goalrow, goalcol = extract_coords(goal)
    difrow = startrow - goalrow
    difcol = startcol - goalcol
    direction = UP

    if difrow == 0:
        rowdirection = NOTHING
    elif difrow > 0:
        rowdirection = UP
    else:
        rowdirection = DOWN

    if difcol == 0:
        coldirection = NOTHING
    elif difcol > 0:
        coldirection = RIGHT
    else:
        coldirection = LEFT

    if direction == rowdirection or direction == coldirection:
        if rowdirection == NOTHING or coldirection == NOTHING:
            turn = 0
        else:
            turn = .3
    else:
        turn = .6

    # Used to calculate the minimum amount of turning needed

    turnsum = abs(difrow) + abs(difcol) + turn

    return turnsum


def heuristic6(node_coords, node_dir, goal):
    return 3 * heuristic5(node_coords, node_dir, goal)

H_MAP = {1: heuristic1,
         2: heuristic2,
         3: heuristic3,
         4: heuristic4,
         5: heuristic5,
         6: heuristic6}
