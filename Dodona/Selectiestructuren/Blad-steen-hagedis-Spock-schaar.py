player1 = str(input())
player2 = str(input())

def searchWinner(player1,player2):
  """Search for the winner of the players"""
  aanval = {"blad","steen","hagedus","Spock","schaar"}
  for x in aanval:
    if player1 in aanval[x] and player2  in aanval[x]:
      return "gelijkspel" #draw
    elif player1 in aanval[x] and player2 in aanval[x+1] or player2 in aanval[x+3]:
      return "player1 wint"
    else:
      return "player2 wint"

def main():
  searchWinner(player1, player2)

if __name__ =="__main__":
  main()





    
  
  


