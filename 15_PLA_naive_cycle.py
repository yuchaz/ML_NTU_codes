import numpy as np

f = open('hw1_15_train.dat', 'r')
xVectorList = []
yList = []

for line in f:
    lineDataArray = map(float, line.split())
    x = np.array([1]+lineDataArray[:-1])
    y = lineDataArray[-1]
    xVectorList.append(x)
    yList.append(y)

wVector = np.array([0,0,0,0,0])

loopCyclyingThru = 0
lastMistakeIndex = 0
while True:
    ifInnerLoopContinues = False
    for idx in range(len(xVectorList)):
        if np.dot(wVector,xVectorList[idx])*yList[idx] <= 0:
            wVector = np.add(wVector, xVectorList[idx]*yList[idx])
            lastMistakeIndex = idx
            ifInnerLoopContinues = True

    loopCyclyingThru += 1
    if ifInnerLoopContinues == False:
        break

print ('It loop through {0} loops;\nLast mistake index is {1};\nThe final w is \n{2}'.format(loopCyclyingThru,lastMistakeIndex,wVector))
