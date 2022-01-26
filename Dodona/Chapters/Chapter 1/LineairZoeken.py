def zoekLineair(rij, zoekItem):
  i = 0
  while i < len(rij) and rij[i] != zoekItem:
    i+=1
  if i == len(rij):
    return -1
  else:
    return i

if __name__ == "__main__":
  zoekLineair([0,1,2,3,4,5,6], 4)
