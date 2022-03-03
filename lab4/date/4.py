import datetime

x = datetime.datetime(int(input("year1: ")), int(input("month1: ")), int(input("day1: ")), int(input("hour1: ")), int(input("minute1: ")), int(input("second1: ")))
y = datetime.datetime(int(input("year2: ")), int(input("month2: ")), int(input("day2: ")), int(input("hour2: ")), int(input("minute2: ")), int(input("second2: ")))
x_sec = x.hour * 60 * 60 + x.minute * 60 + x.second
y_sec = y.hour * 60 * 60 + y.minute * 60 + y.second
day_differ = abs(x - y)
print("Day difference: ", day_differ)
sec_differ = (abs(x_sec - y_sec))
print("Second difference: ", day_differ.days * 24 * 60 * 60 + sec_differ)
#done