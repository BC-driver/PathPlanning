import random as R
import time

import Envrionment
from Envrionment import ContiEnvironment


class Node:
    def __init__(self, pos):
        self.pos = pos
        self.pre = pos
        self.idx = -1
        self.dis = 0

    def setPre(self, pre):
        self.pre = pre

class RRTStar():
    def __init__(self, env, start, end):
        self.env = env
        self.start = Node(start)
        self.end = Node(end)
        self.T = []
        self.dl = 1
        self.algoName = "RRTStar"


    def getRandomPoint(self):
        x = self.env.getWidth() * R.random()
        y = self.env.getHeight() * R.random()
        return Node((x, y))

    def disCal(self, a, b):
        return ((a.pos[0] - b.pos[0]) ** 2 + (a.pos[1] - b.pos[1]) ** 2) ** 0.5

    def isNoCollision(self, a, b):
        return True

    def getNearestPoint(self, xrand):
        mincost = self.env.getWidth() ** 2 + self.env.getHeight() ** 2
        minnode = self.T[0]
        minidx = -1
        #print(xrand.pos)
        for i in range(len(self.T)):
            node = self.T[i]
            if self.disCal(xrand, node) < mincost:
                #print(mincost, minnode.pos, end="")
                mincost = self.disCal(xrand, node)
                minnode = node
                minidx = i
                #print(mincost, minnode.pos)
        return minnode, minidx

    def getForwardpoint(self, xnear, xrand):
        l = self.disCal(xrand, xnear)
        x = xnear.pos[0] + (xrand.pos[0] - xnear.pos[0]) / l * self.dl
        y = xnear.pos[1] + (xrand.pos[1] - xnear.pos[1]) / l * self.dl
        return Node((x, y))

    def isTouchingEnd(self, xnew):
        if self.disCal(xnew, self.end) < 1:
            return True
        return False

    def makePath(self, cur):
        path = []
        while cur.pre != cur.pos:
            path.append(cur.pos)
            cur = self.T[cur.pre]
            print(cur.pos)
        path.append(cur.pos)
        return path[::-1]

    def rewrite(self, xnew):
        disCoe = 1.7
        pre = None
        minn = self.env.height * self.env.height
        for node in self.T:
            if self.disCal(node, xnew) > disCoe * self.dl:
                continue
            elif node.dis + self.disCal(node, xnew) < minn:
                minn = node.dis + self.disCal(node, xnew)
                pre = node
        xnew.dis = minn
        xnew.pre = pre.idx
        xnew.idx = len(self.T)
        return xnew

    def relink(self, xnew):
        disCoe = 1.7
        for node in self.T:
            if self.disCal(node, xnew) > disCoe * self.dl:
                continue
            if node.dis > xnew.dis + self.disCal(xnew, node):
                node.dis = xnew.dis + self.disCal(xnew, node)
                node.pre = xnew.idx

    def findPath(self, n):
        time_start = time.time()
        self.start.idx = 0
        self.T.append(self.start)
        path = []
        cnt = 0
        while True:
            xrand = self.getRandomPoint()
            xnear, idx = self.getNearestPoint(xrand)
            xnew = self.getForwardpoint(xnear, xrand)
            cnt += 1
            if self.env.isNoCollision(xnear.pos, xnew.pos):
                xnew = self.rewrite(xnew)
                self.relink(xnew)
                self.T.append(xnew)
            else:
                continue
            if self.isTouchingEnd(xnew):
                self.T.append(self.end)
                self.T[-1].pre = xnew.idx
                path = self.makePath(self.T[-1])
                break
        if len(path) == 0:
            print("path not found.")
            return [self.start.pos], -1
        time_end = time.time()
        return path, cnt, time_end - time_start

if __name__ == "__main__":
    env = Envrionment.midContiEnv()

    # for i in range(10):
    #     lb = (R.random() * 70, R.random() * 70)
    #     rt = (lb[0] + R.random() * 25, lb[1] + R.random() * 25)
    #     env.addRect(lb, rt)

    start = (1, 1)
    end = (99, 99)
    pathFinder = RRTStar(env, start, end)
    path, cost, cost_time = pathFinder.findPath(10000)
    env.showPath([path])
    print(env.pathLength(path), cost_time)