import re
from functools import reduce


#okek bulmak lazım
#okek payda'yı bulmak için
#okek LCM ingilizcede
#bunu 2 taneli yapıp, reduce kullan bir de.
# Python Program to find the L.C.M. of two input number

# define a function
def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


def findLcm(listDenominator):
    x = reduce(lcm, listDenominator)
    return x

def stringSeperator(stringFraction):
    den = re.search(r"(\d+)(/)(\d+)", stringFraction)
    listFractionMember = [den.group(1), den.group(2), den.group(3)]
    return listFractionMember

def calculator(FractionMemberList, operator, lcm):
    #pay payda eşitleme işlemi yap.

    for x in FractionMemberList:
        a = lcm / eval(x.denumerator)
        newNom = a*eval(x.numerator)
        newDenom = lcm
        x.numerator = int(newNom)
        x.denumerator = int(newDenom)
        print(x.numerator)
        print(x.denumerator)

    def _sumf():
        total = 0
        totaldenum = 0
        for x in FractionMemberList:
            total = total + int(x.numerator)
            totaldenum = x.denumerator
        print("%d / %d" % (total, totaldenum))
        print("sadelesiyor")
        _sadelestir(total, totaldenum)


    def _subf():
        total = int(FractionMemberList[0].numerator) - int(FractionMemberList[1].numerator)
        totaldenum = FractionMemberList[0].denumerator
        print("%d / %d" % (total, totaldenum))

    def _mulf():
        L = []
        for x in FractionMemberList:
            L.append(x.numerator)
        total = reduce(lambda x,y : x*y, L)
        totaldenum = FractionMemberList[0].denumerator
        print("%d / %d" % (total, totaldenum))

    def _divf():
        L = []
        for x in FractionMemberList:
            L.append(x.numerator)
        total = reduce(lambda x,y : int(x/y), L)
        totaldenum = FractionMemberList[0].denumerator
        print("%d / %d" % (total, totaldenum))

    def _sadelestir(x,y):
        num = x
        denum = y
        x = simplify_fraction(num, denum)
        print(x)

    def mygcd(x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x

    def simplify_fraction(numer, denom):
        if denom == 0:
            return "Division by 0 - result undefined"

        common_divisor = mygcd(numer, denom)
        print("cmd is: %d" %(common_divisor))
        (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)

        if reduced_den == 1:
            return "%d/%d is simplified to %d" % (numer, denom, reduced_num)
        elif common_divisor == 1:
            return "%d/%d is already at its most simplified state" %(numer,denom)
        else:
            return "%d/%d is simplified to %d/%d" % (numer,denom,reduced_num,reduced_den)










    switcher = {
        "+" : _sumf,
        "-" : _subf,
        "*" : _mulf,
        "/" : _divf
        }
    print("operator is :" + operator)
    switcher.get(operator)()



