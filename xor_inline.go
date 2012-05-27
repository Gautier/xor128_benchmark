package main

import "flag"
import "fmt"
import "strconv"
import "time"

func main() {
    flag.Parse()
    var arg_n, err = strconv.ParseInt(flag.Arg(0), 10, 0)
    if err != nil {
        fmt.Printf("error %s", err.Error())
    }

    var n = int(arg_n)

    var t0 = time.Now()

    var x uint32 = 123456789
    var y uint32 = 362436069
    var z uint32 = 521288629
    var w uint32 = 88675123

    var t uint32 = 0

    for i := 0; i < n; i++ {
        t = x ^ (x << 11)
        x = y
        y = z
        z = w
        w = w ^ (w >> 19) ^ (t ^ (t >> 8))
    }

    fmt.Printf("%d\n", int(time.Now().Sub(t0).Seconds() * 1000))
}
