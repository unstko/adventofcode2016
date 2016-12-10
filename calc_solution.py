#!/usr/bin/env python
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        nr = sys.argv[1]
    else:
        nr = input("Day: ")
    sys.path.insert(0, './'+nr)
    import solution
    solution = solution.Solution(nr)
    solution.calculate()
    print(solution)
