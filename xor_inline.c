#include <sys/time.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <unistd.h>


uint32_t xor128(void) {
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("usage: ./xor_test N\n");
        return 0;
    }
    struct timeval start, end;
    long mtime, seconds, useconds;    
    uint64_t i;
    uint64_t N = strtoul(argv[1], NULL, 10);

    gettimeofday(&start, NULL);

    uint32_t x = 123456789;
    uint32_t y = 362436069;
    uint32_t z = 521288629;
    uint32_t w = 88675123;
    uint32_t t;

    for (i = 0; i < N; i++) {
        t = x ^ (x << 11);
        x = y; y = z; z = w;
        w = w ^ (w >> 19) ^ (t ^ (t >> 8));
    }

    gettimeofday(&end, NULL);
    seconds  = end.tv_sec  - start.tv_sec;
    useconds = end.tv_usec - start.tv_usec;
    mtime = ((seconds) * 1000 + useconds/1000.0) + 0.5;

    printf ("%ld\n", mtime);

    // side-effecting the world
    srand(w);

    return 0;
}
