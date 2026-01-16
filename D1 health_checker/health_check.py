# server_list = [
#     {"name":"Server-1","ip":"192.62.1","status":"active"},
#     {"name":"Server-2","ip":"192.68.1","status":"inactive"},
# ]

def check_server(name,status,ip):
    if status.lower().strip() == "inactive":
        print(f"{name} at {ip} is DOWN.")
    else :
        print(f"{name} is running")

name = input("Enter the server name\n")
status = input("Enter the status\n")
ip = input("Enter the IP\n")

check_server(name,status,ip)