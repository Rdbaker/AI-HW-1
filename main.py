"""
    main file for AI Homework 1 solution

    Authors:
        Ryan Baker
        Matthew Beaulieu
        Anthony Romeo
"""
from solution import solution


def start_homework(file_n, heuristic):
    """Kickoff the setup and execution"""
    terrain_map = []
    try:
        with open(file_n, 'r') as file_p:
            # pretty solution
            terrain_map = [line.split() for line in file_p]
        # they're all strings right now, so we need to cast them to integers
        # unless they're 'S' or 'G'
        for i, row in enumerate(terrain_map):
            for j, col in enumerate(row):
                if col != 'S' and col != 'G':
                    terrain_map[i][j] = int(col)

        # but now we have our terrain map in the (y, x) ordered
        # pair positions. i.e. map[i] will select value on the Y axis
        # and map[0][j] will select a value on the X axis. so we should
        # switch those two
        terrain_map = zip(*terrain_map)
    except IOError:
        print 'Program exiting, could not find file.'
        exit(1)

    # check that the heuristic is good
    if heuristic not in [str(i) for i in range(1, 7)]:
        print 'Program exiting, heuristic not in specified range.'
        exit(1)

    return solution.solve(terrain_map, int(heuristic))


if __name__ == "__main__":
    # Ask for the terrain file to read
    FILE_NAME = raw_input('Please give a file to read as the terrain ' +
                          '(defaults to assignment/sample_board.txt): ')

    # default if no file is supplied
    if not FILE_NAME:
        FILE_NAME = 'assignment/sample_board.txt'

    HEURISTIC = raw_input('Please give a heuristic measure of one of [1, 6]: ')

    # start the homework
    start_homework(FILE_NAME, HEURISTIC)
