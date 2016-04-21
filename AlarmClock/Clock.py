import time

nowTime = time.localtime()
tupleS = (2017, 4, 12, 21, 9, 22, 1, 103, 1)
soTime = time.struct_time(tupleS)
print(soTime)
print(nowTime)

print(soTime < nowTime)