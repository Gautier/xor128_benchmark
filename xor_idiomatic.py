import sys
import time

def xor128():
    x = 123456789
    y = 362436069
    z = 521288629
    w = 88675123

    t = int(0)
    while True:
        t = x ^ (x << 11 & 0xFFFFFFFF)
        x = y
        y = z
        z = w
        w = w ^ (w >> 19) ^ (t ^ (t >> 8))
        yield w

if __name__ == "__main__":
    n = int(sys.argv[1])

    t0 = time.time()

    x = xor128()
    for i in range(n): next(x)

    t1 = time.time()
    print "%d" % ((t1 - t0) * 1000)
