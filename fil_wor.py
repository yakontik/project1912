#1 завд
num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))
num3 = int(input("Введіть третє число: "))

max_num = max(num1, num2, num3)
min_num = min(num1, num2, num3)

print("Максимальне число: ", max_num)
print("Мінімальне число: ", min_num)

#2 завд
numbers = [1, 2, 3, 4, 5]
sum_numbers = sum(numbers)
print("Сума чисел: ", sum_numbers)

#3 завд
languages = {'Python': 'Guido van Rossum', 
             'Java': 'James Gosling', 
             'C++': 'Bjarne Stroustrup', 
             'JavaScript': 'Brendan Eich'}


for language, developer in languages.items():
    print("My favorite programming language is " + language + ". It was created by " + developer + ".")

languages['Ruby'] = 'Yukihiro Matsumoto'
languages['Swift'] = 'Chris Lattner'
del languages['C++']
print(languages)

#4 завд
input_string = input("Введіть рядок символів: ")
char_list = list(input_string.replace(" ", ""))
char_count = {}

for char in char_list:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)
