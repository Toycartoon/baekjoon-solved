R, C = map(int, input().split( ))
road = []

for i in range(R):
    road.append(list(input()))


# 상하좌우 오프셋 설정
offsets = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
]

# 유턴이 필요하다면 True 아니면 False
need_turn = False

# 모든 길을 탐색
for i in range(R):
    for j in range(C):
        # 현재 위치가 x인 경우 지나친다.
        if road[i][j] == 'X':
            continue

        # 현 위치에서 갈 수 있는 길의 개수
        path = 0

        # 상하좌우의 길을 확인
        for off in offsets:
            y = i + off[0]
            x = j + off[1]

            if 0 <= y < R and 0 <= x < C:
                # x, y 좌표가 리스트 인덱스 안에 있고
                # 해당 좌표가 길인 결우 path 증가
                if road[y][x] == '.':
                    path += 1

        # 상하좌우 탐색이 끝난 후
        if path <= 1:
            # 이동 가능한 길이 하나 이하면 유턴이 필요함
            need_turn = True
            break

print(1 if need_turn else 0)