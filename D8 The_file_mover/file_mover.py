#!/usr/bin/env python3
import sys
import shutil

if len(sys.argv)<3:
    print("Error: You forgot the arguments")
    sys.exit(1)

src = sys.argv[1]
dest = sys.argv[2]

try:
    print(f"Moving File from {src} to {dest}")
    shutil.move(src,dest)
    print("Done")
except Exception as e :
    print(f"Error - failed to move :{e}")