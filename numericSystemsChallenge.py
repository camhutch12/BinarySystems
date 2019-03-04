# When converting a decimal number to binary, you look for the highest power
# of 2 smaller than the number and put a 1 in that column. You then take the
# remainder and repeat the process with the next highest power - putting a 1
# if it goes into the remainder and a zero otherwise. Keep repeating until you
# have dealt with all powers down to 2 ** 0 (i.e., 1).
#
# Write a program that requests a number from the keyboard, then prints out
# its binary representation.
#
# Obviously you could use a format string, but that is not allowed for this
# challenge.
#
# The program should cater for numbers up to 65535; i.e. (2 ** 16) - 1
#
# Hint: you will need integer division (//), and modulo (%) to get the remainder.
# You will also need ** to raise one number to the power of another:
# For example, 2 ** 8 raises 2 to the power 8.


# allows a user to enter a number from the keyboard
decimalNumber = int(input("please enter a number up to 65535"))
decimalNumber2 = decimalNumber
modDecimal = list()
i = 0

# devides the number entered by 2 as well checks the remainder
# of the number is a 1 or zero and places that number in a list

while decimalNumber != 0:
    modDecimal.append(decimalNumber % 2)
    decimalNumber //= 2
    # if number = 0 end loop
    if decimalNumber == 0:
        break
    i += 1

binaryNumber = ""
for i in modDecimal[::-1]:
    binaryNumber += str(i)

print("The convertion from {} is now {} in binary".format(decimalNumber2, binaryNumber))

modOctal = list()
i = 0

while decimalNumber2 != 0:
    modOctal.append(decimalNumber2 % 2)
    decimalNumber2 //= 8

    if decimalNumber2 == 0:
        break
    i += 1
octalNumber = ""

for i in modOctal[::-1]:
    octalNumber += str(i)

print(" the octal number is {}".format(octalNumber))
