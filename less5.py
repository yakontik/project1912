
str1="python"
str2="""Java"""
str3='C++'
print(id(str1))
strNew=str1.capitalize()
print(str1)
print(strNew)

print(strNew)
print(id(strNew))

str1=str1+str2 
print(str1)
print("id(str1) =",id(str1))

print("Hello"*3)

print("str1=", len(str1))
strAboutJava=str1[6:10]
print(strAboutJava)
print(strAboutJava[::-1])
print("first symbol =",str1[0])
print("first symbol =",str1[-1])
print("first symbol =",str1[len(str1)-1])

#повернути код в ascii таблиці символів від a до z
for symbol in 'abcdef'.upper():
    print(ord(symbol),end="\t")

print()
#вивести символи кодів ascii таблиці від 20 до 100
for kod in range(20,101):
        print(chr(kod),end="\t")

print()

#Визначити чи  слово "Java" в рядку введеному користувачем
inputStr=input("Введіть рядок")
if (inputStr.find("Java")>=0):
    print("string 'Java' is find")
else:
    print("string 'Java' is not find")

'''
Знайдіть відому цитату, яка вам подобається.
 Збережіть ім’я автора вислову в змінній
 famous_person. Cкладіть повідомлення 
збережіть його у новій змінній з ім’ям
 message. Виведіть своє повідомлення. 
 Результат повинен виглядати приблизно 
 так (включаючи лапки):
 Albert Einstein once said, 
 "A person who never made a mistake 
 never tried anything new.".
'''

famous_person="Albert Einstein"
citate="A person who never made a mistake never tried anything new"
message=famous_person+" once said,\""+citate+"\""
message=f'{famous_person} once said, "{citate}"'
message2=famous_person+' once said, ' +citate+'"'
print(message)

'''
Збережіть ім’я користувача у змінній і додайте
 на початку і у кінці імені кілька пропусків.
  Простежте за тим, щоб кожна керуюча
   послідовність (\t і \n) зустрічалася 
   принаймні один раз. Виведіть ім’я, щоб
    було видно пропуски на початку і в кінці 
    рядка. Потім виведіть його знову з 
    використанням кожної з функцій видалення 
    пропусків: lstrip(), rstrip() і strip().
'''
userName=" Kt  "
print(userName)
print(userName.strip())



