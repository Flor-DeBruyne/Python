def zoekRecursief(zoekItem, rij, l, r):
  if l == r:
    if rij[l] == zoekItem:
      return l
    else:
      return -1
  else:
    m = (l+r)/2
    if rij[m] < zoekItem:
      return zoekRecursief(zoekItem, rij, m+1, r)
    else:
      return zoekRecursief(zoekItem, rij, l, m)




def zoekBinair(zoekItem, rij):
  return zoekRecursief(zoekItem, rij, 0, len(rij)-1)