# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime
import pytz
import random

available_zones = []
for i in range(0, 10):
    r = random.randint(0, len(pytz.all_timezones))
    available_zones.append(pytz.all_timezones[r])
    print("Index: {} Timezone: {}".format(i+1, pytz.all_timezones[r]))

choice = input("Select ")
while int(choice) != 0:
    zone = pytz.timezone(available_zones[int(choice)-1])
    utcTime = datetime.datetime.utcnow()
    localTime = datetime.datetime.now()
    zoneTime = pytz.utc.localize(utcTime).astimezone(zone)
    print("Selected Zone Time: {} | Selected Local Time: {} | Selected UTC Time: {}".format(zoneTime, localTime, utcTime))
    choice  = input("Enter new choice")
else:
    print("Entered 0. Quitting the program!")