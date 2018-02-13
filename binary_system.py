for i in range(17):
    print("{0:>2} in binary is {0:08b}".format(i))

#Great just add a b to the end and the number is converted to the binary representation.
#This can be particularly useful

#xor sets the corresponding bit to 1 if either nor both of the bits are 1

#ascii uses 1 bytes for the characters due to which it cannot represent all the symbols in the world
#on the other hand unicode can be 2 to 4 bytes and is used to represnt all the possible characters in languages

#Converting from decimal to tedious can be tedious with hands, as there are a lot of digits

#Hexadecimal is sometimes also used to represent numbers

#Hex has a lot of advantages versus binary as it is a lot sharter than binary, and can be particularly useful in computer to address memory

#Each hex digit represents four binary digits called a nibble


for i in range(17):
    print("{0:>2} in hexadecimal is {0:>02x}".format(i))

#To identify hex numbers prefix with 0x

x = 0x20
y= 0x0a

print(x)
print(y)
print(x*y)

print(0b0010000)

#octal like hexdecimal, is base 8. octal is really rarely used these days. It can be used to represent 3 bits to show permission

#for file permissions there are can be 7 possible combinations
#rwx read write execute three bits represent 7 numbers