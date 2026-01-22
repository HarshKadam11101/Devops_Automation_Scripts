import psutil
import time

print("--- Containerized System Monitor Starting ---")
while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    print(f"Stats: CPU: {cpu}% | RAM: {ram}%")
    time.sleep(2)
