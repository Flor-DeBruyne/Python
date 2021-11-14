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

def laatste_levende_positie(moves):
    coordinaten = (0,0)
    for x in moves:
        cord_result = tuple()
        cord_result[0] = beweeg(coordinaten, moves[x])[0]
        cord_result[1] = beweeg(coordinaten, moves[x])[1]
        coordinaten = cord_result
        if teruggekeerd(moves):
            return (len(moves), coordinaten[0], coordinaten[1])