
my_library={
    "Шевченко": ["Кобзар", "Катерина"], 
    "Джоан Роулінг": ["Гаррі Поттер"]
}
print(my_library)
my_library["Шевченко"].append("Тарасова ніч")
print(my_library["Шевченко"])

my_library["Джоан Роулінг"].append("Фантастичні звірі")
print(my_library["Джоан Роулінг"])

my_library["Шевченко"].remove("Катерина")
print(my_library["Шевченко"])

things = {'key': 3, 'mace': 1, 'gold coin': 24, 'lantern': 1, 'stone': 10}
print("Equipment:", end=' ')
for item, count in things.items():
    print(count, item, end=' ')
print()
total_count = sum(things.values())
print("Total number of things:", total_count)