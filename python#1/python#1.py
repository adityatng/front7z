#day1/100daysofpython
print("hello, world!")
#2
print("day {day} of {text}"
    .format(
        day="1",
        text="#100daysofpython"
        ))
#3
f7z = "FRONT7Z"
print(f7z.capitalize())
print(f7z.lower())
print(f7z.upper())

#4
from datetime import datetime
now = datetime.now()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
print(dd + "/" + mm + "/" + yyyy)