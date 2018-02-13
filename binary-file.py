#in this file we are going to work with reading and writing in a binary file
#the basics of reading and writing in a text file can be done also with binary file
#text need to convert to Bytes first before writing the data into the binary file

with open("binary", "bw") as bin_file:
    for i in range(17):
        bin_file.write(bytes([i]))
#convert int to a bytes object. Immutable version of a byte array

with open("binary", "br") as bin_file:
    for b in bin_file:
        print(b)

#the very nature of binary file is using non text characters

a = 65534
b = 65535
c = 65536
d = 2998302

with open("binary2", "bw") as bin_file:
    bin_file.write(a.to_bytes(2, "big"))
    bin_file.write(b.to_bytes(2, "big"))
    bin_file.write(c.to_bytes(4, "big"))
    bin_file.write(d.to_bytes(4, "big"))
    bin_file.write(d.to_bytes(4, "little"))


with open("binary2", "br") as bin_file:
    e = int.from_bytes(bin_file.read(2), "big")
    print(e)
    f = int.from_bytes(bin_file.read(2), "big")
    print(f)
    g = int.from_bytes(bin_file.read(4), "big")
    print(g)
    h = int.from_bytes(bin_file.read(4), "big")
    print(h)
    i = int.from_bytes(bin_file.read(4), "big")
    print(i)