# Simple Age Calculator

from datetime import date


def get_age(year, month, day):
    today = date.today()

    age = today.year - year

    # Reduce age if birthday hasn't happened yet this year
    if (today.month, today.day) < (month, day):
        age -= 1
    
    return age


print("=== Age Calculator ===")

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

user_age = get_age(birth_year, birth_month, birth_day)

print(f"Your age is {user_age} years.")