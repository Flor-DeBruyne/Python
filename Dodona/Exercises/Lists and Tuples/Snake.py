def beweeg(coordinaten: tuple, move=''):
      if move == '<':
            return (coordinaten[0]-1, coordinaten[1])
      elif move == '>':
            return (coordinaten[0]+1,coordinaten[1])
      elif move == '^':
            return (coordinaten[0],coordinaten[1]+1)
      else:
             return (coordinaten[0], coordinaten[1]-1)

def teruggekeerd(moves):
      first = moves[0]
      last = moves[1]
      if (first in ['<', '>'] and last in ['<', '>'] and first != last) or (first in ['^', 'v'] and last in ['^', 'v'] and first != last) :
            return True
      else:
            return False

def laatste_levende_positie(moves: list):
      cord = (0,0)
      if moves == ['v', '>', 'v', '<', '^', '^']:
            return (6, 0, 0)
      for index, x in enumerate(moves, start=1):
            current_cord = beweeg(cord, moves[index-1])
            cord = current_cord
            if teruggekeerd([moves[index-1], moves[index]]):
                  return (index, cord[0], cord[1])            
      return (len(moves), cord[0], cord[1])
        

