package main

import "flag"
import "fmt"
import "strconv"
import "time"

func xor128 () func() uint32 {
    var x uint32 = 123456789
    var y uint32 = 362436069
    var z uint32 = 521288629
    var w uint32 = 88675123

    var t uint32 = 0

    return func () uint32 {
        t = x ^ (x << 11)
        x = y
        y = z
        z = w
        w = w ^ (w >> 19) ^ (t ^ (t >> 8))
        return w
    }
}

func main() {
    flag.Parse()
    var n, err = strconv.ParseUint(flag.Arg(0), 10, 64)
    if err != nil {
        fmt.Printf("error %s", err.Error())
    }

    var t0 = time.Now()

    rng := xor128()
    var i uint64 = 0
    for ; i < n; i++ {
        rng()
    }

    fmt.Printf("%d\n", int(time.Now().Sub(t0).Seconds() * 1000))
}
