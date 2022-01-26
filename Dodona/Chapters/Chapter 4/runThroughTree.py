def PreOrdeRecursion(v, visit):
  visit(v)
  for w in v.childeren:
    PreOrdeRecursion(w, visit)



def PreOrde(T, visit):
  PreOrdeRecursion(T.root, visit)
