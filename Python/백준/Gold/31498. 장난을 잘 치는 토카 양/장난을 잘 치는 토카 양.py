a, b = map(int, input().split())
c, d = map(int, input().split())
k = int(input())

toycartoon = a
doldol = a + c

if k == 0:
    t_dist = (toycartoon + b - 1) // b      # 토카의 이동거리
    d_dist = (doldol + d - 1) // d          # 돌돌이의 이동거리

    print(t_dist if t_dist < d_dist else -1)    # 토카의 이동거리 < 돌돌이의 이동거리면 토카는 안전하게 집에 들어감
else:
    s = b
    ans = 0

    while 0 < toycartoon <= doldol and s > 0:   # 토카가 지치지 않고, 돌돌이를 앞서고 있을때까지 반복
        toycartoon -= s

        if toycartoon < 0:  # 0 밑으로 내려가는 경우는 없음, 보정
            toycartoon = 0

        s -= k  # 속도 감소

        if s < 0:
            s = 0   # 속도는 0 이하로 내려가지 않음

        doldol -= d
        ans += 1

    print(ans if toycartoon <= 0 < doldol else -1)  # 토카가 돌돌이에게 잡히지 않은 경우에 답을 출력
