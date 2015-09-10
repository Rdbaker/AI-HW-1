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


def heuristic1():
    return 0


def heuristic2(terrainmap):

    start = terrainmap.get_start_node()
    goal = terrainmap.get_goal_node()
    startrow = start[0]
    startcol = start[1]
    goalrow = goal[0]
    goalcol = goal[1]
    difrow = abs(startrow - goalrow)
    difcol = abs(startcol - goalcol)

    if difrow > difcol:
        return difcol
    else:
        return difrow


def heuristic3(terrainmap):

    start = terrainmap.get_start_node()
    goal = terrainmap.get_goal_node()
    startrow = start[0]
    startcol = start[1]
    goalrow = goal[0]
    goalcol = goal[1]
    difrow = abs(startrow - goalrow)
    difcol = abs(startcol - goalcol)

    if difrow > difcol:
        return difrow
    else:
        return difcol


def heuristic4(terrainmap):

    start = terrainmap.get_start_node()
    goal = terrainmap.get_goal_node()
    startrow = start[0]
    startcol = start[1]
    goalrow = goal[0]
    goalcol = goal[1]
    difrow = abs(startrow - goalrow)
    difcol = abs(startcol - goalcol)
    difsum = difrow + difcol

    return difsum


def heuristic5(terrainmap):

    start = terrainmap.get_start_node()
    goal = terrainmap.get_goal_node()
    startrow = start[0]
    startcol = start[1]
    goalrow = goal[0]
    goalcol = goal[1]
    difabsrow = abs(startrow - goalrow)
    difabscol = abs(startcol - goalcol)
    difrow = startrow - goalrow
    difcol = startcol - goalcol
    difsum = difabsrow + difabscol
    direction = UP

    print difrow, difcol

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

    turnsum = difsum + turn

    return turnsum


def heuristic6(terrainmap):

    start = terrainmap.get_start_position()
    goal = terrainmap.get_goal_position()
    startrow = start[0]
    startcol = start[1]
    goalrow = goal[0]
    goalcol = goal[1]
    difabsrow = abs(startrow - goalrow)
    difabscol = abs(startcol - goalcol)
    difrow = startrow - goalrow
    difcol = startcol - goalcol
    difsum = difabsrow + difabscol

    direction = UP

    print difrow, difcol

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

    turnsum = difsum + turn

    return 3*turnsum
