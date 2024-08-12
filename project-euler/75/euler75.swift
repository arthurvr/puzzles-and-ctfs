
import Foundation

let N = 1500000
let s = Int(round(sqrt(Double(N)/2)))

var count = Array(repeating: 0, count: N)

func gcd(_ a: Int, _ b: Int) -> Int {
    let remainder = abs(a) % abs(b)
    if remainder != 0 {
        return gcd(abs(b), remainder)
    } else {
        return abs(b)
    }
}

for m in 2...s {
    for n in stride(from: (m % 2) + 1, to: m, by: 2) {
        if gcd(m, n) > 1 {
            continue
        }

        let L = 2 * m * (m + n)

        if L > N {
            break;
        }

        for k in stride(from: L, to: N, by: L) {
            count[k] += 1
        }
    }
}

var frequency = 0;
for i in count {
    if i == 1 {
        frequency += 1
    }
}

print(frequency)

