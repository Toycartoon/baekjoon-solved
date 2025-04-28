n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(reversed(a))
d = list(reversed(b))

x = a.index(1) + 1
y = b.index(1) + 1
z = c.index(1) + 1
_ = d.index(1) + 1

for i in [a, c, a[:x]+a[x:], a[x:]+a[:x], list(reversed(a[:x]+a[x:])), list(reversed(a[x:]+a[:x])),
          c[:z]+c[z:], c[z:]+c[:z], list(reversed(c[:z]+c[z:])), list(reversed(c[z:]+c[:z]))]:
    for j in [b, d, b[:y]+b[y:], b[y:]+b[:y], list(reversed(b[:y]+b[y:])), list(reversed(b[y:]+b[:y])),
              d[:_]+d[_:], d[_:]+d[:_], list(reversed(d[:_]+d[_:])), list(reversed(d[_:]+d[:_]))]:
        if i == j:
            print("good puzzle")
            exit()

print("bad puzzle")
