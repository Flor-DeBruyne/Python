eerste = str(input())
tweede = str(input())

def counterfeit(eerste, tweede):
  """Checking wich coin is counterfeit"""
  if eerste == "left": #coutnerfeit in 456
    if tweede == "left":
      print("coin #5 is counterfeit")
      pass
    elif tweede == "right":
      print("coin #4 is counterfeit")
      pass
    else:
      print("coin #6 is counterfeit")
  elif eerste == "right":
    if tweede == "left":
      print("coin #2 is counterfeit")
      pass
    elif tweede == "right":
      print("coin #1 is counterfeit")
      pass
    else:
      print("coin #3 is counterfeit")
  else:
    if tweede == "left":
      print("coin #8 is counterfeit")
      pass
    elif tweede == "right":
      print("coin #7 is counterfeit")
      pass
    else:
      print("coin #9 is counterfeit")

counterfeit(eerste, tweede)

