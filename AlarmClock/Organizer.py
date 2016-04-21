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

    def returnMemoryHolder(self):
        return self.memoryHolder


class AlarmClock:
    def __init__(self, memoryHolder):
        self.myHolder = memoryHolder

    def printNearestMemo(self):
        self.nowTime = time.localtime()
        for index in range(len(self.myHolder)):
            if self.nowTime <= self.myHolder[index].time:
                print(self.myHolder[index].time)
                print(self.myHolder[index].memo)

    def printOldMemos(self):
        self.nowTime = time.localtime()
        for index in range(len(self.myHolder)):
            if self.nowTime > self.myHolder[index].time:
                print(self.myHolder[index].time)
                print(self.myHolder[index].memo)
            else:
                print("bozuklukvar")

    def startAlarm(self):
        self.ttime = self.giveNext()
        alarm1 = AlarmAlerter(self.ttime)
        alarm1.start()

        try:
            while True:
                text = str(input())
                if text == "stop":
                    alarm1.just_die()
                    break
        except:
            print("Yikes lets get out of here")
            alarm1.just_die()

    def giveNext(self):
        self.nowTime = time.localtime()
        for index in range(len(self.myHolder)):
            if self.nowTime <= self.myHolder[index].time:
                return self.myHolder[index]
                break



class AlarmAlerter(threading.Thread):
    def __init__(self, atime):
        super(AlarmAlerter, self).__init__()
        self.atime = atime
        self.keep_running = True

    def run(self):
        print("thread basliyor")
        try:
            while self.keep_running:

                now = time.localtime()
                if(now.tm_hour == self.atime.time.tm_hour and now.tm_min == self.atime.time.tm_min):
                    print("ALARM ALARM")
                    return
                else:
                    print("olmadi")
                    time.sleep(5)

        except:
            return

    def just_die(self):
        self.keep_running = False





myHolder = MemoryHolder()
time1 = (2016, 4, 20, 18, 15, 39, 2, 111, 1)
mem1 = Memory("abc1", time.struct_time(time1))
myHolder.addToList(mem1)
#time.sleep(10)

time2 = time1 = (2016, 4, 20, 18, 15, 39, 2, 111, 1)
mem2 = Memory("qyz2", time.struct_time(time2))
myHolder.addToList(mem2)
#time.sleep(10)

time3 = time1 = (2016, 4, 20, 20, 27, 39, 2, 111, 1)
mem3 = Memory("uyt3", time.struct_time(time3))
myHolder.addToList(mem3)

myHolder.printAll()


alarmClock = AlarmClock(myHolder.returnMemoryHolder())
alarmClock.startAlarm()





