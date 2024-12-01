import Envrionment
import AStar
import Dijkstra
import rrt
import rrtStar
import matplotlib.pyplot as plt
from copy import deepcopy

sde = Envrionment.smallDiscreateEnv()
mde = Envrionment.midDiscreateEnv()
bde = Envrionment.bigDiscreateEnv()
sce = Envrionment.smallContiEnv()
mce = Envrionment.midContiEnv()
bce = Envrionment.bigContiEnv()
discreateEnvs = [sde, mde]
contiEnvs = [sce, mce]

start = (0, 0)
end = (99, 99)
N = 10000
testTime = 100

pathFinderList = [rrt.RRT, rrt.RRTPSmart, rrt.RRTP, rrtStar.RRTStar]
timeList = []
pathLengthList = []

result = []

for algo in pathFinderList:
    envRes = []
    for env in contiEnvs:
        testRes = []
        for t in range(testTime):
            pathFinder = algo(env, start, end)
            path, cnt, timeCost = pathFinder.findPath(N)
            testRes.append([env.pathLength(path), timeCost])
            print([env.pathLength(path), timeCost])
        envRes.append(testRes)
    result.append(envRes)

def showTestResultSep(pathFinderList, result):
    fig, ax = plt.subplots(len(pathFinderList), len(result[0]))
    for algoidx in range(len(result)):
        for envidx in range(len(result[0])):
            data = result[algoidx][envidx]
            xlist = [i + 1 for i in range(len(data))]
            lenList = [row[0] for row in data]
            timeList = [row[1] for row in data]
            ax[algoidx][envidx].set_xlabel(
                "{}-{} Env".format(["RRT", "RRTPSmart", "RRTP"][algoidx], ["Small", "Middle", "Big"][envidx]))
            ax1 = ax[algoidx][envidx]
            ax2 = ax1.twinx()
            ax1.plot(xlist, lenList, color='blue')
            ax1.set_ylabel("pathLength", color='blue')
            ax2.plot(xlist, timeList, color='green')
            ax2.set_ylabel("time", color='green')
    plt.tight_layout()
    plt.show()

def showTestResult(pathFinderList, result):
    colors = ['lightsteelblue', 'peachpuff', 'mediumseagreen', 'lavender', 'lightpink',
              'lightgray', 'lightyellow', 'powderblue', 'olive', 'honeydew']
    fig, ax = plt.subplots(2, len(result[0]))
    for paraidx in range(2):
        paraName = ["pathLength", "time"][paraidx]
        for envidx in range(len(result[0])):
            ax[paraidx][envidx].set_label("pathLength")
            for algoidx in range(len(result)):
                algoName = ["RRT", "RRTPSmart", "RRTP", "RRTStar"][algoidx]
                data = result[algoidx][envidx]
                xlist = [i + 1 for i in range(len(data))]
                dataList = [row[paraidx] for row in data]
                ax[paraidx][envidx].plot(xlist, dataList, color=colors[algoidx], label=algoName)
                ax[paraidx][envidx].plot(xlist, [sum(dataList) / len(dataList) for i in range(len(xlist))],
                                         linestyle='--', color=colors[algoidx])
            ax[paraidx][envidx].legend()
            ax[paraidx][envidx].set_xlabel("{}-{} Env".format(paraName, ["Small", "Middle", "Big"][envidx]))
    plt.tight_layout()
    plt.show()

showTestResult(pathFinderList, result)