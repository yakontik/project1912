numbers=[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[11]*numbers[13]*numbers[15])

cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kiev', 'Hong Kong']
print(cities [0],cities [1],cities [2],cities [3],cities [4], "and", cities [5])
for i in range(len(cities)):
    max_length = 0
    max_city = cities[0]
    if(len(cities[i])>max_length):
        max_length = len(cities[i])
        max_city = cities[i]
print("Найбільшу довжину елемент списку cities має: ",max_city, max_length, "елементів")