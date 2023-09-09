#!/usr/bin/python3
import sys
if __name__ == "__main__":
    """Print the sum of all arguments."""
    count = len(sys.argv) - 1
    sum = 0
    for i in range(1, count + 1):
        sum += int(sys.argv[i])
    print("{}".format(sum))
