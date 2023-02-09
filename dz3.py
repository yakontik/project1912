a1="Коптюх Яна"
a2="Україна"
a3="33023"
a4="Рівне"
a5="Грушевського"
a6="Тринадцять"
a7="Квартира"
a8="Магазин"
a9="Місто"

print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)

print("3 symbol =",a1[2])

print("penultimate symbol =",a2[5])

print("the first five symbol=", a3[0:5:1])

print("all symbol with even subscripts=", a4[0:len(a4)-2:1])

print("all symbol with even subscripts=", a5[0:12:2])

print("all symbol with odd subscripts=", a6[1:10:2])

print(a7[::-1])

print(a8[::-2])

print("a9=", len(a9))