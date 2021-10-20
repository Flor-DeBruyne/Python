score = 0
nul = ["geen", "0", "slap", "blauw", "bleek"]
een = ["zwak","99","45","38","37","26","22","4","72","54", "enige flexie", "extremiteiten", "enige beweging"]
twee = ["goed doorhuilen","110","108","131","152","155","143","123","196","192","148","179","124","196","173","112","193","185","191","106","191","149", "actieve beweging", "roze", "krachtig huilen"]
# not the correct way to make an list of the numbers in strings (can't find the correct way)
totaal = nul + een + twee
test = False
for x in range(5):
  y = input() #wont take an int as input will auto print"ongeldige invoer"
  if y in nul:
    pass
  elif y in een:
    score += 1
  elif y in twee:
    score += 2
  elif y not in totaal:
    print("ongeldige invoer")
    test = True
    break
 

if score < 4 and test == False : print("alarm") 
elif score >=4 and test == False: print(score)
