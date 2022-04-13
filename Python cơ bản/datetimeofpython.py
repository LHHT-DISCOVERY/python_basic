import datetime 
today  = datetime.datetime(year = 2022 , month = 4 , day = 12 , hour = 16 , minute = 16 , second = 30 )
print ("hôm nay là : ")
print (today)
tooday = datetime.datetime.now();
weeek = datetime.timedelta(days=7)
# thoi gian thuc
print (tooday)
print("\n")
#ngay nay tuan tiep theo 
print(tooday + weeek)
print("\n")
# chi lay ngay thang nam , HOAC LAY GIO PHUT GIAY
print (tooday.strftime("%Y-%m-%d ") ,"\n")
print(tooday.strftime("%H:%M:%S"))
print("\n")
user_date = input("Enter to day date : ")
# Assume they entered 23-12-2022
tday = datetime.datetime.strptime(user_date, "%d-%m-%Y")
print(tday,"\n")
# dau tgian
print(tooday.timestamp())
import time
print (time.time())
# chuyển đổi múi giờ này sang múi giờ khác
import pytz
eastern = pytz.timezone("US/Eastern")
amsterdam = pytz.timezone("Europe/Amsterdam")
local_time = datetime.datetime.now()
eastern_time = eastern.localize(local_time)
print(eastern_time)
amsterdam_time = eastern_time.astimezone(amsterdam)
print(amsterdam_time)