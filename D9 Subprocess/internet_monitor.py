#!/usr/bin/env python3
import subprocess
import sys

if len(sys.argv)<2 :
    print("Error : Enter the address")
    sys.exit(1);

address = sys.argv[1]

result = subprocess.run(["ping","-c","1",address])

if result.returncode==0:
    print(f"{address} is up")
else:
    print(f"{address} is down")
