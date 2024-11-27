import matplotlib.pyplot as plt
from math import sqrt

class Environment:
    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.env = [[0 for i in range(width)] for i in range(height)]

    def getEnv(self, x, y):
        return self.env[x][y]

    def getSize(self):
        return (self.height, self.height)

    def showenv(self):
        for i in range(self.height):
            for j in range(self.width):
                print(".#PBSE"[self.env[i][j]], end='')
            print()

    def setObs(self, ltx, lty, rbx, rby):
        for i in range(ltx, rbx + 1):
            for j in range(lty, rby + 1):
                self.env[i][j] = 1;

    def setPath(self, pos):
        self.env[pos[0]][pos[1]] = 2

    def setStart(self, pos):
        self.env[pos[0]][pos[1]] = 4

    def setEnd(self, pos):
        self.env[pos[0]][pos[1]] = 5

    def showPath(self, paths):
        fig = plt.figure(figsize=(self.width, self.height))
        axes = fig.add_subplot(1, 1, 1)
        plt.axis('scaled')
        axes.set_xlim(0, self.width)
        axes.set_ylim(0, self.height)

        for path in paths:
            axes.add_patch(plt.Rectangle(xy=path[0], width=1, height=1, color="black"))
            axes.add_patch(plt.Rectangle(xy=path[-1], width=1, height=1, color="red"))

            cur = path[0]
            for point in path[1:]:
                axes.plot([cur[0], point[0]], [cur[1], point[1]], color="green")
                cur = point

        for i in range(self.height):
            for j in range(self.width):
                if self.env[i][j] != 0:
                    axes.add_patch(
                        plt.Rectangle(xy=(j, i), width=1, height=1))
        plt.show()

def smallDiscreateEnv():
    res = Environment(width=100, height=100)
    lilLBPt = [(48, 45), (46, 3), (14, 47), (20, 4)]
    lilRTPt = [(72, 73), (61, 31), (44, 78), (45, 19)]
    for i in range(len(lilRTPt)):
        res.setObs(lilLBPt[i][1], lilLBPt[i][0], lilRTPt[i][1] - 1, lilRTPt[i][0] - 1)
    return res

def midDiscreateEnv():
    res = Environment(width=100, height=100)
    midLBPt = [(59, 44), (1, 62), (32, 65), (25, 33), (10, 22), (68, 4), (12, 60), (27, 44), (38, 69), (30, 10)]
    midRTPt = [(79, 68), (13, 84), (45, 89), (40, 58), (27, 44), (83, 19), (22, 84), (41, 65), (57, 80), (55, 27)]
    for i in range(len(midLBPt)):
        res.setObs(midLBPt[i][1], midLBPt[i][0], midRTPt[i][1] - 1, midRTPt[i][0] - 1)
    return res

def bigDiscreateEnv():
    res = Environment(width=100, height=100)
    bigLBPt = [(48, 23), (28, 35), (47, 73), (31, 22), (13, 59), (59, 47), (4, 71), (49, 64), (69, 17), (6, 13),
               (51, 32), (74, 61), (49, 63), (54, 38), (84, 10), (44, 57), (75, 50), (1, 53), (19, 28), (23, 7),
               (50, 32), (61, 38), (23, 65), (63, 1), (33, 51), (26, 9), (79, 6), (84, 64), (31, 2), (46, 18), (3, 43),
               (45, 80), (14, 24), (1, 83), (54, 0), (13, 30), (75, 43), (5, 52), (4, 57), (18, 5), (56, 60), (10, 22),
               (6, 13), (45, 69), (41, 22), (59, 20), (81, 2), (13, 6), (73, 20), (63, 40), (24, 16), (30, 65),
               (14, 27), (79, 61), (65, 29)]
    bigRTPt = [(56, 37), (42, 47), (58, 85), (38, 28), (21, 69), (71, 54), (18, 80), (62, 79), (74, 26), (15, 21),
               (57, 44), (81, 70), (55, 73), (65, 49), (96, 21), (51, 64), (89, 56), (9, 64), (27, 36), (34, 21),
               (63, 40), (66, 47), (33, 72), (72, 11), (40, 62), (38, 20), (92, 20), (92, 71), (42, 13), (60, 30),
               (16, 52), (50, 92), (27, 29), (9, 95), (61, 8), (25, 37), (81, 54), (11, 61), (9, 68), (24, 14),
               (68, 68), (24, 36), (21, 22), (58, 82), (50, 34), (68, 34), (91, 15), (24, 14), (85, 29), (74, 49),
               (38, 24), (35, 72), (22, 41), (92, 72), (71, 35)]
    for i in range(len(bigLBPt)):
        res.setObs(bigLBPt[i][1], bigLBPt[i][0], bigRTPt[i][1] - 1, bigRTPt[i][0] - 1)
    return res

def emptyEnv(width, height):
    env = Environment(width, height)
    return env

class ContiEnvironment():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacleRect = []

    def showPath(self, paths):
        fig = plt.figure(figsize=(self.width, self.height))
        axes = fig.add_subplot(1, 1, 1)
        plt.axis('scaled')
        axes.set_xlim(0, self.width)
        axes.set_ylim(0, self.height)

        for path in paths:
            axes.add_patch(plt.Rectangle(xy=path[0], width=1, height=1, color="black"))
            axes.add_patch(plt.Rectangle(xy=path[-1], width=1, height=1, color="red"))

            cur = path[0]
            for point in path[1:]:
                axes.plot([cur[0], point[0]], [cur[1], point[1]], color="green")
                cur = point

        for rect in self.obstacleRect:
            axes.add_patch(plt.Rectangle(xy=rect[0], width=rect[1][0] - rect[0][0], height=rect[1][1] - rect[0][1]))
        plt.show()

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def addRect(self, left_bottom, right_top):
        self.obstacleRect.append((left_bottom, right_top))

    def outProduct(self, a, b):
        return a[0] * b[1] - a[1] * b[0]

    def isNoLineCollision(self, a, b, c, d):
        vecAB = (b[0] - a[0], b[1] - a[1])
        vecAC = (c[0] - a[0], c[1] - a[1])
        vecAD = (d[0] - a[0], d[1] - a[1])
        m = self.outProduct(vecAB, vecAC)
        n = self.outProduct(vecAB, vecAD)
        #print(a, b, c, d, m, n)
        if m == 0 and n == 0:
            if max(a[0], b[0]) < min(c[0], d[0]) or \
                max(a[1], b[1]) < min(c[1], d[1]) or \
                min(a[0], b[0]) < max(c[0], d[0]) or \
                min(a[1], b[1]) < max(c[1], d[1]):
                return True
            return False
        return m * n > 0

    def isNoCollision(self, u, v):
        flag = True
        for rect in self.obstacleRect:
            flag &= self.isNoLineCollision(u, v, rect[0], (rect[0][0], rect[1][1]))
            flag &= self.isNoLineCollision(u, v, (rect[0][0], rect[1][1]), rect[1])
            flag &= self.isNoLineCollision(u, v, (rect[1][0], rect[0][1]), rect[1])
            flag &= self.isNoLineCollision(u, v, rect[0], (rect[1][0], rect[0][1]))
            if flag == False:
                break
        return flag

    def pathLength(self, path):
        res = 0
        for i in range(1, len(path)):
            x1, y1 = path[i - 1]
            x2, y2 = path[i]
            res += sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return res


def smallContiEnv():
    res = ContiEnvironment(width=100, height=100)
    lilLBPt = [(48, 45), (46, 3), (14, 47), (20, 4)]
    lilRTPt = [(72, 73), (61, 31), (44, 78), (45, 19)]
    for i in range(len(lilRTPt)):
        res.addRect(lilLBPt[i], lilRTPt[i])
    return res

def midContiEnv():
    res = ContiEnvironment(width=100, height=100)
    midLBPt = [(59, 44), (1, 62), (32, 65), (25, 33), (10, 22), (68, 4), (12, 60), (27, 44), (38, 69), (30, 10)]
    midRTPt = [(79, 68), (13, 84), (45, 89), (40, 58), (27, 44), (83, 19), (22, 84), (41, 65), (57, 80), (55, 27)]
    for i in range(len(midLBPt)):
        res.addRect(midLBPt[i], midRTPt[i])
    return res

def bigContiEnv():
    res = ContiEnvironment(width=100, height=100)
    bigLBPt = [(48, 23), (28, 35), (47, 73), (31, 22), (13, 59), (59, 47), (4, 71), (49, 64), (69, 17), (6, 13),
               (51, 32), (74, 61), (49, 63), (54, 38), (84, 10), (44, 57), (75, 50), (1, 53), (19, 28), (23, 7),
               (50, 32), (61, 38), (23, 65), (63, 1), (33, 51), (26, 9), (79, 6), (84, 64), (31, 2), (46, 18), (3, 43),
               (45, 80), (14, 24), (1, 83), (54, 0), (13, 30), (75, 43), (5, 52), (4, 57), (18, 5), (56, 60), (10, 22),
               (6, 13), (45, 69), (41, 22), (59, 20), (81, 2), (13, 6), (73, 20), (63, 40), (24, 16), (30, 65),
               (14, 27), (79, 61), (65, 29)]
    bigRTPt = [(56, 37), (42, 47), (58, 85), (38, 28), (21, 69), (71, 54), (18, 80), (62, 79), (74, 26), (15, 21),
               (57, 44), (81, 70), (55, 73), (65, 49), (96, 21), (51, 64), (89, 56), (9, 64), (27, 36), (34, 21),
               (63, 40), (66, 47), (33, 72), (72, 11), (40, 62), (38, 20), (92, 20), (92, 71), (42, 13), (60, 30),
               (16, 52), (50, 92), (27, 29), (9, 95), (61, 8), (25, 37), (81, 54), (11, 61), (9, 68), (24, 14),
               (68, 68), (24, 36), (21, 22), (58, 82), (50, 34), (68, 34), (91, 15), (24, 14), (85, 29), (74, 49),
               (38, 24), (35, 72), (22, 41), (92, 72), (71, 35)]
    for i in range(len(bigLBPt)):
        res.addRect(bigLBPt[i], bigRTPt[i])
    return res

if __name__ == "__main__":
    env = bigDiscreateEnv()
    env.showPath([])
