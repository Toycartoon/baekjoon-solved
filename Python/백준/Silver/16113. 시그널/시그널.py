N = int(input())
signal = input()

width = int(N/5)

division_code = []
for i in range(5):
    division_code.append(signal[width*i:width*(i + 1)])

# N 행에서 '#'의 값을 정의
level = [1, 2, 3, 4, 5]

# 0부터 9까지의 숫자 패턴
pattern = [
    [15, 6, 15],       # 0
    [15],              # 1
    [13, 9, 11],       # 2
    [9, 9, 15],        # 3
    [6, 3, 15],        # 4
    [11, 9, 13],       # 5
    [15, 9, 13],       # 6
    [1, 1, 15],        # 7
    [15, 9, 15],       # 8
    [11, 9, 15]        # 9
]

# 문자열을 분석한 패턴값을 저장할 리스트
match = []

# 한 열의 패턴값
value = 0

for i in range(width):
    for j in range(5):
        value += level[j] if division_code[j][i] == '#' else 0

    if value != 0:
        # 열의 값이 0이 아닌 경우(즉, 0이 아님)
        # match 에 삽입
        match.append(value)
        value = 0
    else:
        # 열의 값이 0인 경우
        # 앞서 만든 pattern 리스트에서 match 를 찾음
        for k in range(10):
            if match == pattern[k]:
                # 찾았으면 해당하는 인덱스 번호를 출력
                print(k, end='')
                # match 리스트 초기화
                match.clear()

# 만약 match 리스트에 값이 남아있으면
# 마지막으로 pattern 리스트와 비교
for k in range(10):
    if match == pattern[k]:
        print(k, end='')

'''
###.#.###.###.#.#.###.###.###.###.###
#.#.#...#...#.#.#.#...#.....#.#.#.#.#
#.#.#.###.###.###.###.###...#.###.###
#.#.#.#.....#...#...#.#.#...#.#.#...#
###.#.###.###...#.###.###...#.###.###
'''