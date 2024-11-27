import heapq
import Envrionment
import math

class node:
    def __init__(self, x, y):
        self.pre = 4
        self.inf = 1e10
        self.dis = self.inf
        self.pos = (x, y)
        self.vis = 0

    def __lt__(self, other):
        if self.dis < other.dis:
            return True
        else:
            return False

class Dijkstra:
    def __init__(self, start, end, env):
        self.env = env
        self.start = start
        self.end = end
        self.height = self.env.getSize()[0]
        self.width = self.env.getSize()[1]
        self.graph = [[node(i, j) for j in range(self.width)] for i in range(self.height)]
        self.q = []
        self.opcnt = 0

    def disCal(self, nodea, nodeb):
        if self.env.env[nodea.pos[0]][nodea.pos[1]] == 1 or self.env.env[nodeb.pos[0]][nodeb.pos[1]] == 1:
            return nodea.inf
        else:
            return math.sqrt((nodea.pos[0] - nodeb.pos[0])**2 + (nodea.pos[1] - nodeb.pos[1])**2)

    def preCal(self, nodea, nodeb):
        return 3 * (nodea.pos[0] - nodeb.pos[0] + 1) + (nodea.pos[1] - nodeb.pos[1] + 1)

    def run(self):
        heapq.heappush(self.q, self.graph[self.start[0]][self.start[1]])
        self.graph[self.start[0]][self.start[1]].dis = 0
        while len(self.q) != 0:
            curnode = heapq.heappop(self.q)
            curnode.vis = 1
            if self.end == curnode.pos:
                break
            for i in range(-1, 2):
                for j in range(-1, 2):
                    curx = curnode.pos[0]
                    cury = curnode.pos[1]
                    if curx + i < 0 or curx + i >= self.height \
                    or cury + j < 0 or cury + j >= self.width:
                        continue
                    nxtnode = self.graph[curx + i][cury + j]
                    if nxtnode.vis == 1:
                        continue
                    if nxtnode.dis > curnode.dis + self.disCal(curnode, nxtnode):
                        nxtnode.dis = curnode.dis + self.disCal(curnode, nxtnode)
                        nxtnode.pre = self.preCal(curnode, nxtnode)
                        self.opcnt += 1
                        heapq.heappush(self.q, nxtnode)

        curnode = self.graph[self.end[0]][self.end[1]]
        while curnode.pos != self.start:
            self.env.setPath(curnode.pos)
            curnode = self.graph[curnode.pos[0] + (curnode.pre // 3) - 1][curnode.pos[1] + (curnode.pre % 3) - 1]
        self.env.setStart(self.start)
        self.env.setEnd(self.end)
        print(f"Operation count:{self.opcnt}")




def main():
    mymap = Envrionment.smallDiscreateEnv()
    mymap.showenv()
    print()
    model = Dijkstra((0, 0), (99, 99), mymap)
    model.run()
    mymap.showenv()


if __name__ == "__main__":
    main()