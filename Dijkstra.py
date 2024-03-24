import heapq
import Envrionment

class node:
    def __init__(self):
        self.next = 4
        self.inf = 1e10
        self.dis = self.inf

class Dijkstra:
    def __init__(self, start, end, env):
        self.env = env
        self.start = start
        self.end = end
        self.height = self.env.getSize()[0]
        self.width = self.env.getSize()[1]
        self.graph = [[node() for i in range(self.width)] for i in range(self.height)]


def main():
    mymap = Envrionment.Envrionment(10, 10)
    mymap.showenv()


if __name__ == "__main__":
    main()