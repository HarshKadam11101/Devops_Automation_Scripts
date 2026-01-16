import requests

username = input("Enter the username who want to search for :\n")
response = requests.get(f'https://api.github.com/users/{username}')

if response.status_code == 200:
    data = response.json()
    print(f"{data['name']}\n")
    print(f"{data['bio']}\n")
    print(f"{data['location']}\n")
    print(f"{data['public_repos']}\n")
else:
    print("User not Found!")

