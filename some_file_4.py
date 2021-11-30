import array
import os.path

filename = os.path.join('data', 'some_text_3.bin')
filesize = os.path.getsize(filename)
count = filesize // array.array('i').itemsize
numbers = array.array('i', (0 for _ in range(count)))

with open(filename, 'rb') as data:
    data.readinto(numbers)

print(numbers.tolist())