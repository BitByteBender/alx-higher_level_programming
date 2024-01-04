#!/usr/bin/python3

import sys

if (__name__ == "__main__"):
    args = sys.argv[1:]
    argsCount = len(args)

    if (argsCount == 0):
        print("0 arguments.")
    else:
        if (argsCount == 1):
            print("{} argument:\n{}: {}".format(argsCount, argsCount, args[0]))
        else:
            print("{} arguments:".format(argsCount))
            for i in range(argsCount):
                print("{}: {}".format((i + 1), args[i]))
