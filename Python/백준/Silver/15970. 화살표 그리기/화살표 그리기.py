# 점의 개수 입력
n = int(input())

# 각 점의 정보를 저장하는 리스트
all_points = []

# 각 점의 정보들을 입력
for i in range(n):
    all_points.append(list(map(int, input().split())))

# 모든 거리의 합
total = 0

# 현재 점 nowP에서 다음 점 nextP를 비교하며
# 색이 같고 거리가 가장 가까운 점을 구한 후
# 최소 거리를 total 에 합산 해줌
for nowP in all_points:
    # 최소 거리의 초기값은 최대 거리로 설정
    min_distance = 100000
    # nowP를 제외한 모든 점들을 검사
    for nextP in all_points:
        if nowP == nextP:
            continue
        if nowP[1] == nextP[1]:
            distance = abs(nowP[0] - nextP[0])
            if distance < min_distance:
                min_distance = distance
    total += min_distance

print(total)