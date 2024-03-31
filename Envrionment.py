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
