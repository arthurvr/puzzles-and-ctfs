# I wrote and debugged this code with all the convoluted "EAT" variable names.
# Was it confusing? Yes. Was debugging hard? Yes.
# Did I spend more time than I should have on this problem? Yes

def Eating(eat):
    return str(int(eat)*EATEATEAT)

def EAt(eat, eats):
    eat1 = 0
    eat2 = 0
    eateat = 0
    eAt = ""
    while eat1 < len(eat) and eat2 < len(eats):
        if eateat%EATEATEAT == EATEATEATEATEAT//EATEATEATEAT:
            eAt += eats[eat2]
            eat2 += 1
        else:
            eAt += eat[eat1]
            eat1 += 1
        eateat += 1
    return eAt

def aten(eat):
    return eat[::EATEATEAT-EATEATEATEAT]

def eaT(eat):
    return Eating(eat[:EATEATEAT]) + aten(eat)

def aTE(eat):
    return eat#*len(eat)

def Ate(eat):
    return "Eat" + str(len(eat)) + eat[:EATEATEAT]

def Eat(eat):
    if len(eat) == 9:
        if str.isdigit(eat[:EATEATEAT]) and\
            str.isdigit(eat[len(eat)-EATEATEAT+1:]):
                eateat = EAt(eaT(eat), Ate(aTE(aten(eat))))
                if eateat == "E10a23t9090t9ae0140":
                    flag = "eaten_" + eat
                    print("absolutely EATEN!!! CTFlearn{",flag,"}")
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False

EATEATEAT = 9//3
EATEATEATEAT = EATEATEAT+1
EATEATEATEATEAT = EATEATEAT-1

# 'eat' as middle string was kindof a giveway... But brute forcing the 3 letter word wouldn't be a big effort either.
for i in range(1000):
    for j in range(1000):
        input_str = "{:03d}".format(i) + "eat" + "{:03d}".format(j)
        Eat(input_str)

