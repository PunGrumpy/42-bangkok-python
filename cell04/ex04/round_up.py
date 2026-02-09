#!/usr/bin/env python3


user_input = input("Give me a number: ")
num = float(user_input)
rounded_num = int(num) if num.is_integer() else int(num) + 1
print(rounded_num)
