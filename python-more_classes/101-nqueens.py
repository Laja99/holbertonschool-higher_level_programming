#!/usr/bin/python3
"""
Solves the N Queens problem using backtracking
"""

import sys


def print_usage_and_exit(msg):
    print(msg)
    sys.exit(1)


def is_safe(queens, row, col):
    """
    Check if a queen can be placed at (row, col)
    """
    for r, c in queens:
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n, row, queens):
    """
    Recursive backtracking solver
    """
    if row == n:
        print(queens)
        return

    for col in range(n):
        if is_safe(queens, row, col):
            solve_nqueens(n, row + 1, queens + [[row, col]])


def main():
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")

    try:
        n = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    if n < 4:
        print_usage_and_exit("N must be at least 4")

    solve_nqueens(n, 0, [])


if __name__ == "__main__":
    main()
