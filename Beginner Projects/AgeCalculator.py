
# Created By @dypixx ....

from datetime import datetime, timedelta

birthday_str = input("Enter your birthday (YYYY-MM-DD): ")
birthday = datetime.strptime(birthday_str, '%Y-%m-%d')
now = datetime.now()
delta = now - birthday
weeks = delta.days // 7
years = delta.days // 365
remaining_days = delta.days % 365
months = remaining_days // 30
days = remaining_days % 30
total_seconds = int(delta.total_seconds())
total_minutes = total_seconds // 60
seconds = total_seconds % 60
current_year_birthday = birthday.replace(year=now.year)


saved = f"""TOTAL Years: {years}, Months: {months}, Days: {days}, Weeks: {weeks}, Total Days: {
    delta.days}, Total Minutes: {total_minutes}, Total Seconds: {total_seconds}"""
print(saved)


if current_year_birthday < now:
    next_birthday = current_year_birthday.replace(year=now.year + 1)
else:
    next_birthday = current_year_birthday

time_until = next_birthday - now

days_until = time_until.days
hours_until = time_until.seconds // 3600
minutes_until = (time_until.seconds % 3600) // 60
seconds_until = time_until.seconds % 60
next_age = (now.year - birthday.year) + \
    (1 if next_birthday.year > now.year else 0)

print()
print("Time until next birthday:")
print(f"Days: {days_until}")
print(f"On your next birthday, you will be {next_age} years old.")
