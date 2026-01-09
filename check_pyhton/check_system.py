#!/usr/bin/env python3
import platform
import datetime

print("--- SYSTEM REPORT ---")
print(f"✅ OS:   {platform.system()} {platform.release()}")
print(f"✅ Time: {datetime.datetime.now()}")
print("---------------------")
