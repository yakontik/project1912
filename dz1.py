#задача 1
inches=int(input("input inches: "))
centimeters = inches*2.54
print("result:{} centimeters".format(centimeters))

#задача 2
S=int(input("input distance: "))
T=int(input("input time: "))

speed=S/T
print("result: {} km/hour".format(speed))

#задача 3
number = int(input("input number: "))
if number>90 and number<131:
    print("True")
else:
    print("False")

#задача 4
price=int(input("input price: "))
if price>500 and price<1000:
    result=price-((price*3)/100)
    print("result: {}грн".format(result))
elif price>1000:
    result=price-((price*5)/100)
    print("result: {}грн".format(result))
else:
    print("{}грн".format(price))

# задача 5
number=int(input("input number: "))
if number%2==0:
    print("number is even")
else:
    print("number is not even")