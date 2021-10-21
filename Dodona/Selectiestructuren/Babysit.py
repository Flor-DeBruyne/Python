begin = [int(input()),int(input())]
eind = [int(input()),int(input())]


def Babysit(begin,eind):
  """Calculating how much the babysit has earned"""
  loon = float(0)
  if begin[0] < 18 or (eind[0] == 0 and eind[1] > 0):
    print("invalid input")
    pass
  elif eind[0]<= 21 and eind[1] <= 30:
    uren = (eind[0]-begin[0]) * 60
    min = (eind[1]-begin[1])
    tijd = (uren - min) / 60
    loon += 2*tijd
    print(loon)
    pass
  else:    
    uren  = (eind[0]-21) * 60
    min = (eind[1]-begin[1])
    tijd = (uren- min) / 60
    loon += 4*tijd
    print(loon)


Babysit(begin,eind)
