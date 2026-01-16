calculate_units = 24*60
unit = "minutes"

def days_to_hours(day):
    print(f"{day} days are {day * calculate_units} {unit}")


days_to_hours(20)
days_to_hours(35)