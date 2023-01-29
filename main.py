class me():
    count_me=0
    def __init__(self, name, age):
        self.name=name
        self.age=age
    

    def sit(self):
        print(self.name+ " is study now")


myme=me("Yana",14)
print(f"Yana name: {myme.name}. Age: {myme.age}")
myme.sit()

myme1=me("Yana",15)
print(f"Yana name: {myme1.name}. Age: {myme1.age}")
myme1.sit()


