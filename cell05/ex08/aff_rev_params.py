#!/usr/bin/env python3
import sys

def main():
    params = sys.argv[1:]
    if len(params) < 2:
        print("RTFM (Read the F-ing manual)")
    else:
        # แสดงพารามิเตอร์ย้อนกลับทีละบรรทัด
        for param in reversed(params):
            print(params)
main()