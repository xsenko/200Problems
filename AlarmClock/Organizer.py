import time
import threading
import sys

class Memory:
    def __init__(self, memo, time):
        self.memo = memo
        self.time = time

    def showMemo(self):
        print(self.memo)


class MemoryHolder:
    def __init__(self):
        self.memoryHolder = []

    def addToList(self, memory):
        if len(self.memoryHolder) == 0:
            self.memoryHolder.append(memory)
        else:
            self.sortAndAdd(self.memoryHolder, memory)

    def sortAndAdd(self, memoryHolder, memory):
        for index in range(len(memoryHolder)):
            if(memory.time < memoryHolder[index].time):
                memoryHolder.insert(index, memory)
            else:
                memoryHolder.append(memory)
                break

    def printAll(self):
        for item in self.memoryHolder:
            print(item.memo, item.time)


myHolder = MemoryHolder()
mem1 = Memory("abc1", time.localtime())
myHolder.addToList(mem1)
#time.sleep(10)

mem2 = Memory("qyz2", time.localtime())
myHolder.addToList(mem2)
#time.sleep(10)

mem3 = Memory("uyt3", time.localtime())
myHolder.addToList(mem3)

myHolder.printAll()




