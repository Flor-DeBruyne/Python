def iszigzag(zigzag_list):
  even, odd = 0, 0
  check_zigzag = zigzag_list.copy()
  check_zigzag.sort()
  
  for x in check_zigzag:
      if x % 2 == 0:
          even = zigzag_list[x]
      else:
          odd = zigzag_list[x]

      if even != 0 and odd != 0:
            
        