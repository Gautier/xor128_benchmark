function unsign(x) {
  return (((x|1) >>> 1) * 2)
}

function xor128 () {
  var x = 123456789
  var y = 362436069
  var z = 521288629
  var w = 88675123

  var t = 0

  return function () {
    t = unsign(x ^ (x << 11))
    x = y
    y = z
    z = w
    w = unsign(w ^ (w >>> 19) ^ t ^ (t >>> 8))
    return w
  }
}

var n = process.argv[2]
var t0 = new Date().getTime();

var rng = xor128()
for (i = 0; i < n; i++) rng()

console.log(new Date().getTime() - t0)
