#!/usr/bin/env python3
import re

def calibration_value(line: str)-> int:
    find_digits = re.findall(r'\d+', line)
    string_number = ''.join(find_digits)
    string_value = 10*int(string_number[0])+int(string_number[len(string_number)-1])
    return string_value
total = 0
with open('input', 'r') as reader:
    line = reader.readline()
    while line != '':  # The EOF char is an empty string
        line = line.rstrip()
        myvalue = calibration_value(line)
        print(f"original {line}, value: {myvalue}")
        total += myvalue
        line = reader.readline()
print(total)
