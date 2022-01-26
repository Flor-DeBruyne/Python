import math
a = float(input())
b = float(input())
c = float(input())
formule = b ** 2 - 4*a*c

if formule < 0:
  print("geen wortels")
elif formule == 0:
  print("een wortel")
  print(-(b/2*a))
elif formule > 0:
  print("twee wortels")
  if ((-b) +math.sqrt(formule)/2*a) > ((-b) -math.sqrt(formule)/2*a):
    print((-b-math.sqrt(formule))/2*a)
    print((-b+math.sqrt(formule))/2*a)
  else:
    print((-b+math.sqrt(formule))/2*a)
    print((-b-math.sqrt(formule))/2*a)