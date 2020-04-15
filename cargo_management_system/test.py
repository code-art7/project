import datetime

yes = datetime.datetime.today() - datetime.timedelta(days=1)
print(yes.days_in_month)