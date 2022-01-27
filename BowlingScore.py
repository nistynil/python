frame = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 10, 10]
bonus = 0
scoresum = sum(frame)
a = 0
def Say():
    print("Function not easy")
while a < 18:
    if frame[a] == 10:
        if frame[a+2] == 10:
            bonus = bonus + frame[a+2] + frame[a+4]
        else:
            bonus = bonus + frame[a+2] + frame[a+3]
    elif frame[a]+frame[a+1] == 10:
        bonus = bonus + frame[a+2]
    a = a + 2
print (bonus+scoresum)
Say()
#print (bonus)
