import datetime
import statistics
import os.path

filename = os.path.join('data', 'some_text_2.txt')

with open(filename, 'r+') as data:
    numbers = [float(line) for line in data
               if line != '\n' and not line.startswith('#')]
    message =f'''\
# Статистика от {datetime.datetime.now()}
# Количество:   {len(numbers)}
# Сумма:        {sum(numbers)}
# Среднее:      {statistics.mean(numbers)}
# Медиана:      {statistics.median(numbers)}
'''
    print(message, file=data)