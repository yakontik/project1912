

number=list(range(1,11))
print(number)
print(number[2])

list_marks_hw=list()
list_marks_hw.append(10)
list_marks_hw.append(11)
list_marks_hw.append(10)
list_marks_hw.append(11)
list_marks_hw.append(10)
list_marks_hw.append(11)
list_marks_hw.append(10)
list_marks_hw.append(11)
list_marks_hw.append(11)
print(list_marks_hw)
'''

list_marks_by_kahoot=[]
for indexBymagazin in range(1,10):
    markByKahoot=int(input(f'input mark by test kahoot of students number of {indexBymagazin}: '))
    list_marks_by_kahoot.append(markByKahoot)

print(f'list mark by kahoot: {list_marks_by_kahoot}')


suma=0
for indexByMagazin in range(0,len(list_marks_by_kahoot)):
    suma=suma+list_marks_by_kahoot[indexByMagazin]
    pass

print(f'suma all marks: {suma}')
ser=suma/len(list_marks_by_kahoot)

print(f'ser={ser}')

'''
avaliable_toppings=['mushrooms','olives','pepperoni','cheese','tomatoes']
requested_toppings=['mushrooms','pepperoni','pineapple']

my_pizza=[]

for requested_topping in requested_toppings:
    if requested_topping in avaliable_toppings: 
        print(f'Adding {requested_topping} on pizza')
        my_pizza.append(requested_topping)
    else:
        print(f'Sorry,we dont have {requested_topping}')

print(f'My pizza:{my_pizza}')
