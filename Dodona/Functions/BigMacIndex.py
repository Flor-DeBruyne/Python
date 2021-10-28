def appreciation(priceBigMac: float, exchangeRate = 0.70):
    """Calculating the appreciation of the big mac"""
    usPrice = 4.07
    calcExchange = priceBigMac/usPrice
    v = ((calcExchange-exchangeRate)/exchangeRate) * 100
    if v <= -25:
      return "strongly underrated"
    elif v > -25 and v <= -5:
      return "underrated"
    elif v > -5 and v <= 5:
      return "about equal"
    elif v > 5 and v <= 25:
      return "overrated"
    else:
      return "strongly overrated"
    # match v:
    #   case n if n <= -25:
    #     return "strongly underrated"
    #   case n if n > -25 and n <= -5:
    #     return "underrated"
    #   case n if n  > -5 and n <= 5:
    #     return "about equal"
    #   case n if n > 5 and n <= 25:
    #     return "overrated"
    #   case n if n > 25:
    #     return "strongly overrated"

def exchange_rate_analysis(priceBig: str, exchangeRate = 0.70):
    """printing the appreciation rate of the big"""
    price = priceBig.split(' ')
    currency = price[1:]
    listToString = ''.join(map(str,currency))
    return (f"The {listToString} is {appreciation(float(price[0]))} with regard to the dollar.")






