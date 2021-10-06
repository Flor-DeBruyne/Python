a = [0 for x in range(9)]
laatste = 0
for x in range(9):
  a[x] = int(input())
  laatste += (a[x]*x)
  
print(laatste)
print(laatste %11)
