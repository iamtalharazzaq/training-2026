# Variables (no hardcoding)
name = input("Enter your name: ")
age = int(input("Enter your age: "))
drinks_coffee = input("Do you drink coffee? (yes/no): ").lower() == "yes"
salary = float(input("Enter your monthly salary (Rs): "))

# Calculations
retirement_age = 60
years_until_retirement = retirement_age - age

# Coffee budget calculation
cups_per_day = 3
price_per_cup = 150
days_per_week = 7

# If the person drinks coffee, calculate the weekly budget; otherwise, it's 0
weekly_coffee_budget = cups_per_day * price_per_cup * days_per_week if drinks_coffee else 0

# Output
output = (
    "\n\n---------------------------------------------------------\n"
    f"My name is {name}. I am {age} years old. \n"
    f"I {'do' if drinks_coffee else 'do not'} drink coffee. \n"
    f"My monthly salary is Rs. {salary:.2f}. \n"
    f"I will retire in {years_until_retirement} years. \n"
    f"My weekly coffee budget is Rs. {weekly_coffee_budget}."
    "\n---------------------------------------------------------\n"
)

print(output)