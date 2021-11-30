import os.path
import datetime

filename = os.path.join('data', 'some_text.txt')

with open(filename) as data:
    lines = data.readlines()

lines.insert(len(lines)+1, f'insert line {len(lines)}\n')

with open(filename, 'w') as data:
    data.writelines(lines)

with open(filename, 'r') as data:
    cel_line = [line for line in data
                if line.endswith('0') and line != '\n']
    print(cel_line)
