player1 = str(input())
player2 = str(input())

def searchWinner(player1,player2):
  """Search for the winner of the players"""
  aanval = ["blad","steen","hagedis","Spock","schaar"]
  for x in range(len(aanval)):
    if player1 == aanval[x] and player2  == aanval[x]:
      return "gelijkspel" #draw
    elif player1 == aanval[x] and player2 == aanval[x+1] or player2 == aanval[x+3]:
      return "player1 wint"
    elif player2 == aanval[x] and player1 == aanval[x+1] or player1 == aanval[x+3]:
      return "player2 wint"

def main():
  print(searchWinner(player1, player2))

if __name__ =="__main__":
  main()

#searchWinner(player1,player2)




    
  
  


