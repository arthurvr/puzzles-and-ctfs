var n: Int = 0
var d: Int = 1

let limit: Int = 1000000

for q in stride(from: limit, to: 3, by: -1) {
    let p = (3 * q - 1) / 7

    if (p * d > n * q) {
        d = q
        n = p
    }
}

print("\(n)")
