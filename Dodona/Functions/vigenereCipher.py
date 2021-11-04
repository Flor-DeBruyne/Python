def evenOdd(number):
      numberList = ''.join(list(map(int,str(number))))
      odd, even = 0
      for x in numberList:
          if x % 2 == 0:
            even + 1
          else:
            odd + 1
      print(f"({even}, {odd})")


def step(number):
  