#! python3

a = 3127
b = 8201

i = a

while (a % i != 0) or (b % i != 0):
    i = i - 1

print(i)
