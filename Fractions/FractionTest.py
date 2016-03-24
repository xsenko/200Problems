import FractionCalculator
from FractionMember import FractionMember

inputRaw = input("enter your fraction: ")
inputRaw2 = input("enter second fraction: ")
operation = input("enter your operation: ")



mylist = FractionCalculator.stringSeperator(inputRaw)
mylist2 = FractionCalculator.stringSeperator(inputRaw2)

member1 = FractionMember(mylist[0], mylist[2])
member1.showAsFraction()

member2 = FractionMember(mylist2[0], mylist2[2])
member2.showAsFraction()

fractionMemberList = []
fractionMemberList.append(member1)
fractionMemberList.append(member2)

#find the LCM
listOfDem = []
listOfDem.append(eval(member1.denumerator))
listOfDem.append(eval(member2.denumerator))
lcm = FractionCalculator.findLcm(listOfDem)
print(lcm)

FractionCalculator.calculator(fractionMemberList, operation, lcm)








