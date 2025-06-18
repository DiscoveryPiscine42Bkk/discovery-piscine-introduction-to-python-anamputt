#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 3:
        print("RTFM (Read the F-ing manual)")
        return

    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    except ValueError:
        print("RTFM (Read the F-ing manual)")
        return

    if start <= end:
        arr = list(range(start, end + 1))
    else:
        # กรณี start > end สร้างลำดับย้อนกลับ
        arr = list(range(start, end - 1, -1))

    print(arr)
main()