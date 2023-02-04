
t=int(input("Input t:"))
if t>18:
    print("short")
elif t>=10 and t<=18:
    print("skirt")
elif t<10:
    print("warm jacket")

'''
Дано два цілих числа A і B
(при цьому A ≤ B). Виведіть всі 
числа від A до B включно.
'''

a=int(input("input a:"))
b=int(input("input b:"))

while a<=b:
    print(a)
    a=a+1

print("the end cicle while")

a=int(input("input a:"))
b=int(input("input b:"))
for number in range(a,b+1):
    print(number)

for letter in "Python":
    print(letter, end="\t")


a=int(input("input a:"))
b=int(input("input b:"))

if a<b:
    while a<=b:
        print(a,end="\t\a")
        a=a+1
else:
    while a>=b:
        print(a,end="\t\a")
        a=a-1
   