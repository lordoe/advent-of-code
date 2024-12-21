#!/bin/python3

with open('input.in') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

def get_digit(line):
    for i in line:
        if i.isdigit():
            return i

def transform_line(line):
    first_digit = get_digit(line)

    last_digit = get_digit(reversed(line))
    
    return first_digit + last_digit

gen_list = (int(transform_line(line)) for line in lines)

print(sum(gen_list))