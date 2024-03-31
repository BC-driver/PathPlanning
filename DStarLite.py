import Envrionment
import heapq

class node:
    def __init__(self, i, j):
        self.inf = 1e10
        self.g = self.inf
        self.rhs = self.inf
        self.key = [0, 0]
        self.pos = [i, j]
        self.next = 4

    def __lt__(self, other):
        if self.key[0] == other.key[0]:
            return self.key[1] < other.key[1]
        else:
            return self.key[0] < self.key[0]

class DStarLite:
    def __init__(self, start, end, realenv, botenv):
        self.realenv = realenv
        self.botenv = botenv
        self.height = realenv.height
        self.width = realenv.width
        self.graph = [[node(i, j) for j in range(self.width)] for i in range(self.height)]
        self.start = start
        self.end = end
        self.botpos = start
        self.hOffset = 0
        self.q = []

    def herCal(self, nodea, nodeb):
        return abs(nodea.pos[0] - nodeb.pos[0]) + abs(nodea.pos[1] - nodeb.pos[1])

    def disCal(self, nodea, nodeb):
        if self.botenv.env[nodea.pos[0]][nodea.pos[1]] == 1 or self.botenv.env[nodeb.pos[0]][nodeb.pos[1]] == 1:
            return nodea.inf
        else:
            return ((nodea.pos[0] - nodeb.pos[0]) ** 2 + (nodea.pos[1] - nodeb.pos[1]) ** 2) ** 0.5

    def keyCal(self, curnode):
        botnode = self.graph[self.botpos[0]][self.botpos[1]]
        curnode.key[0] = min(curnode.rhs, curnode.g) + self.herCal(curnode, botnode) + self.hOffset
        curnode.key[1] = min(curnode.rhs, curnode.g)

    def processState(self, curnode):
        if node.rhs < node.g:
            node.g = node.rhs
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if node.pos[0] + i < 0 or node.pos[0] + i >= self.height \
                    or node.pos[1] + j < 0 or node.pos[1] + j >= self.width:
                        continue
                    desnode = self.graph[node.pos[0] + i][node.pos[1] + j]
                    if curnode.g + self.disCal(curnode, desnode) < desnode.rhs:
                        desnode.rhs = curnode.g + self.disCal(curnode, desnode)
                        self.keyCal(desnode)
                        heapq.heappush(self.q, desnode) #To be conti.



    def run(self):
        botnode = self.graph[self.botpos[0]][self.botpos[1]]
        curnode = self.graph[self.end[0]][self.end[1]]
        curnode.rhs = 0
        self.keyCal(curnode)
        heapq.heappush(self.q, self.self.graph[self.end.pos[0]][self.end.pos[1]])
        while len(self.q) != 0:
            curnode = heapq.heappop(self.q)
            self.processState(curnode)
            if curnode.pos == self.botpos:
                break


