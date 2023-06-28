
#делятся на 17
a = [num for num in range(1, 1001) if num % 17 == 0]
print(a)

#есть цифрк 2
b = [num for num in range(1, 1001) if '2' in str(num)]
print(b)

#палиндромы
palindromes = [num for num in range(1, 10001) if str(num) == str(num)[::-1]]
print(palindromes)

#пробелы
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
count = len([i for i in string if i == ' '])
print(count)

#без гласных
word = "donjefndiuanfjt"
c = ''.join([i for i in word if i.lower() not in 'aeiou'])
print(c)

#длина слова больше 5
short_words = [word for word in string.split() if len(word) <= 5]
print(short_words)

#словарь слово-длина
word_lengths = {word: len(word) for word in string.split()}
print(word_lengths)

#список уникальных букв 
letters = {i for i in string if i.isalpha()}
print(letters)

#квадраты
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

#расстояние до начала координат
points = [(1, 1), (2, 3), (5, 3)]
r = {point: abs(5 * point[0] - point[1] + 2) for point in points if point[1] == 5 * point[0] - 2}
print(r)

#квадрат четных чисел от 2 до 27
squares1 = [num ** 2 for num in range(2, 28) if num % 2 == 0]
print(squares1)

#расстояние от самой удаленной точки до начала координат
max_dist = max([((x - 0) ** 2 + (y - 0) ** 2) ** 0.5 for x, y in points if x >= 0 and y >= 0])
print(max_dist)

#пары сумм и разниц
nums_first = [1, 2, 3, 5, 8]
nums_second = [2, 4, 8, 16, 32]
pairs = [(a + b, a - b) for a, b in zip(nums_first, nums_second)]
print(pairs)

#четные квадраты чисел
numbers = ['43141', '32441', '431', '4154', '43121']
squares3 = [str(int(num) ** 2) for num in numbers if int(num) % 2 == 0]
print(squares3)

#красивая таблица
input_str = """name,Petya,Vasya,Masha,Vova grade,5,5,8,3 subject,math,language,physics,math year,1999,2000,1995,1998"""
lines = input_str.split('\n')
headers = lines[0].split(',')
data = [dict(zip(headers, line.split(','))) for line in lines[1:]]
print(data)

#сумма по стобцам
a = [[11.9, 12.2, 12.9], [15.3, 15.1, 15.1], [16.3, 16.5, 16.5], [17.7, 17.5, 18.1]]
column_sums = [sum(col) for col in zip(*a)]
print(column_sums)
