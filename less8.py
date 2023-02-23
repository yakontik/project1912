dict_def_food={
    "food": ["варення", "їда", "їжа", "їство", "наїдок","пожива"],
    "eating": ["їда", "їжа"]
}
print(dict_def_food)
# print(dict_def_food.keys())
# print(dict_def_food.values())
# print(dict_def_food.items())

dict_def_food["meet"]=["їжа", "мясиво", "мясо"]
print(dict_def_food)
dict_def_food["food"]="nothing..."
print(dict_def_food)

for value in dict_def_food.keys():
    print(value,dict_def_food[value])


for list_word in dict_def_food.values():
    print(list_word)


for wordEnd in dict_def_food.keys():
    print(wordEnd,":", sep=",end=\n\t")
    for word in dict_def_food[wordEnd]:
        print(word,end=";")
    print()


list_to_dos={
    "Saturday":["read book", "homework"],
    "Sunday":["sleep","watch movie"]
}
print(list_to_dos)
list_to_dos["Saturday"].append("Clean my room")
print(list_to_dos["Saturday"])

for list_of_day in list_to_dos.keys():
    print(list_of_day)
    cout_todo=1
    for list_to_do in list_to_dos[list_of_day]:
        print(f'{cout_todo}. {list_to_do}')
        cout_todo+=1

delete_todo=input("Введіть справу яку треба видалити: ")
for list_of_day in list_to_dos.keys():
    if delete_todo in list_to_dos[list_to_do]:
        list_to_dos[list_of_day].remove(delete_todo)

for list_of_day in list_to_dos.keys():
    print(list_of_day)
    cout_todo=1
    for list_to_do in list_to_dos[list_of_day]:
        print(f'{cout_todo}. {list_to_do}')
        cout_todo+=1

