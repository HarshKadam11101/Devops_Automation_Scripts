#!/usr/bin/env python3
import sys

print(f"1.The Whole List:{sys.argv}")

print(f"2.Script Name (Index 0):{sys.argv[0]}")
print(len(sys.argv))

if len(sys.argv)>1:
    print(f"3.First Argument (Index 1):{sys.argv[1]}")

if len(sys.argv)>2:
    print(f"4. Second Argument (Index 2):{sys.argv[2]}")