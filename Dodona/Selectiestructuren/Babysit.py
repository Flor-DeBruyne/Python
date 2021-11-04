x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

x1 += y1 / 60.0
x2 += y2 / 60.0

u1800 = 18.0
u2130 = 21.5

if x1 < u1800 or x2 < x1:
    print("ongeldige invoer")
else:
    if x2 < u2130:
        t1 = x2 - x1
        t2 = 0.0
        
    elif x1 < u2130:
        t1 = u2130 - x1
        t2 = x2 - u2130

    else:
        t2 = x2 - x1
        t1 = 0

    result = 2 * t1 + 4 * t2
    print(result)









# begin = [int(input()),int(input())]
# eind = [int(input()),int(input())]

# def Babysit(begin,eind):
#     """Calculating how much the babysit has earned"""
#     loon = float(0)
#     if begin[0] < 18 or (eind[0] == 0 and eind[1] > 0):
#         #checking if the input is valid
#         #doesn't start working before 18.00 and not later than 00.00
#         print("invalid input")
#     elif eind[0]<= 21 and eind[1] <= 30:
#         uren = (eind[0]-begin[0]) * 60
#         min = (eind[1]-begin[1])
#         tijd = (uren - min) / 60
#         loon += 2*tijd
#         print(loon)
#     else:    
#         uren  = (eind[0]-21) * 60
#         min = (eind[1]-begin[1])
#         tijd = (uren- min) / 60
#         loon += 4*tijd
#         print(loon)


# Babysit(begin,eind)
