import shelve

with shelve.open('bike') as bike:
    bike['make'] = "Honda"
    bike['model'] = "250 dream"
    bike['color'] = "red"
    bike["engine_size"] = 250
    bike["engin_size"] = 250

    for key in bike:
        print(key)

    print(bike["engine_size"])
    print(bike["color"])
    del bike["engin_size"]

    for key in bike:
        print(key)
#correct great
#doing just what is expected

#shelves are presisted in files
#now let us look at the limitations of the shelves

#mispelling earlier in one shelf can lead to wo copies of the keys, because it is persistent