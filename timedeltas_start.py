from datetime import date
from datetime import datetime
from datetime import timedelta



def main():
    print (timedelta(days=365,hours=5,minutes=1))
    now =datetime.now()
    print("today is :" +str(now))
    print("one year from now ", str(now +timedelta(days=365) ) )
    print("time after two weeks and 5 days from now ",  str(now+timedelta(days=5, weeks=2)))
    t= datetime.now() - timedelta(weeks=1)
    s=t.strftime("%A %B %d,%Y")
    print("one week ago it was: ", s)
    
    today=date.today()
    afd=date(today.year, 4, 1)
    
    if afd< today:
        print("April foold day already went by %d days ago" % ((today-afd).days))
        afd = afd.replace (year = today.year+1)
        time_to_afd= afd-today
        print("It's just ",  time_to_afd.days ,  "days until April Fool's Day :")
        
if __name__ == "__main__":
    main()

