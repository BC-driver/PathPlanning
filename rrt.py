from Envrionment import ContiEnvironment
import random as R

class Node():
    def __init__(self, pos):
        self.pos = pos
        self.pre = pos

    def setPre(self, pre):
        self.pre = pre
class RRT():
    def __init__(self, env, start, end):
        self.env = env
        self.start = Node(start)
        self.end = Node(end)
        self.T = []


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
        x = xnear.pos[0] + (xrand.pos[0] - xnear.pos[0]) / l
        y = xnear.pos[1] + (xrand.pos[1] - xnear.pos[1]) / l
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
        path.append(cur.pos)
        return path[::-1]

    def findPath(self, n):
        self.T.append(self.start)
        path = []
        cnt = 0
        while True:
            xrand = self.getRandomPoint()
            xnear, idx = self.getNearestPoint(xrand)
            xnew = self.getForwardpoint(xnear, xrand)
            xnewidx = -1
            cnt += 1
            if self.env.isNoCollision(xnear.pos, xnew.pos):
                self.T.append(xnew)
                xnewidx = len(self.T) - 1
                xnew.setPre(idx)
            else:
                continue
            if self.isTouchingEnd(xnew):
                self.T.append(self.end)
                self.T[-1].setPre(xnewidx)
                path = self.makePath(self.T[-1])
                break
        if len(path) == 0:
            print("path not found.")
            return [self.start.pos], -1
        return path, cnt

class RRTStar():
    def __init__(self, env, start, end, p):
        self.env = env
        self.start = Node(start)
        self.end = Node(end)
        self.p = p
        self.T = []


    def getRandomPoint(self):
        if R.random() > self.p:
            x = self.env.getWidth() * R.random()
            y = self.env.getHeight() * R.random()
        else:
            x, y = self.end.pos
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
        x = xnear.pos[0] + (xrand.pos[0] - xnear.pos[0]) / l
        y = xnear.pos[1] + (xrand.pos[1] - xnear.pos[1]) / l
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
        path.append(cur.pos)
        return path[::-1]

    def findPath(self, n):
        self.T.append(self.start)
        path = []
        cnt = 0
        while True:
            xrand = self.getRandomPoint()
            xnear, idx = self.getNearestPoint(xrand)
            xnew = self.getForwardpoint(xnear, xrand)
            xnewidx = -1
            cnt += 1
            if self.env.isNoCollision(xnear.pos, xnew.pos):
                self.T.append(xnew)
                xnewidx = len(self.T) - 1
                xnew.setPre(idx)
            else:
                continue
            if self.isTouchingEnd(xnew):
                self.T.append(self.end)
                self.T[-1].setPre(xnewidx)
                path = self.makePath(self.T[-1])
                break
        if len(path) == 0:
            print("path not found.")
            return [self.start.pos], -1
        return path, cnt

class RRTStar():
    def __init__(self, env, start, end, p):
        self.env = env
        self.start = Node(start)
        self.end = Node(end)
        self.p = p
        self.T = []


    def getRandomPoint(self):
        if R.random() > self.p:
            x = self.env.getWidth() * R.random()
            y = self.env.getHeight() * R.random()
        else:
            x, y = self.end.pos
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
        x = xnear.pos[0] + (xrand.pos[0] - xnear.pos[0]) / l
        y = xnear.pos[1] + (xrand.pos[1] - xnear.pos[1]) / l
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
        path.append(cur.pos)
        return path[::-1]

    def findPath(self, n):
        self.T.append(self.start)
        path = []
        cnt = 0
        while True:
            xrand = self.getRandomPoint()
            xnear, idx = self.getNearestPoint(xrand)
            xnew = self.getForwardpoint(xnear, xrand)
            xnewidx = -1
            cnt += 1
            if self.env.isNoCollision(xnear.pos, xnew.pos):
                self.T.append(xnew)
                xnewidx = len(self.T) - 1
                xnew.setPre(idx)
            else:
                continue
            if self.isTouchingEnd(xnew):
                self.T.append(self.end)
                self.T[-1].setPre(xnewidx)
                path = self.makePath(self.T[-1])
                break
        if len(path) == 0:
            print("path not found.")
            return [self.start.pos], -1
        return path, cnt

if __name__ == "__main__":
    width = 100
    height = 100
    start = (1, 1)
    end = (69, 76)
    env = ContiEnvironment(width, height)
    env.addRect((30, 30), (60, 70))
    env.addRect((10, 10), (20, 30))
    rrtCost = []
    rrtStartCost = []
    for i in range(20):
        pathFinder = RRT(env, start, end)
        pathFinder2 = RRTStar(env, start, end, 0.3)
        path, cost = pathFinder.findPath(10000)
        if cost != -1:
            rrtCost.append(cost)
        path2, cost = pathFinder2.findPath(10000)
        if cost != -1:
            rrtStartCost.append(cost)
    print(rrtCost, sum(rrtCost) / len(rrtCost))
    print(rrtStartCost, sum(rrtStartCost) / len(rrtStartCost))
    #env.showPath(path)
    #env.showPath(path2)