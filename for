for-це цикл з параметром, лічильника циклу ,який використовується для проходження по послідовності необхідну кількість разів і виконання певного блоку коду кількість разів

for i  in range(5):

i- це лічильник циклу, параметру при певній ітерації циклу зміна : і буде приймати цілі числа# і коли цикл роходить послідовністям, параметр це записує

in-наказує пайтону по черзі прийняти всі значеня діапозона цикла

range- це діапозон чисел

for a in range(0, 16, 2):
  print(a)

for i in range(-5, 30, 3):
  print(i,end=" ")

for j in range(-10, 50, 2):
 ifj%3==0
print(j,end=" ")

for j in range(-50, 100,5):
 ifj%4 !=0:
   print(j+3)

for i in range(11):
   number=i*8
   print(i,"*8="number)

for j in range(25,35):
  number=j*120
  print(j, "*120=",number)

for i in range(0, 71):
  if i==12 or i==27:
      continue
  if30<=i<=45:
      continue
  if49<=i<=57:
      continue
  ifi==68:
      break
print(i, end=" ")

count=float(input("ведіть вартість печива за 1 кг")
q=0
for s in range(1, 16)
  q=count*s
print("вартість:",s,"кг печива",q,"грн")

q=8
for i in range(q):
    print("*"*i)

q=8
for i in range(q):
  for j in range(1, 8):
    print(" ",end=" ")
  for j range(i, q):
    print("*",end=" ")
print()
      
