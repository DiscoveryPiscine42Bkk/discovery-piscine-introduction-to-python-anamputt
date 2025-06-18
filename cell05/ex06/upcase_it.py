#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) == 2:
        # แปลงพารามิเตอร์ตัวที่ 1 เป็นตัวพิมพ์ใหญ่
        print(sys.argv[1].upper())
    else:
        print("RTFM (Read the F-ing manual)")
main()