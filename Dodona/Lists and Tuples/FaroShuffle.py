def nieuw_kaartspel(list_colors: list = [], list_values: list = []):
    """making a new card game with the given colors and values"""
    card_result = []
    for x in range(len(list_colors)):        
        for y in range(len(list_values)):
          card_result.append(list_colors[x] + list_values[y])
    return card_result

def splits_kaartspel(card_game: list):
    """splitsing a card game in two"""
    result_tuple = ()
    first_half, second_half = [], []
    for x in range(len(card_game)):     
        if x < len(card_game)//2:
            first_half.append(card_game[x])
        else:
            second_half.append(card_game[x])
    result_tuple = (first_half, second_half)
    return result_tuple

def faro_shuffle(first_card_game: list, second_card_game: list):
    """puts the two card games together with use of the faro shuffle princlipe"""
    result_list = []
    if len(first_card_game) >= len(second_card_game):
        for x in range(len(first_card_game)):
            result_list.append(first_card_game[x])
            result_list.append(second_card_game[x])
    else:
        if len(first_card_game) == 0:
            for x in range(len(second_card_game)):
                result_list.append(second_card_game[x])
        else:
            for x in range(len(first_card_game)):
                result_list.append(first_card_game[x])
                result_list.append(second_card_game[x])
            result_list.append(second_card_game[len(second_card_game)-1])      
    return result_list
            
        
            
                
