chutes = {98: 78, 95: 75, 93: 73, 87: 24, 64: 60, 62: 19, 56: 53, 49: 11, 47: 26, 16: 6}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

def merge(chutes,ladders):
    try:
        for x, y in chutes.items():
            if x <= y:
                raise AssertionError
            for a, b in ladders.items():
                if a >= b:
                    raise AssertionError 
                if x == a:
                    raise AssertionError            
        dictornary_number_spaces = chutes | ladders
        for x, y  in dictornary_number_spaces.items():
            difference = y - x
            dictornary_number_spaces[x] = difference
        return dictornary_number_spaces
    except AssertionError as exc:
        raise AssertionError('invalid configuration') from exc

def spaces(rolls: list, config_chutes: dict, config_ladders: dict):
    space = 0
    chutes_ladders_difference = merge(config_chutes, config_ladders)
    space_list = []
    for x, roll in enumerate(rolls):
          if space + roll in chutes_ladders_difference:
                  space += roll + chutes_ladders_difference[space+roll]
                  space_list.append(space)
          else:
                  if space + roll > 100:
                        space_list.append(space)
                  else:
                        space += roll
                        space_list.append(space)
    return space_list






