#include <sys/time.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <unistd.h>

uint32_t xor128(void) {
  static uint32_t x = 123456789;
  static uint32_t y = 362436069;
  static uint32_t z = 521288629;
  static uint32_t w = 88675123;
  uint32_t t;

  t = x ^ (x << 11);
  x = y; y = z; z = w;
  return w = w ^ (w >> 19) ^ (t ^ (t >> 8));
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("usage: ./xor_test N\n");
        return 0;
    }
    struct timeval start, end;
    long mtime, seconds, useconds;    
    gettimeofday(&start, NULL);

    int N = atoi(argv[1]);;
    int i;
    for (i = 0; i < N; i++) {
        xor128();
    }

    gettimeofday(&end, NULL);
    seconds  = end.tv_sec  - start.tv_sec;
    useconds = end.tv_usec - start.tv_usec;
    mtime = ((seconds) * 1000 + useconds/1000.0) + 0.5;

    printf ("%ld\n", mtime);

    return 0;
}
