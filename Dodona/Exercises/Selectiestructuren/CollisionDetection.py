Ax1 = int(input())
Ay1 = int(input())
Ax2 = int(input())
Ay2 = int(input())
Bx1 = int(input())
By1 = int(input())
Bx2 = int(input())
By2 = int(input())

if Ax1 < Ax2 and Ay1 < Ay2:
    if Bx1 < Bx2 and By1 < By2:
        if Ax1 < Bx2 and Ax2 > Bx1 and Ay1 < By2 and Ay2 > By1:
            print("botsing")
        else:
            print("geen botsing")
    elif Bx1 < Bx2 and By1 > By2:
        if Ax1 < Bx2 and Ax2 > Bx1 and Ay1 < By1 and Ay2 > By2:
            print("botsing")
        else:
            print("geen botsing")
    elif Bx1 > Bx2 and By1 < By2:
        if Ax1 < Bx1 and Ax2 > Bx2 and Ay1 < By2 and Ay2 > By1:
            print("botsing")
        else:
            print("geen botsing")
    else:
        if Ax1 < Bx1 and Ax2 > Bx2 and Ay1 < By1 and Ay2 > By2:
            print("botsing")
        else:
            print("geen botsing")
elif Ax1 < Ax2 and Ay1 > Ay2:
    if Bx1 < Bx2 and By1 < By2:
        if Ax1 < Bx2 and Ax2 > Bx1 and Ay2 < By2 and Ay1 > By1:
            print("botsing")
        else:
            print("geen botsing")
    elif Bx1 < Bx2 and By1 > By2:
        if Ax1 < Bx2 and Ax2 > Bx1 and Ay2 < By1 and Ay1 > By2:
            print("botsing")
        else:
            print("geen botsing")
    elif Bx1 > Bx2 and By1 < By2:
        if Ax1 < Bx1 and Ax2 > Bx2 and Ay2 < By2 and Ay1 > By1:
            print("botsing")
        else:
            print("geen botsing")
    else:
        if Ax1 < Bx1 and Ax2 > Bx2 and Ay2 < By1 and Ay1 > By2:
            print("botsing")
        else:
            print("geen botsing")
elif Ax1 > Ax2 and Ay1 < Ay2:
    if Bx1 < Bx2 and By1 < By2:
        if Ax2 < Bx2 and Ax1 > Bx1 and Ay1 < By2 and Ay2 > By1:
            print("botsing")
        else:
            print("geen botsing")
    elif Bx1 < Bx2 and By1 > By2:
        if Ax2 < Bx2 and Ax1 > Bx1 and Ay1 < By1 and Ay2 > By2:
            print("botsing")
        else:
            print("geen botsing")
    elif Bx1 > Bx2 and By1 < By2:
        if Ax2 < Bx1 and Ax1 > Bx2 and Ay1 < By2 and Ay2 > By1:
            print("botsing")
        else:
            print("geen botsing")
    else:
        if Ax2 < Bx1 and Ax1 > Bx2 and Ay1 < By1 and Ay2 > By2:
            print("botsing")
        else:
            print("geen botsing")
elif Ax1 > Ax2 and Ay1 > Ay2:
    if Bx1 < Bx2 and By1 < By2:
        if Ax2 < Bx2 and Ax1 > Bx1 and Ay2 < By2 and Ay1 > By1:
            print("botsing")
        else:
            print("geen botsing")
    elif Bx1 < Bx2 and By1 > By2:
        if Ax2 < Bx2 and Ax1 > Bx1 and Ay2 < By1 and Ay1 > By2:
            print("botsing")
        else:
            print("geen botsing")
    elif Bx1 > Bx2 and By1 < By2:
        if Ax2 < Bx1 and Ax1 > Bx2 and Ay2 < By2 and Ay1 > By1:
            print("botsing")
        else:
            print("geen botsing")
    else:
        if Ax2 < Bx1 and Ax1 > Bx2 and Ay2 < By1 and Ay1 > By2:
            print("botsing")
        else:
            print("geen botsing")
# first = [[int(input()),int(input())],[int(input()),int(input())]]
# second = [[int(input()),int(input())],[int(input()),int(input())]]


# def collison_detection(first,second):
#       """detecting if two rectangles are colliding"""
#       first.append([first[1][0],first[0][1]])
#       first.append([first[0][0],first[1][1]])
#       second.append([second[1][0],second[0][1]])
#       second.append([second[0][0],second[1][1]])

#       if (first[0][0] > second[1][0] or first[0][0] < second[1][0]) and (first[0][1] > second[1][1] or first[0][1] < second[1][1]):
#           print("no collision")
#       elif (first[1][0] > second[0][0] or first[1][0] < second[0][0]) and (first[1][1] < second[0][1] or first[1][1] > second[0][1]):
#           print("no collision")
#       elif (first[0][0] > second[0][0] or first[0][0] < second[0][0]) and (first[0][1] > second[0][1] or first[0][1] < second[0][1]):
#           print("no collision")
#       elif first[1][0] < second[1][0] and first[1][1] < second[1][1]:
#           print("no collision")
#       else:
#           print("collision")



# collison_detection(first, second)