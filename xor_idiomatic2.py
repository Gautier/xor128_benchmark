import sys
import time

class Xor128():
    def __init__(self):
        self.x = 123456789
        self.y = 362436069
        self.z = 521288629
        self.w = 88675123
        self.t = int(0)

    def next_number(self):
        self.t = self.x ^ (self.x << 11 & 0xFFFFFFFF)
        self.x = self.y
        self.y = self.z
        self.z = self.w
        self.w = self.w ^ (self.w >> 19) ^ (self.t ^ (self.t >> 8))
        return self.w

if __name__ == "__main__":
    n = int(sys.argv[1])

    t0 = time.time()

    x = Xor128()
    for i in range(n): x.next_number()

    t1 = time.time()
    print "%d" % ((t1 - t0) * 1000)
