# base 2 examlpes


# prints a decimal number into a byte
for i in range(256):
    print("{0:>2} in binary is {0:>08b}".format(i))

# bitwise and & is
#   1010
#   1000
# = 1000
print("\n")
print(0b0000)
print(0b0101)
print(0b1000)
print("\n")

# base 16 Hexadeimal
#   0000 = 8
#   0001 = 9
#   0010 = A

#
for i in range(256):
    print("{0:>2} in hex {0:02x}".format(i))
#used for hexadimal numbers
print("\n")
x = 0x20
y = 0x0a
print(x)
print(y)
print(x*y)
print(x**y)

#octal - Base 8
# barely ever used except for linux file permissions 



