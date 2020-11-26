

age = input("What is your current age: ")
life_until = input("To what age of lifetime calculate: ")

years_left = int(int(life_until) - int(age))

days_left = int(years_left * 365)
weeks_left = int(days_left / 7)     # May use: years_left * 52
monthes_left = int(days_left / 30)  # May use: years_left * 12

print(f"You have {years_left} years or {days_left} days or {weeks_left} weeks or {monthes_left} monthes left.")