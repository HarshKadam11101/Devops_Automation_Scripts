import json

with open('aws_services.json','r') as f:
    data = json.load(f)
    total = 0

for service in data['services']:
    total += service['hours'] * service['rate_per_hour']

    if total < data['budget_limit']:
        print(f"Services are within budget")
    else:
        print(f"ALERT : Total cost {total} exceeds budget of {data['budget_limit']}")




