#!/usr/bin/env python3
import psutil
import time
from datetime import datetime


def write_log(message) :

    timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    logged_msg = f"[{timestamp}] : {message}\n"

    with open("system_monitor.log","a") as f:
         f.write(logged_msg)

while True:
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    storage_usage = psutil.disk_usage('/').percent

    if cpu_usage<80 and ram_usage<80 and storage_usage<80 :
        write_log(f"Normal : CPU - {cpu_usage} | MEM - {ram_usage} | DISK - {storage_usage}")
    else :
        if cpu_usage >= 80 :
            write_log(f"ALERT: High CPU! - {cpu_usage}%")
        if ram_usage >= 80:
                write_log(f"ALERT: High Memory Usage! - {ram_usage}%")
        if storage_usage >= 80:
            write_log(f"ALERT : Low Disk Space! - {storage_usage}")
    time.sleep(1)

