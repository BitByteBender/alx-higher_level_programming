#!/usr/bin/python3

import sys

if (__name__ == "__main__"):
    args = sys.argv[1:]
    argsCount = len(args)

    if (argsCount == 0):
        print(0)
    else:
        result = 0
        for i in range(argsCount):
            result += int(args[i])
        print("{}".format(result))
