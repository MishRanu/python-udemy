# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments it contains, and the length of each segment.
#
# An IP address consists of 4 numbers, separated from each other with a full stop. But
# your program should just count however many are entered
# Examples of the input you may get are:
#    127.0.0.1
#    .192.168.0.1
#    10.0.123456.255
#    172.16
#    255
#
# So your program should work even with invalid IP Addresses. We're just interested in the
# number of segments and how long each one is.
#
# Once you have a working program, here are some more suggestions for invalid input to test:
#    .123.45.678.91
#    123.4567.8.9.
#    123.156.289.10123456
#    10.10t.10.10
#    12.9.34.6.12.90
#    '' - that is, press enter without typing anything
#
# This challenge is intended to practise for loops and if/else statements, so although
# you could use other techniques (such as splitting the string up), that's not the
# approach we're looking for here.

ipAddress = input("Please enter your ip addresss \n")

segments = 1

for char in ipAddress:
    if char in "0123456789":
        continue
    elif char == '.':
        segments += 1

print("the number of segments in the ip address is {}".format(segments))

currentSegmentLength = 0

if (len(ipAddress) == 0):
    print("the input you entered is not valid")
else:
    for i in range(0, len(ipAddress)):
        if ipAddress[i] in "0123456789" or ipAddress[i] == '.':
            if ipAddress[i] in "0123456789":
                currentSegmentLength += 1
                if currentSegmentLength > 4:
                    print("The number is not valid")
                    break
            elif ipAddress[i] == '.' and currentSegmentLength==0:
                print("The number is not valid")
            else:
                currentSegmentLength = 0
        else:
            print("The number is not valid")
            break
    else:
        print("the input you entered is valid")