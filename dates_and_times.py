# standard library: datetime time calendar
# external: dateutil arrow
from datetime import datetime, date

today = date.today()
brit_bd = date(1990, 8, 27)
print(today, brit_bd)

diff = today - brit_bd
print(diff)
age = diff.days / 365.25
print("Britomarte's age is", age)

years, days = divmod(diff.days, 365.25)
print(f"{years} years and {days} days")

now = datetime.now()
print(now)

moment = datetime(1975, 3, 22, 10, 14, 37)
print(moment)





