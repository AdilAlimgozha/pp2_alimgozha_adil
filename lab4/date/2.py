import datetime

today = datetime.datetime.now()
tomorrow = today + datetime.timedelta(days = 1)
yesterday = today - datetime.timedelta(days = 1)
print(today, today.strftime("%A"))
print(tomorrow, tomorrow.strftime("%A"))
print(yesterday, yesterday.strftime("%A"))
#done