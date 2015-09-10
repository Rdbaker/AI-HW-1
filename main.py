"""
    main file for AI Homework 1 solution

    Authors:
        Ryan Baker
        Matthew Beaulieu
        Anthony Romeo
"""
from solution import solution
import re


def start_homework(file_n, heuristic):
    """Kickoff the setup and execution"""
    terrain_map = []
    try:
        with open(file_n, 'r') as file_p:
            for line in file_p:
                # split the line on tabs
                row = re.split(r'[\t+]', line)
                # strip the \r\n or \n off the end of the lines
                # there's probably a better way to do this
                row[-1] = row[-1][0]
                terrain_map.append(row)
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
