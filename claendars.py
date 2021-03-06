import calendar 

'''
c = calendar.TextCalendar(calendar.MONDAY)
st = c.formatmonth(2017,1,0,0)
print(st)
'''

'''
c = calendar.HTMLCalendar(calendar.MONDAY)
st = c.formatmonth(2017,1)
print(st)


c = calendar.TextCalendar(calendar.MONDAY)
for i in c.itermonthdays(2018,4):
    print(i)


for name in calendar.month_name:
    print(name)

for name in calendar.day_name:
    print(name)
'''

print("Team meetings will be on :")
for m in range(1,13):
    cal = calendar.monthcalendar(2018,m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print ("%10s %2s" % (calendar.month_name[m], meetday))
