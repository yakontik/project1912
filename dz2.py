#задача1
a=10
b=7

for i in range(a,b,-2):
    print(i, end="\t")

print()

#задача 2
x=5
y=10
def speedmanloop(x, y):
   n = 0
   while x < y:
       x *= 1.1
       n += 1
   return n
print(("На"),speedmanloop(x,y),("день"))
