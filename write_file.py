#in this file we are going to deal with writing files


cities  = ["Adelaide", "Alice Springs", "Dublin", "Melbourne", "Sydney"]

with open("cities.txt", 'w') as city_file:
    for city in cities:
        print(city, file=city_file)

#Great three lines of code and it is written to the file cities.txt
#Really incredible

#external drivers are much slower than your computer. You te dta to be written is written to be a buffer
#data is written to the buffer, and written to the file, depending upon the speed of the drive
#there is a flush parameter, and will flush the file directly to the file
#include flush=True in the print statement

cities = []
with open("cities.txt", 'r') as city_file:
    for city in city_file:
        cities.append(city.strip("\n"))

print(cities)
for city in cities:
    print(city)

#anything you can see on the screen can be written to a text file, but necessarily not be reread in the same form

imelda = "More Mayhem", "Imelda May", "2011", (
    (1, "Pulling the hug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town")
)

with open("imelda.txt", "w") as imelda_file:
    print(imelda, file=imelda_file)


with open("imelda.txt", "r") as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)

print(imelda)
title, artist, year, tracks  = imelda
print(title)
print(artist)

#though this do allows us to deal with reading the data, but it is not a good option to
#use eval when you are dealing with data external to your program
#because the content of the file could be changed