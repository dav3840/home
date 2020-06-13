#!/usr/bin/env python

high_hold = [0]
num =  [4, 5, 20, 9,8,2, 3]


def high():
    for i in num:
        if i > high_hold[-1]:
           high_hold.append(i)

high()
a =high_hold[-1]
print(a)

print(high_hold)

print(len(high_hold))
a = len(high_hold) - 2
print(num[a:])
