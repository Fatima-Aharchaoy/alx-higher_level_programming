#!/usr/bin/python3
import sys


def main():
    argv = sys.argv[1:]  # Exclude the script name from the arguments list
    arg_count = len(argv)  # Number of arguments

    if arg_count == 0:
        print(f"{arg_count} arguments.")
    elif arg_count == 1:
        print(f"{arg_count} argument:")
    else:
        print(f"{arg_count} arguments:")

    # Print each argument with its position
    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")


if __name__ == "__main__":
    main()
