import matplotlib.pyplot as plt

class Envrionment:
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

def emptyEnv(width, height):
    env = Envrionment(width, height)
    return env

def envOne():
    env = Envrionment(10, 10)
    env.setObs(0, 4, 1, 4)
    env.setObs(3, 0, 4, 4)
    env.setObs(2, 6, 5, 7)
    env.setObs(7, 2, 7, 3)
    env.setObs(6, 4, 7, 5)
    env.setObs(7, 7, 8, 8)
    env.setObs(6, 6, 6, 6)
    return env

class ContiEnvironment():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacleRect = []

    def showPath(self, path):
        cur = path[0]
        for point in path[1:]:
            plt.plot([cur[0], point[0]], [cur[1], point[1]], color="green")
            cur = point
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
        m = self.outProduct(a, c)
        n = self.outProduct(a, d)
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


if __name__ == "__main__":
    env = ContiEnvironment(100, 100)
    env.addRect((1, 1), (5, 5))
    print(env.isNoCollision((0, 1), (6, 1)))
