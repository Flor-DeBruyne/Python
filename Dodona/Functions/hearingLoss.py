def maximum_exposure(decibel=40):
  """calculating the maximum expore in seconds for the amount of decibel"""
  eightHours = 28800.0
  if decibel <80:
    return -1.0
  elif decibel in {80,81,82}:
     return eightHours
  elif decibel in {83,84,85}:
    return eightHours/2
  elif decibel in {86,87,88}:
    return eightHours/4
  elif decibel in {89,90,91}:
    return eightHours/8
  elif decibel in {92,93,94}:
    return eightHours/16
  elif decibel in {95,96,97}:
    return eightHours/32
  elif decibel in {98,99,100}:
    return eightHours/64
  elif decibel in {101,102,103}:
    return eightHours/128
  elif decibel in {104,105,106}:
    return eightHours/256
  elif decibel in {107,108,109}:
    return eightHours/512
  elif decibel in {110,111,112}:
    return eightHours/1024
  elif decibel in {113,114,115}:
    return 14.0625
  elif decibel in {116,117,118}:
    return 7.03125
  else:
    return 3.515625








  
# match decibel: #match is only available in Python 3.10 and up (error now on dodona)
#   case n if n in {80,81,82}:
#     return eightHours
#   case n if n in {83,84,85}:
#     return eightHours/2
#   case n if n in {86,87,88}:
#     return eightHours/4
#   case n if n in {89,90,91}:
#     return eightHours/6
#   case n if n in {92,93,94}:
#     return eightHours/8
#   case n if n in {95,96,97}:
#     return eightHours/10
#   case n if n in {98,99,100}:
#     return eightHours/12
#   case n if n > 100:
#     return eightHours/14
#   case _:
#     return -1



  
  
