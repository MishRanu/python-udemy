import pytz
import datetime

country = 'Europe/Moscow'

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country,local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

for x in pytz.all_timezones:
    print(x)

for x in sorted(pytz.country_names):
    print(x + ":" + pytz.country_names[x])


for x in sorted(pytz.country_names):
    print(x + ":" + pytz.country_names[x])
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t \t {}; {}".format(zone, local_time))
    else:
        print("\t \t No time zone defined")

#it is easy to convert utc to local time zone using pytz
#but it is indeed difficult to convert local time to utc unless there is explictly time zone
#so store time in utc and convert to local time only when to display them to the users of the program
#which gets rid a lot of the problems. pytz helps us convert a naive date time to time aware date time


print("="*50)

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Native local time {}".format(local_time))
print("Native UTC {}".format(utc_time))

aware_local_time = pytz.utc.localize(utc_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print("aware local time: {}, time zone : {}".format(aware_local_time, aware_local_time.tzinfo))
print("aware UTC {}, time zone {}".format(aware_utc_time, aware_utc_time.tzinfo))

#assuming this time and date are in utc, we add an hour and print the time
gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())

s = 1445733000
t = s + 3600

gb = pytz.timezone("GB")
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print(dt1)
print(dt2)

# gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0 , 0)
# print(gap_time)
# print(gap_time.timestamp())
#
# s = 1445716800
# t = s + (60*60)


