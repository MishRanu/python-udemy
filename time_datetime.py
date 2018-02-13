import time
#
#
# print(time.gmtime(0))
# print(time.localtime())
# print(time.time())
#
# time_here = time.localtime()
#
# print("Year: ", time_here[0], time_here.tm_year)
# print("Month: ", time_here[1], time_here.tm_mon)
# print("Day: ", time_here[3], time_here.tm_mday)

from time import monotonic as my_timer
import random

input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")
end_time = my_timer()

print("Started at ", time.strftime("%X", time.localtime(start_time)))
print("Ended at ", time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time - start_time))


#there are many time modules in python to measure elapsed time
# use proces_time to measure time elapsed by cpu performance
#use perf_counter to measure difference between time between two instances
# monotonic is also used, and is same like perf_time, but pef_time has higher perfomance on most systems


# pep is called python enhancement process
# check pep 0418 to read about monotic time