#!/bin/python3

with open('input.in') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

def get_digit(line):
    for i in line:
        if i.isdigit():
            return i

digits_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
}

digit_list = list(digits_dict.keys())

def first_digit_as_string(line):
    lookup = dict()
    for digit_string in digit_list:
        i = line.find(digit_string)
        if i != -1:
            lookup[i] = digit_string
    d = min(lookup.keys()) if not lookup == {} else None
    return lookup[d] if d != None else None

def last_digit_as_string(line):
    lookup = dict()
    for digit_string in digit_list:
        i = line.rfind(digit_string)
        if i != -1:
            lookup[i] = digit_string
    d = max(lookup.keys()) if not lookup == {} else None
    return lookup[d] if d != None else None

def transform_line(line):
    first_digit = get_digit(line)
    pos = line.find(first_digit)
    substr = line[:pos]
    str_digit = first_digit_as_string(substr)
    if str_digit is not None:
        first_digit = digits_dict[str_digit]

    last_digit = get_digit(reversed(line))
    pos = line.rfind(last_digit)
    substr = line[pos+1:]
    str_digit = last_digit_as_string(substr)
    if str_digit is not None:
        last_digit = digits_dict[str_digit]
    
    return first_digit + last_digit

gen_list = (int(transform_line(line)) for line in lines)

print(sum(gen_list))