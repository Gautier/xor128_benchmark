function unsign(x) {
  return (((x|1) >>> 1) * 2)
}

var x = 123456789
var y = 362436069
var z = 521288629
var w = 88675123

var t = 0

var n = process.argv[2]
var t0 = new Date().getTime()

for (i = 0; i < n; i++) { 
    t = unsign(x ^ (x << 11))
    x = y
    y = z
    z = w
    w = unsign(w ^ (w >>> 19) ^ t ^ (t >>> 8))
}

console.log(new Date().getTime() - t0)
