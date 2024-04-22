# [Silver III] Yacht Dice - 27162 

[문제 링크](https://www.acmicpc.net/problem/27162) 

### 성능 요약

메모리: 30616 KB, 시간: 56 ms

### 분류

브루트포스 알고리즘, 많은 조건 분기, 구현

### 제출 일자

2023년 1월 18일 22:50:19

### 문제 설명

<p><strong>《Yacht Dice》</strong>는 여러 명이 플레이하는 주사위 게임입니다. 플레이어는 우선 주사위를 $5$개 굴립니다. 이후 원하는 주사위를 고정시킨 뒤, 남은 주사위를 다시 굴리는 일을 두 번 이하로 할 수 있습니다. 그렇게 주사위를 굴려 나온 값들의 조합으로 아래 족보에서 이전까지 선택하지 않은 하나를 선택해 점수를 기록합니다.</p>

<ul>
	<li><strong>Ones</strong>: $1$이 나온 주사위의 눈 수의 총합.</li>
	<li><strong>Twos</strong>: $2$가 나온 주사위의 눈 수의 총합.</li>
	<li><strong>Threes</strong>: $3$이 나온 주사위의 눈 수의 총합.</li>
	<li><strong>Fours</strong>: $4$가 나온 주사위의 눈 수의 총합.</li>
	<li><strong>Fives</strong>: $5$가 나온 주사위의 눈 수의 총합.</li>
	<li><strong>Sixes</strong>: $6$이 나온 주사위의 눈 수의 총합.</li>
	<li><strong>Four of a Kind</strong>: 동일한 주사위 눈이 $<strong>4</strong>$<strong>개 이상</strong>이라면, 동일한 주사위 눈 $<strong>4</strong>$<strong>개</strong>의 총합. 아니라면 $0$점.</li>
	<li><strong>Full House</strong>: 주사위 눈이 <strong>정확히 두 종류</strong>로 이루어져 있고 한 종류는 $3$개, 다른 종류는 $2$개일 때, 주사위 눈 $5$개의 총합. 아니라면 $0$점.</li>
	<li><strong>Little Straight</strong>: 주사위 눈이 $1$, $2$, $3$, $4$, $5$의 조합이라면, 즉 $1$에서 $5$까지의 눈이 한 번씩 등장했다면 $30$점, 아니라면 $0$점.</li>
	<li><strong>Big Straight</strong>: 주사위 눈이 $2$, $3$, $4$, $5$, $6$의 조합이라면, 즉 $2$에서 $6$까지의 눈이 한 번씩 등장했다면 $30$점, 아니라면 $0$점.</li>
	<li><strong>Yacht</strong>: 동일한 주사위 눈이 $5$개라면 $50$점, 아니라면 $0$점.</li>
	<li><strong>Choice</strong>: 모든 주사위 눈의 총합.</li>
</ul>

<p>모든 플레이어의 모든 족보가 사용되면 게임이 끝납니다.</p>

<p>지금은 한별이 차례입니다. 한별이는 첫 번째로 굴린 주사위의 조합에서 세 개의 주사위를 고정하고 나머지 두 개의 주사위를 다시 굴려야 하는 상황입니다. 이 상황에서 나올 수 있는 점수의 최댓값은 얼마일까요?</p>

### 입력 

 <p>첫 번째 줄에는 이미 선택한 족보를 의미하는 $12$글자의 문자열이 주어집니다. 문자열의 모든 글자는 <span style="color:#e74c3c;"><code>Y</code></span> 또는 <span style="color:#e74c3c;"><code>N</code></span>이며, 글자들 중 적어도 하나는 <span style="color:#e74c3c;"><code>Y</code></span>입니다.</p>

<ul>
	<li>$1$번째 글자가 <span style="color:#e74c3c;"><code>Y</code></span>라면 <strong>Ones</strong>를 선택할 수 있습니다. 마찬가지로 $6$번째 글자까지 같은 규칙이 적용되어, $6$번째 글자가 <span style="color:#e74c3c;"><code>Y</code></span>라면 <strong>Sixes</strong>를 선택할 수 있습니다.</li>
	<li>$7$번째 글자가 <span style="color:#e74c3c;"><code>Y</code></span>라면 <strong>Four of a Kind</strong>를 선택할 수 있습니다.</li>
	<li>$8$번째 글자가 <span style="color:#e74c3c;"><code>Y</code></span>라면 <strong>Full House</strong>를 선택할 수 있습니다.</li>
	<li>$9$번째 글자가 <span style="color:#e74c3c;"><code>Y</code></span>라면 <strong>Little Straight</strong>를 선택할 수 있습니다.</li>
	<li>$10$번째 글자가 <span style="color:#e74c3c;"><code>Y</code></span>라면 <strong>Big Straight</strong>를 선택할 수 있습니다.</li>
	<li>$11$번째 글자가 <span style="color:#e74c3c;"><code>Y</code></span>라면 <strong>Yacht</strong>를 선택할 수 있습니다.</li>
	<li>$12$번째 글자가 <span style="color:#e74c3c;"><code>Y</code></span>라면 <strong>Choice</strong>를 선택할 수 있습니다.</li>
</ul>

<p>각각의 경우에서 글자가 <span style="color:#e74c3c;"><code>N</code></span>이라면 해당하는 족보를 이미 선택하여 다시 선택할 수 없음을 의미합니다.</p>

<p>두 번째 줄에는 한별이가 첫 번째로 굴린 조합에서 고정한 주사위들의 눈의 수를 나타내는 $1$과 $6$ 사이의 정수 $3$개가 공백으로 구분되어 주어집니다.</p>

### 출력 

 <p>한별이가 얻을 수 있는 점수의 최댓값을 출력합니다.</p>

