#time.timezone
#time.tzname names nondst time zone and name of dst time zone name
#if time.daylight is non zero then dst_time zone name is defined and should only then be used

#uses dst time to calculate the tome offset

import time

print("The epoch of this system starts at ", time.strftime("%c", time.gmtime(0)))

print("The current time zone is {0} with the offset of {1}".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("Day light saving time is in affect on this location")
    print("The DST Time zone is", time.tzname[1])

print("The local time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("UTC time is " + time.strftime("%Y-%m-%d %H:%M%S", time.gmtime()))

import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())