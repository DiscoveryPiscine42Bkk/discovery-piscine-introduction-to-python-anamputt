#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("RTFM (Read the F-ing manual)")
        return

    text = sys.argv[1]
    count_z = text.count('z')

    if count_z == 0:
        print("RTFM (Read the F-ing manual)")
    else:

        print('z' * count_z)
main()