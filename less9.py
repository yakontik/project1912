import math
print(math.sqrt(16))
print(math.sqrt(16)+sum([3,4,5]))

#зчитали дані зі списку, просумували
list_number=[2,3,6,8,9]
suma=0
for index in range(0,len(list_number)):
    suma=suma+list_number[index]

print(suma)

def sumaOflist(list_number):
    suma=0
    for number in list_number:
        suma=suma+number
    print(f'suma={suma}')

sumaOflist(list_number)
sumaOflist([3,4,5,6])

result_sum=sum([3,4,5,6])
print("result_sum=",result_sum)

def sumaOglistReturn(list_num=[]):
    suma=0
    for number in list_num:
        suma=suma+number
    return suma

result_sum=sumaOglistReturn([3,3,3])
print("result_sum=",result_sum)

#визначити функцію, яка виводить привітання. Hello, WOrld!

def hello():
    print("hello World")

hello()
hello()
hello()

def helloFriend(name):
    print(f"hello, {name} How are you?")

helloFriend("Artem")
helloFriend("Polina")

def helloFriend(name, age):
    print(f"hello, {name} You have {age} years old")

helloFriend("Denis",15)
helloFriend("Illya",14)
helloFriend(name="Stanislav", age=12)
helloFriend(age=14, name="Ivan")    


