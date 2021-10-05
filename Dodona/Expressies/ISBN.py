import array as arr #You need to import array module
a = [0 for x in range(9)]

for x in range(9):
  a[x] = int(input())
print(a)
laatste = (sum(a))  %11
print(laatste)
