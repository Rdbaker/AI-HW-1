"""
    agent file for AI Homework 1 solution

    Authors:
        Ryan Baker
        Matthew Beaulieu
        Anthony Romeo
"""


def backtrace(node):
    if node.parent:
        backtrace(node.parent)
    print node.action
