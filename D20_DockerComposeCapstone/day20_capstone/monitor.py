import psutil
import time
import os

# Define the path to the shared file
REPORT_FILE = "/shared_data/index.html"

print("--- Monitor Service Started ---")

while True:
    # 1. Get Stats
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    # 2. Create simple HTML with auto-refresh (Meta tag)
    html_content = f"""
    <html>
    <head>
        <meta http-equiv="refresh" content="2">
        <title>Harsh's DevOps Dashboard</title>
        <style>
            body {{ font-family: sans-serif; text-align: center; padding-top: 50px; background-color: #f0f0f0; }}
            .card {{ background: white; padding: 20px; border-radius: 10px; display: inline-block; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
            h1 {{ color: #333; }}
            .stat {{ font-size: 24px; margin: 10px; color: #007BFF; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>💻 System Health</h1>
            <p class="stat">CPU Usage: <strong>{cpu}%</strong></p>
            <p class="stat">RAM Usage: <strong>{ram}%</strong></p>
	    <p class="stat">DISK Usage: <strong>{disk}%</strong></p>
            <p><small>Updated: {time.ctime()}</small></p>
        </div>
    </body>
    </html>
    """

    # 3. Write to the file
    with open(REPORT_FILE, "w") as f:
        f.write(html_content)

    print(f"Updated dashboard: CPU {cpu}% | RAM {ram}%")
