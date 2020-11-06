"""
Write a program that prompts the user to enter an integer for
today’s day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6). Also
prompt the user to enter the number of days after today for a future day and dis-
play the future day of the week
"""

# Prompt user enter an integer for today's day
today = eval(input("Enter today's day : "))
days_elapsed = eval(input("Enter the number of days elapsed since today : "))
days_elapsed = days_elapsed + today

if 0 <= today <= 6:
    if today == 0:
        today = "Today is Sunday"
    if today == 1:
        today = "Today is Monday"
    if today == 2:
        today = "Today is Tuesday"
    if today == 3:
        today = "Today is Wednesday"
    if today == 4:
        today = "Today is Thursday"
    if today == 5:
        today = "Today is Friday"
    if today == 6:
        today = "Today is Saturday"
else:
    today = "Inputting Error"

if 0 <= days_elapsed <= 6:
    if days_elapsed == 0:
        day_meet = "the future day Sunday"
    if days_elapsed == 1:
        day_meet = "the future day Monday"
    if days_elapsed == 2:
        day_meet = "the future day Tuesday"
    if days_elapsed == 3:
        day_meet = "the future day Wednesday"
    if days_elapsed == 4:
        day_meet = "the future day Thursday"
    if days_elapsed == 5:
        day_meet = "the future day Friday"
    if days_elapsed == 6:
        day_meet = "the future day Saturday"
else:
    if days_elapsed > 6:
        days_elapsed = days_elapsed % 7
        if days_elapsed == 0:
            day_meet = "the future day is Sunday"
        if days_elapsed == 1:
            day_meet = "the future day is Monday"
        if days_elapsed == 2:
            day_meet = "the future day is Tuesday"
        if days_elapsed == 3:
            day_meet = "the future day is Wednesday"
        if days_elapsed == 4:
            day_meet = "the future day is Thursday"
        if days_elapsed == 5:
            day_meet = "the future day is Friday"
        if days_elapsed == 6:
            day_meet = "the future day is Saturday"

# Display the result
print(f"{today} and {day_meet}")
