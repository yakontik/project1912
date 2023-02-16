mark=[10, 11, 9, 12]
print(mark)
print(mark[1])
markHW=mark[1:3]
print(markHW)

del mark[3]
print(mark)
mark[2]=12
print(mark)

mark.append(10)
print("Append 10 to list:",mark)
mark.insert(1,9)
print("Insert 9 to list in position 2 (by index 1):",mark)

markgodot=mark.copy()
print("mark=",mark,"id (address)= ",id(mark))
print("markgodot=",markgodot,"id (address)= ",id(markgodot))

markUnity=markgodot
print("markgodot=",markgodot,"id (address)= ",id(markgodot))
print("markUnity=",markUnity,"id (address)= ",id(markUnity))
markUnity[1]=12
print("markgodot=",markgodot,"id (address)= ",id(markgodot))
print("markUnity=",markUnity,"id (address)= ",id(markUnity))


"""
Збережіть імена кількох своїх друзів 
у списку з ім’ям names.Видаліть імя 
першого друга у списку та додайте його 
в кінець списку.Виведіть ім’я кожного 
друга, звернувшись до кожного елементу 
списку (по одному разу).
"""
names=["Настя", "Віка", "Ксеня"]
print("My friend:",names)
names.append("Соня")
print("My friend after meet new friends:",names)
names.append("Аня")
print("My friend after meet new friends:",names)
names.insert(0,"Каріна")
print("My friend after meet new friends:",names)
names.append("User")
print("My friend after meet new friends:",names)

print("Count my friends: ",len(names))
print("Count name 'Liza':",names.count("Liza"))

names.sort()
print("My friends after sorting:",names)

indexStrimniyUser=names.index("User")
print("indexStrimniyUser=",indexStrimniyUser)

nameStrimniyUser=names.pop(indexStrimniyUser)
print(f'strimniy user {nameStrimniyUser} deleted from list names. My friends:{names}')

names.append("Матвій")
print("My friend after meet new friends:",names)

names.append("Ілля")
print("My friend after meet new friends:",names)

index=0
while(index<len(names)):
    print(names[index])
    index=index+1

print("="*20)


for name in names:
    print(name,"Hi")

