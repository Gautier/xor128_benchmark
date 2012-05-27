import sys
import time

if __name__ == "__main__":
    n = int(sys.argv[1])

    x = 123456789
    y = 362436069
    z = 521288629
    w = 88675123

    t = int(0)
    t0 = time.time()
    i = 0
    while i < n:
        t = x ^ (x << 11 & 0xFFFFFFFF)
        x = y
        y = z
        z = w
        w = w ^ (w >> 19) ^ (t ^ (t >> 8))
        i += 1
    t1 = time.time()
    print "%d" % ((t1 - t0) * 1000)
