import os

servers = ["google.com", "facebook.com", "fake-website-123.com", "amazon.com"]

for server in servers :
    result = os.system(f"ping -n 1 {server} > nul")
    if result==0 :
        print(f"{server} is Working")
    else :
        print(f"{server} is Down")