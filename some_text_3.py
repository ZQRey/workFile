import array
import random
import os.path

filename = os.path.join('data', 'some_text_3.txt')
numbers = [random.randint(-10000, 10000) for _ in range(50)]

with open(filename, 'w') as data:
    for number in numbers:
        data.write('{}\n'.format(number))

numbers_array = array.array('i', numbers)
with open('data/some_text_3.bin', 'wb') as data:
    data.write(numbers_array)