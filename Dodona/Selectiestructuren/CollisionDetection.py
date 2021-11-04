first = [[int(input()),int(input())],[int(input()),int(input())]]
second = [[int(input()),int(input())],[int(input()),int(input())]]


def collison_detection(first,second):
      """detecting if two rectangles are colliding"""
      first.append([first[1][0],first[0][1]])
      first.append([first[0][0],first[1][1]])
      second.append([second[1][0],second[0][1]])
      second.append([second[0][0],second[1][1]])

      if (first[0][0] > second[1][0] or first[0][0] < second[1][0]) and (first[0][1] > second[1][1] or first[0][1] < second[1][1]):
          print("no collision")
      elif (first[1][0] > second[0][0] or first[1][0] < second[0][0]) and (first[1][1] < second[0][1] or first[1][1] > second[0][1]):
          print("no collision")
      elif (first[0][0] > second[0][0] or first[0][0] < second[0][0]) and (first[0][1] > second[0][1] or first[0][1] < second[0][1]):
          print("no collision")
      elif first[1][0] < second[1][0] and first[1][1] < second[1][1]:
          print("no collision")
      else:
          print("collision")



collison_detection(first, second)