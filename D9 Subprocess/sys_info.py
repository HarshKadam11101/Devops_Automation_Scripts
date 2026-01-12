#!/usr/bin/env python3
import subprocess

cmd = ["ls","-l"]

result = subprocess.run(cmd,capture_output=True,text=True)

print(f"Exitcode : {result.returncode}")
print(result.stdout)