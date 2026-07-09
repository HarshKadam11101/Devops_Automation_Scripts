#!/usr/bin/env python3
import subprocess
import sys
import os
from datetime import datetime

if len(sys.argv)<2 :
    print("Error : Enter the address")
    sys.exit(1)

address = sys.argv[1]
timestamp =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)
log_file_path = os.path.join(script_dir, "monitor.log")
print(log_file_path)

result = subprocess.run(["ping","-c","1",address],capture_output=True,text=True)

if result.returncode==0:
    status = "Up"
    print(f"{address} is up")
else:
    status = "Down"
    print(f"{address} is down")

with open(log_file_path,"a") as f:
    f.write(f"[{timestamp}] Target : {address} | Status:{status}\n")
    print("Saved to monitor.log")